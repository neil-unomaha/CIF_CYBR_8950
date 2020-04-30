import time, shlex, subprocess, json
from flask_restplus import Namespace, Resource
from flask import send_file

from .constants import ROUTER_ADDR

api = Namespace('palo', description='Palo API')

@api.route('/<string:page_num>')
@api.response(401, 'Unauthorized')
@api.response(200, 'OK')
class Palo(Resource):
    @api.doc(security=[])
    def get(self, page_num):
        if self.__is_invalid_page_num(page_num):
            return "Error: invalid page numer"
        
        cmd = '''curl -o /home/cif/palo_all_indicators.json -X GET "http://localhost:5000/indicators/?fmt=json&tags=scanner%2Cbotnet%2Cphishing%2Cmalware%2Cbruteforce%2Cdarknet&itype=ipv4" -H  "accept: application/json" -H  "Authorization: 5D8CCAE1B56E664D347F314C69721FA0DA2F816B11B8D7B72FBFB122EE304F4D"'''

        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.__init_page_output(page_num)

        return send_file("/home/cif/palo_paged_indicators.txt")
    
    def __is_invalid_page_num(self, page_num):
        if(page_num == None or page_num == ""):
            return True
        for character in page_num:
            if not(character.isdigit()):
                return True
        return False

    def __init_page_output(self, page_num):
        input_file = open('/home/cif/palo_all_indicators.json', 'r')
        output_file = open('/home/cif/palo_paged_indicators.txt', 'w')
        json_decode = json.load(input_file)
        all_indicators_dirty = []
        all_indicators_clean = []
        
        # all_indicators_dirty is a list of dictionaries containing only the "id" and "indicator" attributes
        # the items within the all_indicators_dirty list are sorted by the dictionary item's "id" attribute
        for item in json_decode:
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
                output_file.write(all_indicators_clean[index_count])
                output_file.write("\n")
                index_count += 1
        input_file.close()
        output_file.close()
        return
