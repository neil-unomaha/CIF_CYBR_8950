from flask import request, current_app, send_file
from .indicators import *

import json, os
from .constants import ROUTER_ADDR

import zmq
import io
from flask_restplus import Namespace, Resource, fields
from cif.constants import FEEDS_LIMIT, FEEDS_WHITELIST_LIMIT, \
    HTTPD_FEED_WHITELIST_CONFIDENCE, FEEDS_WHITELIST_DAYS
from cifsdk.constants import ROUTER_ADDR, VALID_FILTERS
from cifsdk.client.zmq import ZMQ as Client
from cifsdk.exceptions import AuthError, TimeoutError, InvalidSearch, \
    SubmissionFailed, CIFBusy

api = Namespace('palo', description='Palo API')


@api.route('/')
@api.response(401, 'Unauthorized')
@api.response(200, 'OK')
class Palo(Resource):
    @api.param('page_num','Page Number')
    @api.doc(security=[])
    def get(self):
        page_num = request.args.get('page_num')
        """Returns IPv4 indicators, one per line, 5,000 per page, max 150,000 indicators (30 pages)"""
        if self.__is_invalid_page_num(page_num):
            return "Error: invalid page number"
        out_file = io.StringIO()
        self.__init_page_output(page_num, out_file)
        byte_out_file = io.BytesIO()
        byte_out_file = io.BytesIO()
        byte_out_file.write(out_file.getvalue().encode('utf-8'))
        byte_out_file.seek(0)
        out_file.close()
        return send_file(byte_out_file, attachment_filename="palo_paged_indicators.txt")
        
    def __is_invalid_page_num(self, page_num):
        if(page_num == None or page_num == ""):
            return True
        for character in page_num:
            if not(character.isdigit()):
                return True
        return False

    def __init_page_output(self, page_num, out_file):

        filters = {
            'tags': 'botnet,phishing,malware,scanner,bruteforce,darknet',
            'itype': 'ipv4',
            'limit': '150000'
        }
        with Client(ROUTER_ADDR, os.getenv('CIF_TOKEN')) as client:
            results = client.indicators_search(filters)
        all_indicators_dirty = []
        all_indicators_clean = []


        # all_indicators_dirty is a list of dictionaries containing only the "id" and "indicator" attributes
        # the items within the all_indicators_dirty list are sorted by the dictionary item's "id" attribute
        for item in results:
            my_dict = {}
            my_dict['id'] = item.get('id')
            my_dict['indicator'] =item.get('indicator')
            all_indicators_dirty.append(my_dict)

        all_indicators_dirty.sort(key=lambda x: x["id"])

        # the "all_indicators_clean" list is the entire list of indicators
        for obj in all_indicators_dirty:
            all_indicators_clean.append(obj["indicator"])

        length_of_indicators = len(all_indicators_clean)

        # each page can contain no more than 5000 indicators
        # initialize index count based on paging
        index_count = (int(page_num) * 5000) - 5000
        
        for num in range(5000):
            if(index_count > length_of_indicators - 1):
                break
            else:
                out_file.write(all_indicators_clean[index_count])
                out_file.write("\n")
                index_count += 1

        return
