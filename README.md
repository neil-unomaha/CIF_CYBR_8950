# CIF Framework

## Executive Project Summary

The Collective Intelligence Framework, or CIF, is built to intelligently retrieve threat information from various sources, and use that information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based off these observations. The process is split into seven parts: parse, normalize, post process, store, query, share, and produce.  

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF holds a database of millions of records of threat intelligence. One source of the threat intelligence information is from Palo Alto hardware. Information is pulled from Palo Alto devices and pushed to CIF, then pushed to Palo Alto devices within CIF. At this time, a script is run once a day to automatically copy threats into a file, then manually added to the CIF. For this project, it is the aim to make this threat pulling process more automatic. Palo Alto will update their threat information numerous times a day, and it would be more effective to collect this information and push to CIF numerous times a day, rather than once a day. The goal is to pull information from Palo Alto every 15 minutes and update CIF with the information pulled.

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
![Gant Chart](/Assets/Gantt_Timeline.png "Project Timeline")

## Risk List

|Risk name  | Impact     | Likelihood | Description | Mitigation |
|-----------|------------|------------|-------------|------------|
|Developed API contains errors| 10 | 2 | Errors in code must be avoided at all costs. |Include peer review and pair programming practices throughout the code development prorcess.  Conduct manual and automated tests. |
|Developed API containers security vulnerabilities | 10 | 2 | Controls should be in place to provide assurance of the quality and security of the developed software. | Research what the most common security vulnerabilities are regarding APIs.  Ensure the code is peer reviewed. |
|Insufficient technical skills to develop API| 10 | 2 | The team must collectively possess the skills required to deliver the desired feature requests.  If the team does not possess the skills, the team must have resources available to them in order to acquire the needed skillset to complete the job. | The team must identify the software technologies they will be working with throughout the project. The team should determine if the team already possesses sufficient knowledge for each of these technologies.  If not, the team should ensure that resources are available to them in order to acquire this knowledge. |
|Roadblocks to setting up test environment | 5 | 4 | It is critical to setup a test environment in order to aid in the development and testing of the API.  | Step through the installation process within the CIF4 documentation. If trouble arises, consult Brian for assistance.|
|Developed API product has poor documentation| 10 | 1 | Poorly written documentation can sabotage even the best software products.  It is important that just as much effort goes into creating the documentation about the software as the software itself. | Research what comprises state of the art documentation.  Discover what principles and best practices should be followed. |





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
|Virtual Machine Software| No | All | CIF 4 runs in Ubuntu 16.04 Server.  Run a vm for Ubuntu 16.04.  |
|Ubuntu 16.04 Server| No | All | Required to run CIF4  |
|Docker| No | All | Docker image exists for CIF 4.  It is one of the methods for getting CIF4 installed.  |
|cifsdk| No | All | Install cif within the docker container  |
|Palo Alto API Documentation| No | All | Necessarty to familiarize ourselves iwth the Palo Alto documentation in order to build the requsted feature.  |
|Python| No | All | CIF4 is written in Python.  |
|Text Editor| No | All | For developing the code |


## First Sprint Plan
Progress of the Project is [tracked via Github issues](https://github.com/neil-unomaha/CIF_CYBR_8950/issues). Tracking sprints on [kanban board](https://github.com/neil-unomaha/CIF_CYBR_8950/projects)

## License
[MIT License](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/MIT-LICENSE)
