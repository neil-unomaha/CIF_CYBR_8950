# Milestone 3

## Progress Report (5/7/20)

### Overview

By the end of the second milestone, We technically had a CIF environment setup but we did not sufficiently understand how it worked in order to extend its functionality.  

By the end of the third milestone, we gained the necessary knowledge to implement the Palo Alto endpoint.  We conducted multiple code review session which resulted to [three functioning iterations of the Palo Alto endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/palo_endpoint_versions). The code along the way was made better in several ways, including providing better code comments and API documentation, increasing optimization, accounting for eventual edge cases that would cause issues, and writing [test coverage](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/test-file). 

During milestone 3 we informed the stakeholder of our progress, as well as the user-friendly [walk-through guide](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) we developed for installing CIF along with adding in our endpoint. The stakeholder requested we create a short presentation for him to share what we had created with other Universities, [and we delivered](https://app.vidgrid.com/view/8JmGblYqwkXE/?sr=0sOkk6).

The stakeholder was unable to setup a live implementation of CIF 4 with our included endpoint, so we were unable to execute our [originally planned methodology](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone_1.md#project-methodology). This would have involved comparing network traffic both before and after our Palo Alto extension within CIF.  However, the stakeholder was able to provide us two-and-a-half hours worth of network traffic data which we analyzed and were able to determine, in theory, the additional amount of blocked, malicious IPs had the firewall been actively using our CIF extension.  


### Outcomes

#### CIF Test Environment

We were aware since our last [realization report](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Milestone_2.md#project-realizationn) that setting up and understanding a CIF test environment was crucial. There is a [rich documented history](https://github.com/neil-unomaha/CIF_CYBR_8950/issues/20) of all the roadblocks we faced as we gained a better understanding of the CIF test enviornment in order to properly extend it. Two particular milestones stand out.  One was were figuring out how to whitelist the Palo Alto endpoint so that a token was not needed to be passed in.  The other was getting a version of our Palo endpoint up and running. We not only successfully created the endpoint, but we iterated through three functioning versions.

#### Palo Endpoint Versions

* Version one was monumental because our endpoint was functioning, but it left much to be desired. The implemention involved using the `curl` command within our endpoing which called another, existing endpoint with specified options.  Upon that request returning its results, our endpoint set out formatting the output in an ingestible format according to Palo Alto constraints.  Two identified issues were identified: one was that we were creating an unnecessary dependency.  If the underlying end point changed it would likely break our endpoint, and this could entirely be avoided. The other identified issue was that this strategy was inefficeint. Calling our endpoint would require significant overhead since the request essentially invokes another request that, in turn, occupys an additional gunicorn worker.

* The second version improved upon the first version by no longer invoking another endpoint via the `curl` command. What we did instead was we imported all the necessary modules into our endoint so that we could query the database exactly like how the other endpoint was doing it. This provided our endoint the desired functionality, removed the dependency on the other endpoint, and improved the efficiency of the request. More areas were identified to be improved.  In both versions one and two, we were writing the IP addresses pulled from the database to a temporary file on disk.  This is an inefficient way of managing data, but what was more concerning: our implementation made it possible for a race condition to ensure which could result in improper responses, or worse the server crashing.  Our implementation had all requests reading and writing to the same file.  If two or more requests were made very close to one another, a race condition would ensure. The other area of improvement was related to the paging mechanism.  Palo Alto constrains specify that no external block list can include more than 5,000 IP addresses.  We implemented our paging mechanism via [Flask's variables rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules).  In example: `localhost:5000/palo/1` would return the first set of 5,000 IP addresses, `localhost:5000/palo/2` would return the second set of 5,000 IP addresses, and so on.  After discussion we realized that this was likely not an ideal place to implement a variable rule.  Nothing about the url provide clues to the user that the `1` within `localhost:5000/palo/1` represents the first page.  There was a more explicit, and more appropriate way to specify that paramter. 

* The third and final version was revised to no longer write to a file on disk, but rather write to a file in memory via the [StringIO module](https://docs.python.org/3/library/io.html). This removed the race condition that would occur if two requests happened at the same time, and since all the processing was done in memory it improved efficencly.  The variable rule for the paging parameter was removed, and it was replaced by the more explicit way of designating parameters: `localhost:5000/palo/?page_num=1`.

### Hindrances

One of the first obstacles was the documentation on CIFv4's [wiki page](https://github.com/csirtgadgets/cifsdk-v4-py/wiki) had some gaps in its explanations and the team had to fill in said gaps for test environment setup. In addition, some code examples provided in the [documentation](https://github.com/csirtgadgets/verbose-robot/wiki/Introducing-the-CIF-client) did not work as expected.

Once the CIF test environment was set up, we transitioned to work on the Palo Alto endpoint. When initially looking at Dynamic Block Lists with Palo Alto as a solution, there was an issue where the HTTP requests sent from Palo Alto could not include CIF required tokens for authorization. However, in researching and gaining a better understanding of CIF, we were able to find a way to implement this endpoint in such a way that a token was not required.

## Final Report

* List out accomplishments across the project pulling from milestone 1 and deliverables achieved in 2 and 3

## Research Paper

* Later link to finished research paper
