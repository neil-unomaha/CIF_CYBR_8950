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
| ------------* | ------------* |
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
|Compatibilties and Format Issues| 4 | 5 | Any issues with getting the data  formated correctly for CIF to ingest or for Palo Alto to use to block IP address. | Proper testing and verfication that the CIF server andd  Palo Alto boxes can ingest and implment the data correctly. |
|Developed API contains errors| 5 | 2 | Errors in code must be avoided at all costs. |Include peer review and pair programming practices throughout the code development process.  Conduct manual and automated tests. |
|Performance  Issues with CIF or Palo Alto | 2 | 3 | Issues that arrise from are change with the API. This is caused by the influx of traffic since we are running every 15 minutes. | Monitor before and after the implementation to see the changes to network traffic.  Then to opitzme the API or change the time frame for refreshes to 30 minutes. |
|Developed API product has poor documentation| 4 | 1 | Poorly written documentation can sabotage even the best software products. It is important that just as much effort goes into creating the documentation about the software as the software itself. | Research what comprises state of the art documentation.  Discover what principles and best practices should be followed. |

## Project Methodology

**Note:** Brian mentioned that most Universities in this collective intelligence network only push every 24hrs.  However, at least one University, Duke, pushes more often. This provides us the opportunity to perform before/after measurements as described below.

### Baseline Measurement

* Measure the number of new threats ingested into Palo Alto firewalls within a 24hr period within the current system.
  * Spoke with customer and he confirmed he can set up a Palo Alto firewall with a rule to collect a 7-day log report for us to use as a baseline measurement for blocked IPs during that period

### Build and Implement Solution

* Extend CIFv4 API

  * Build an additional endpoint into CIF server which outputs a list of IP indicators in Palo Alto ingestible format
    * Indicators are retrieved from other universities under the CIF framework

### Conduct Post-Solution Measurement

* Generate Palo Alto report to show blocked IPs after endpoint implementation and compare with baseline metrics gathered

* Calculate and document any differences perceived following implementation

----

### Technical Plan

In order to arrive at our solution, it is necessary to break it down into pieces.  In this section we hope to do just that. 

After doing an initial review of the [CIFv4 codce](https://github.com/csirtgadgets/verbose-robot), as well as the [CIFv4 documentation](https://github.com/csirtgadgets/verbose-robot/wiki), we recognized that there are various technologies that we need to learn:

* Python

CIFv4 is mostly written in Python.  Some of the team members had a limited amount of experience with Python, while others had none.  Resources available which we will reference is the [Python Documentation](https://docs.python.org/3/), a course on [lynda.com](https://www.lynda.com/Python-tutorials/Python-Essential-Training/614299-2.html?srchtrk=index%3a21%0alinktypeid%3a2%0aq%3apython%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2), as well as [w3 schools](https://www.w3schools.com/python/default.asp).

* Flask

Flask is a web framework and is used in CIF.  We will familiarize ourselves with Flask via the [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/), as well as [this course](https://www.lynda.com/Flask-tutorials/Flask-Essential-Training/2822169-2.html?srchtrk=index%3a1%0alinktypeid%3a2%0aq%3aflask%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2), and [thish course](https://www.lynda.com/Flask-tutorials/Building-RESTful-APIs-Flask/794143-2.html?srchtrk=index%3a3%0alinktypeid%3a2%0aq%3aflask%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2) on Lynda.com


* Familiarize ourselves with Python

  * CIF is written in Python

* Setup a test environment for CIF

  * Brian will provide to us a test environment with CIFv3
  
  * We will set up our own VMs with CIFv4

* Familiarize ourselves with CIF at the UI
 level
  
  * This includes common commands and features of CIF, including but not limited to: querying CIF database, adding/removing feeds

* Familiarize ourselves with CIF at the code level

  * Like most software applications, CIF is a an aggregate application which is composed of several other libraries working together.   The [requirements.txt](https://github.com/csirtgadgets/bearded-avenger/blob/master/requirements.txt) file is a good starting place

  * CIF is modularized into at least 5 CIF-related libraries, and has additional dependencies, and also possesses dependencies on other libraries.

  * Flask is used as a web application framework and used within this project, thus we may look into this framework to build our solution based off of it

* Develop the solution
  * Develop extension to work in conjuction of YML files that bidirectionally share CIF information between universities
    * Require extension to ingest IP indicators from YML files
    * Format retrieved IP indicators into Palo Alto ingestible file format
    * Have extension refer to specific file directory to place files of retrieved IP indicators

  * Implement Palo Alto API to refer to directory on CIF server to import files from

* Test the solution

  * Ensure the extension properly formats and put IP indicators into Palo Alto ingestible format

  * Ensure it is gathering the correct information from Palo Alto requests from CIF database

  * Ensure extension is sending off requested information to Palo Alto devices efficiently

  * Ensure Palo Alto devices are ingesting files as expected


* Deploy the solution to production

* Submit pull request

### Literature Review and Research

#### [Literature and Research](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Literature-Research.md)

#### Research Questions

* To what extent does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting?

**Keywords:** Web Services, Systems Architecture Integration, Process Automation

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
