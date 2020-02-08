# CIF Framework

## Executive Project Summary

The Collective Intelligence Framework, or CIF, is built to intelligently retrieve threat information from various sources, and use that information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based off these observations. The process is split into seven parts: parse, normalize, post process, store, query, share, and produce.  

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF holds a database of millions of records of threat intelligence. One source of the threat intelligence information is from the company, Palo Alto. Information is pulled from Palo Alto and pushed to CIF, then pushed to Palo Alto devices within CIF. At this time, a cron job is used once a day to automatically copy threats into a file, then manually added to the CIF. For this project, it is the aim to make this threat pulling process more automatic. Palo Alto will update their threat information numerous times a day, and it would be more effective to collect this information and push to CIF numerous times a day, rather than once a day. One potential goal is to utilize the Palo Alto API to pull this information and automatically copy the threats to CIF. Another potential goal may to pull the threats from CIF and push them to the Palo Alto devices directly. 


### Goals and Objectives

* Familiarize ourselves with the CIF framework to better understand the system
* Setup sandbox environment with CIF
* Research Palo Alto documentation and other resources to better understand the API
* Look into using the Palo Alto API to automate any processes within the CIF framework
* Document key findings and processes that were attempted in the sandbox environment

### Merit

If we can effectively implement tools from the Palo Alto API to the CIF Framework, this will help to automate some of the processes within the system. This can remove some of the manual, tedious task(s) that must be done with the framework. With proper implementation, this could also eliminate risk associated with human error within the framework, as it would be done automatically. If deemed appropriate, this could also be shared with other colleges/organizations that utilize the CIF framework. However, if in the event we are unable to accomplish this, the fallback would be to pull threat from the CIF, and automatically push them to the Palo Alto devices. This would still accomplish a more automated process.

## Project Timeline

* Come up with task list and projected deadlines for said tasks
* Look at [ganttpro](https://ganttpro.com/) for making a planning chart

## Risk List

|Risk name  | Impact     | Likelihood | Description | Mitigation |
|-----------|------------|------------|-------------|------------|
|Sample name| 1-10 | 1-10 | Some description | How to avoid it |
| another example | 1-10 | 1-10 | Some description | How to avoid it|

## Project Methodology
- *Probably first do the research, set up test environment, get a feel of the environment, start testing Palo Alto API calls and document what worked and what didn't. Maybe start around there? Eventually try to set it up in a way that it can be applied in the field?*

### Literature Review and Research

#### Research Questions
* What are the barriers/enablers of api integration for a CIF? 
* If there are barriers, how can they be mitigated?
* How does mitigating the barriers increase efficiency?
* What are the required attributes for a CIF framework to be used in a university setting?
* To what degree does the current CIF satisfy those required API  endpoints?



**Keywords:** [put in keywords here to use when looking for literature]

1. **[Title of the document]**  
**Authors:**  
**Date Published:**  
**Published in:**  
**Summary:**  

### Technical Plan
**High-Level Project Overview** 
- *Probaby a hierarchical bulleted list*

## Resources/Technology Needed

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|Some resource| No | Bob | Some description  |

## First Sprint Plan
* Link to Kanban board on github (probably issue based)

## License
* TBD
