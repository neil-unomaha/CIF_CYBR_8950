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
|Developed API contains errors| 5 | 2 | Errors in code must be avoided at all costs. |Include peer review and pair programming practices throughout the code development process.  Conduct manual and automated tests. |
|Developed API product has poor documentation| 4 | 1 | Poorly written documentation can sabotage even the best software products. It is important that just as much effort goes into creating the documentation about the software as the software itself. | Research what comprises state of the art documentation.  Discover what principles and best practices should be followed. |

## Project Methodology

**Note:** Brian mentioned that most Universities in this collective intelligence network only push every 24hrs.  However, at least one University, Duke, pushes more often. This provides us the opportunity to perform before/after measurements as described below.

### Baseline Measurement

* Measure the number of new threats ingested into Palo Alto firewalls within a 24hr period within the current system.

### Build and Implement Solution

* Build an extension into CIFv3  and/or CIFv4 Python library to:
  * Pull retrieved IP indicators for Palo Alto in ingestible format.
    * Indicators are retrieved from other universities under the CIF framework

  * Save retrieved IP indicators to file with no more than 5,000 indicators per file, as [referenced in page 60 of Palo Alto API](https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/framemaker/pan-os/7-1/pan-os-panorama-api.pdf).

  * Have CIF push generated files to Palo Alto via the Palo Alto API every 15 minutes.
    * [Palo Alto API Documentation on importing files](https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/framemaker/pan-os/7-1/pan-os-panorama-api.pdf)

### Conduct Post-Solution Measurement

* Gather metrics and compare before/after extension implementation

  * Example: a threat reported in 24 hrs (before) vs a threat reported at 1am (23hrs savings)

  * Example: a threat reported in 24hrs (before) vs a threat reported at 5am (19hrs savings)

* Calculate and document any differences perceived following implementation

----

### Technical Plan

In order to arrive at our solution, it is necessary to break it down into pieces.  Below are a list of tasks to complete in order to accomplish our desired solution.

* Familiarize ourselves with Python

  * CIF is written in Python

* Setup a test environment for CIF

  * Brian will provide to us a test environment with CIFv3.
  
  * We will set up our own VMs with CIFv4

* Familiarize ourselves with CIF at the UI
 level
  
  * This includes common commands and features of CIF, including but not limited to: querying CIF database, adding/removing feeds

* Familiarize ourselves with CIF at the code level

  * Like most software applications, CIF is a an aggregate application which is composed of several other libraries working together.   The [requirements.txt](https://github.com/csirtgadgets/bearded-avenger/blob/master/requirements.txt) file is a good starting place.
  * CIF is modularized into at least 5  CIF-related libraries, and has additional dependencies, and also possesses dependencies on other libraries.
  * Flask is used as a web application framework and used within this project, thus we may look into this framework to build our solution based off of it

* Develop the solution
  * Develop extension to work in conjuction of YML files that bidirectionally share CIF information between universities
    * Require extension to ingest IP indicators from YML files
    * Format retrieved IP indicators into Palo Alto ingestible file format
    * Have extension refer to specific file directory to place files of retrieved IP indicators
    * Check if latest file in directory is less than or equal to 5,000

      * If less, add IP indicators until it equals 5,000
      * If at 5,000, create new file in directory and add up to 5,000 IP entries
  * Implement Palo Alto API to refer to directory on CIF server to import files from

* Test the solution

  * Ensure our extension is properly creating Palo Alto ingestible files of IP indicators within 15 minute or less intervals.

  * Ensure the files do not exceeed 5,000 IP indicators

  * Ensure our extension pushes the indicators to Palo Alto, and Palo Alto successfully ingests the indicators.

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
