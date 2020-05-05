# Milestone 3

## Progress Report (5/7/20)

### Overview

By the end of the second milestone, We technically had a CIF environment setup but we did not sufficiently understand how it worked in order to extend its functionality. We had pseudocode for steps of writing the new endpoint, as well as a possible implemention, but the solution had yet to be written.  

By the end of the third milestone, we gained the necessary knowledge to implement the Palo Alto endpoint.  We conducted multiple code review session which resulted to [three functioning iterations of the Palo Alto endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/palo_endpoint_versions). The code along the way was made better in several ways, including providing better code comments and API documentation, increasing optimization, accounting for edge cases that would cause issues, and writing [test coverage](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/test-file). 

During milestone 3 we informed the stakeholder of our progress, and we wrote for him a user-friendly [walk-through guide](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) on how to install CIF and how to add in our endpoint, and we also included highlights of important features such as configuring threat feeds as well as how to add new indicators. The stakeholder requested we create a short presentation for him to share what we had created with other Universities, [and we delivered](https://app.vidgrid.com/view/8JmGblYqwkXE/?sr=0sOkk6).

### Outcomes

We made serveral outcomes within milestone three. By the end we met our stakeholders expectations by creating the desired Palo Alto endpoint.  A list of all our achievements are the following:

* [Setup a CIF test environment](https://github.com/neil-unomaha/CIF_CYBR_8950/issues/20)
* [Created the Palo Alto Endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/cif-palo-changes)
* Iterated through [three functioning versions of the Palo Alto Endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/tree/master/palo_endpoint_versions)
* [Wrote test coverage on our endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/test-file/test_basics.py)
* [Developed a user-friendly walkthrough guide](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) of setting up CIF version 4 with our endpoint
* As requested by stakeholder, [recorded a quick 2-minute video presentation](https://app.vidgrid.com/view/8JmGblYqwkXE/?sr=0sOkk6) highlighting what we achieved
* [Analyzed 2.5hrs of network traffic](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/SanitizedParsedPackets.csv) to derive a [theoretical model](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/milestone_3.pptx) of the impact ob timely threat intelligence gathering, aggregation and sharing on risk profile reduction


### Hinderances

One of the first obstacles was the documentation on CIFv4's [wiki page](https://github.com/csirtgadgets/cifsdk-v4-py/wiki) had some gaps in its explanations.  CIF was largely written, and is currently maintained, by a single individuaul, so the gaps in documentation is understandable. The team had to troubleshoot various installation issues they encounted which is [well documented in the our capstone repo of issues](https://github.com/neil-unomaha/CIF_CYBR_8950/issues/20).  

Another hurdle involved the methodology on how we were going to conduct our analysis.  Our original analysis would have involved the following:
* Pull a report from Palo Alto to examine the amount of blocked IPs over a seven day period resulting from the existing, daily blocking strategy of CIF
* Implement our solution and configure a 15-minute blocking strategy on Palo Alto
* Pull another seven day report of blocked IPs from CIF with the 15-minute blocking strategy
* Compare the two reports

Unfortunately, due to fallout from COVID-19, the manpower was not available at UNL to setup a CIF version four instance with our endpoint, and to conduct either of the seven day reports.  

We overcame this hinderance by analyzing the network traffic the stakeholder was able to provide to us.  Our stakeholder provided us with [two-and-a-half hours of network traffic](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/SanitizedParsedPackets.csv) along with the previous day's listing of newly added IPs to block from CIF.  With this data, we were able to derive a theoretical model by applying those newly added blocked IPs to the network traffic.  We describe in more detail our analysis strategy in both our presentation, as well as our research paper.

## Final Report

* List out accomplishments across the project pulling from milestone 1 and deliverables achieved in 2 and 3

## Research Paper

* Later link to finished research paper
