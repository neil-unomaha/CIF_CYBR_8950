# Milestone 3

## Progress Report (5/7/20)

### Overview

By the end of the second milestone, We had a functioning test environment and were in the process of getting a functioning implementation of the Palo Alto endpoint set up.  By the end of the third milestone, we not only successfully created the Palo Alto endpoint, but after multiple code review sessions we ended up iterating through three functioning versions of the Palo Alto endpoint. The code was made better in a number of ways, including providing better code comments and API documentation, optimization, and accounting for eventual edge cases that would cause issues. 

We informed the stakeholder of our progress and informed him of the [walkthrough guide](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) we developed to provide a more user-friendly guide to installing CIF along with including our endpoint.   The stakeholder requested we create a short presentation for him to share what we had created with other Universities, [and we delivered](https://app.vidgrid.com/view/8JmGblYqwkXE/?sr=0sOkk6).

### Outcomes

#### CIF Test Environment

It was documented in the last [realization report](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone%202.md#Project-Realization) that proper set up of the CIF test environment had to be handled in the beginning of the project. Since the [original setup](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone%202.md#Environment-Setup-and-Hardships), the team has learned more about CIF when it came to initial installation and about its codebase. In particular, the team was able to find the CIF file that specifies endpoints in app.py. From here, a Palo Alto endpoint was created and tested. This endpoint will be further explained below.

#### API Endpoint

The Palo Alto API endpoint was the most significant portion of this project. In milestone 2, it was stated that the team would be looking into use Palo Alto Dynamic Block Lists to directly access the CIF server and request latest feeds. Palo Alto would use an external IP address to the database to request feeds via an HTTP request, and the endpoint would listen for these requests and reply with file pages of IP address for Palo Alto to block. A Palo Alto endpoint was created and then added in the app.py file to allow integrate it into CIF. The endpoint had gone under three revisions:

* The first version essentially used a curl command within the endpoint itself which called another existing endpoint in the CIF environment. The results of the curl command were outputted and formatted into a file following Palo Alto's constraints to be sent. However, there were two issues identified with this solution. It was that it was inefficient and it made an unnecessary dependency for the Palo Alto endpoint.

* The second version removed the curl implementation and instead queried the database directly using an existing object relational mapper. It was an immense improvement, but some vulnerabilities in this implementation existed. For both the first and second version, they outputted results to a file and when sent, caused the server to crash. In addition, this implementation was still inefficient.

* Version three was built upon version two and implemented a few improvements. The output of the database query was not written to a file but wrote into a file in memory via the python module. The other major change was regarding a passed parameter. It was found to be better design to pass a page number as an actual parameter (i.e. `/?page_num=1`) as opposed to using a variable rule to represent it (i.e. `/1`). The variable rule was not as self-explanatory as passing in a page number as a parameter.

As it stands, we are hoping the final version of this endpoint can be implemented in a larger test environment for further testing. Details on how to set this were made [available](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) to the stakeholder.

### Hindrances

One of the first obstacles was the documentation on CIFv4's [wiki page](https://github.com/csirtgadgets/cifsdk-v4-py/wiki) had some gaps in its explanations and the team had to fill in said gaps for test environment setup. In addition, some code examples provided in the [documentation](https://github.com/csirtgadgets/verbose-robot/wiki/Introducing-the-CIF-client) did not work as expected.

Once the CIF test environment was set up, we transitioned to work on the Palo Alto endpoint. When initially looking at Dynamic Block Lists with Palo Alto as a solution, there was an issue where the HTTP requests sent from Palo Alto could not include CIF required tokens for authorization. However, in researching and gaining a better understanding of CIF, we were able to find a way to implement this endpoint in such a way that a token was not required.

## Final Report

* List out accomplishments across the project pulling from milestone 1 and deliverables achieved in 2 and 3

## Research Paper

* Later link to finished research paper
