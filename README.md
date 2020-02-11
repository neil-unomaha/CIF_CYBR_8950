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
|Developed API contains errors| 10 | 2 | Errors in code must be avoided at all costs |Include peer review practices in the code development prorcess.  Conduct automated tests. |
|Developed API containers security vulnerabilities | 10 | 2 | Controls should be in place to provide assurance of the quality and security of the developed software | Research what the most common security vulnerabilities are regarding APIs.  Ensure the code is peer reviewed. |
|Insufficient technical skills to develop API| 10 | 2 | The team must collectively possess the skills required to deliver the desired feature requests.  If the team does not possess the skills, the team must have resources available to them in order to acquire the needed skillset to complete the job. | The team must identify the software technologies they will be working with throughout the project. The team should determine if the team already possesses sufficient knowledge on each of these software components.  If not, the team should ensure that resources are available to them in order to acquire this knowledge. |
|Roadblocks to setting up test environment | 5 | 2 | It is critical to setup a test environment in order to aid in the development and testing of the API  | Step through the installation process within the documentation. If trouble arises, consult Brian for assistance.|
|Developed API product has poor documentation| 10 | 1 | Poorly written documentation can sabotage even the best software products.  It is important that just as much effort goes into creating the documentation about the software as the software itself. | Research what comprises state of the art documentation.  Discover what principles and best practices should be followed. |
|University policies prevent usage of feature| 7 | 1 | Large enterprise often have complex approval policies.  It is possible that we might complete all the objectives, but due to security concern, the feature may be halted from going live. | Brian is our main point of contact and a key stakeholder for cyber security within UNO.  It is important we maintain communication with him throuout our progress. |




## Project Methodology

We will begin this project by conducting thorough research and reviewing literature that pertains to the research questions listed below. Any notes or interesting information that could be useful for the project that accesses the research questions will be documented. Following the research, we will read through documentation to better understand the CIF framework, how it is implemented, how it is set up, how it is used, etc. Following, a test environment will be setup using the CIF documentation provided to get a better understanding of the framework.  

Following setup of CIF, we hope to shift our focus on Palo Alto documentation to learn more about its API and try to find ways to implement it in such a way that we can pull information from the organization and upload it to CIF. Barriers that could affect this API integration will be identified and investigated for any mitigations. Any information that could be of significance throughout the entire process will be documented for other team members, or for others that work with CIF to refer to.  

### Literature Review and Research

#### [Literature and Research](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Literature-Research.md)

#### Research Questions

* What are the barriers/enablers of API integration for a CIF?
* If there are barriers, how can they be mitigated?
* How does mitigating the barriers increase efficiency?
* What are the required attributes for a CIF framework to be used in a university setting?
* To what degree does the current CIF satisfy those required API  endpoints?

**Keywords:** Dockerization Hardening, Web Services, Systems Architecture Integration, Process Automation

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
