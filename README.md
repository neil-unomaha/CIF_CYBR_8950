# CIF Framework

## Executive Project Summary

The Collective Intelligence Framework, or CIF, is built to intelligently retrieve threat information from various sources, and use that information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based on these observations. The process is split into seven parts: parse, normalize, post-process, store, query, share, and produce.  

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF holds a database of millions of records of threat intelligence. One source of the threat intelligence information is from Palo Alto hardware. Information is pulled from Palo Alto devices and pushed to CIF, then pushed to Palo Alto devices within CIF. At this time, a script is run once a day to automatically copy threats into a file, then manually added to the CIF. For this project, it is the aim to make this threat pulling process more automatic. Palo Alto will update their threat information numerous times a day, and it would be more effective to collect this information and push to CIF numerous times a day, rather than once a day. The goal is to pull information from Palo Alto every 15 minutes and update CIF with the information pulled.

### Goals and Objectives

* Familiarize ourselves with the CIF framework to better understand the system
* Setup sandbox environment with CIF
* Research Palo Alto documentation and other resources to better understand the API
* Reduce threat intelligence collection and distribution from one day to 15 minutes
* Enable process automation between CIF framework and Palo Alto by using/creating appropriate APIs
* Document key findings and processes that were attempted in the sandbox environment

### Merit

If successful, our contribution will reduce the time it takes to propogate threat intelligence within an enterprise environment.  As a result, security risk will be reduced.  It is noteworthy that the middleware removes a process that is currently conducted manually.  The automated nature of the midddleware removes the factor of human error, thus increasing overall security reliability.  Lastly, middleware that fuses together threat intelligence with a next generation firewall makes said firewall more effective.  Our solution could be incorporated, or in the very least serve as a template, for enterprises looking for ways to augment their firewall and further develop their security landscape. 

## Project Timeline

This is a rough outline of each weeks project goals. The team came together to make a timeline that follows the milestone markers and other events that might occur. This timeline is suspected to change as the project goes on or if the team hits any faults along the way. A Gantt chart can be seen below for a better look at the team distribution of work.

| Week          | Area of Focus    |
| ------------- | ------------- |
| 0-3           | CIF Environment set up and stabilization.<br> Project Realization will be used to develop a plan for the future. As well as documentation. |
| 4-6           | Finishing goals and Project Realization.<br> Documentation and Presentation planning for the milestone two presentation. |
| 7-10           | Progress of Realization report and Handling any unforeseen events.<br> Packaging of the API and testing will be done.<br> The final report will be started. |
| 11-12            | Final testing and packaging of CIF API.<br> As well as presentation planning. |

![Gant Chart](/Assets/Gantt_Timeline.png "Project Timeline")

## Risk List

|Risk name  | Impact     | Likelihood | Description | Mitigation |
|-----------|------------|------------|-------------|------------|
|Roadblocks to setting up test environment | 10 | 4 | It is critical to set up a test environment to aid in the development and testing of the middleware.  | Step through the installation process within the CIF4 documentation. If trouble arises, consult Brian for assistance.|
|Insufficient technical skills to develop API| 7 | 3 | The team must collectively possess the skills required to deliver the desired feature requests.  If the team does not possess the skills, the team must have resources available to them to acquire the needed skill set to complete the job. | The team must identify the software technologies they will be working with throughout the project. The team should determine if the team already possesses sufficient knowledge for each of these technologies.  If not, the team should ensure that resources are available to them to acquire this knowledge. |
|Developed API contains security vulnerabilities | 10 | 2 | Controls should be in place to assure the quality and security of the developed software. | Research what the most common security vulnerabilities are regarding APIs.  Ensure the code is peer-reviewed. |
|Developed API contains errors| 5 | 2 | Errors in code must be avoided at all costs. |Include peer review and pair programming practices throughout the code development process.  Conduct manual and automated tests. |
|Developed API product has poor documentation| 4 | 1 | Poorly written documentation can sabotage even the best software products. It is important that just as much effort goes into creating the documentation about the software as the software itself. | Research what comprises state of the art documentation.  Discover what principles and best practices should be followed. |




## Project Methodology

We will begin this project by conducting thorough research and reviewing literature that pertains to the research questions listed below. Any notes or interesting information that could be useful for the project that accesses the research questions will be documented. Following the research, we will read through the documentation to better understand the CIF framework, how it is implemented, how it is set up, how it is used, etc. Following, a test environment will be set up using the CIF documentation provided to get a better understanding of the framework.  

Following set up of CIF, we hope to shift our focus on Palo Alto documentation to learn more about its API and try to find ways to implement it in such a way that we can pull information from the organization and upload it to CIF. Barriers that could affect this API integration will be identified and investigated for any mitigations. Any information that could be of significance throughout the entire process will be documented for other team members, or for others that work with CIF to refer to.  

### Literature Review and Research

#### [Literature and Research](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Literature-Research.md)

#### Research Questions

* To what extent does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting?

**Keywords:** Dockerization Hardening, Web Services, Systems Architecture Integration, Process Automation

### Technical Plan

**High-Level Project Overview** 
A high-level view of our plan is to first familiarize ourselves with the CIF version 4 system along with the Dockerized system.  Along with setting up a sandbox CIF instance that has similar configurations to the current CIF system implemented on the University network the code for CIF version 4 will be analyzed and researched such that it could be determined if this version would be usable within the desired University setting.  Along with researching CIF, we must also research the Palo Alto system by examining the API documentation along with other resources that have been produced for this widely used system.

After we have thoroughly researched both CIF version 4 and Palo Alto, our next task that will be undertaken within our plan is to integrate CIF and Palo Alto.  We propose that this will be able to be done using the APIs that are available for both systems and we will create a form of middleware that will accomplish of taking the threat data from the Palo Alto System and automatically put that data into the CIF server for threat mitigation that is more rapid than the current system.


## Resources/Technology Needed

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
|Virtual Machine Software| No | All | CIF 4 runs in Ubuntu 16.04 Server.  Run a vm for Ubuntu 16.04.  |
|Ubuntu 16.04 Server| No | All | Required to run CIF4  |
|Docker| No | All | Docker image exists for CIF 4.  It is one of the methods for getting CIF4 installed.  |
|cifsdk| No | All | Install CIF within the docker container  |
|Palo Alto API Documentation| No | All | Necessary to familiarize ourselves with the Palo Alto documentation in order to build the requested feature.  |
|Python| No | All | CIF4 is written in Python.  |
|Text Editor| No | All | For developing the code |


## First Sprint Plan
Progress of the Project is [tracked via Github issues](https://github.com/neil-unomaha/CIF_CYBR_8950/issues). Tracking sprints on [kanban board](https://github.com/neil-unomaha/CIF_CYBR_8950/projects)

## License
[MIT License](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/MIT-LICENSE)
