# Milestone 3

## Project Realization

Since the second milestone, our team was able to better understand the CIF framework. Before, a Palo Alto endpoint was in its early stages in development during the second milestone, but after trial and error, the new endpoint has reached final stages and could be tested in a larger test environment soon.

### CIF Test Environment

It was documented in the last [realization report](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone%202.md#Project-Realization) that proper set up of the CIF test environment had to be handled in the beginning of the project. Since the [original setup](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone%202.md#Environment-Setup-and-Hardships), the team has learned more about CIF when it came to initial installation and about its codebase. In particular, the team was able to find the CIF file that specifies endpoints in app.py. From here, a Palo Alto endpoint was created and tested. This endpoint will be further explained below.

### Palo Alto

As explained previously in milestone 2, the team is not able to set up a test environment to test the interface between CIF and Palo Alto. However, testing could be made on the CIF test environment to simulate Palo Alto making requests to the CIF server for latest update feeds.

### API Endpoint

The Palo Alto API endpoint was the most significant portion of this project. In milestone 2, it was stated that the team would be looking into use Palo Alto Dynamic Block Lists to directly access the CIF server and request latest feeds. Palo Alto would use an external IP address to the database to request feeds via an HTTP request, and the endpoint would listen for these requests and reply with file pages of IP address for Palo Alto to block. A Palo Alto endpoint was created and then added in the app.py file to allow integrate it into CIF. One of the first roadblocks in accomplishing this was that CIF required tokens for authorization in the HTTP header when making requests. In researching and gaining a better understanding of CIF, we were able to find a way to implement this endpoint in such a way that a token was not required. The endpoint had gone under three revisions:

* The first version essentially used a curl command within the endpoint itself which called another existing endpoint in the CIF environment. The results of the curl command were outputted and formatted into a file following Palo Alto's constraints to be sent. However, there were two issues identified with this solution. It was that it was inefficient and it made an unnecessary dependency for the Palo Alto endpoint.

* The second version removed the curl implementation and instead queried the database directly using an existing object relational mapper. It was an immense improvement, but some vulnerabilities in this implementation existed. For both the first and second version, they outputted results to a file and when sent, caused the server to crash. In addition, this implementation was still inefficient.

* Version three was built upon version two and implemented a few improvements. The output of the database query was not written to a file but wrote into a file in memory via the python module. The other major change was regarding a passed parameter. It was found to be better design to pass a page number as an actual parameter (i.e. `/?page_num=1`) as opposed to using a variable rule to represent it (i.e. `/1`). The variable rule was not as self-explanatory as passing in a page number as a parameter.

As it stands, we are hoping the final version of this endpoint can be implemented in a larger test environment for further testing. Details on how to set this were made [available](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) to the stakeholder.

### Fallback: Bash Script

Since milestone 2, the potential bash script solution has been abandoned since a more internal, efficient solution was found.

## Final Report

* List out accomplishments across the project pulling from milestone 1 and deliverables achieved in 2 and 3

## Research Paper

* Later link to finished research paper