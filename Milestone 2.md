# Milestone 2

[Environment Setup and Hardships](#Environment-Setup-and-Hardships)  
[Project Realization](#Project-Realization)  
[Research Outline](#Research-Outline)  
[Research Abstract](#Research-Abstract)  
[Visuals and Diagrams](#Visuals-and-Diagrams)  

## Environment Setup and Hardships

The following shows how to set up a CIFv4 test environment with Ubuntu 16.04 server running in a virtual machine

### Installation

#### Install Ubuntu 16.04 server

First, you will need to download an [Ubuntu 16.04 server image](http://releases.ubuntu.com/16.04/) and create a virtual machine.  

Once you start up your virtual machine and log in, there are a couple more steps for our guide.  We wanted a GUI, so we installed the ubuntu-desktop extension:

`sudo apt-get update`  
`sudo apt-get install ubuntu-desktop`

#### Install Docker

Docker must be installed, as it is the container for CIFv4

`sudo apt install docker.io`

#### Install CIFv4 Docker Image

Install the CIFv4 container from docker hub

`sudo docker pull csirtgadgets/verbose-robot`

### Setup Before running Docker Container

Before running the docker container, you need to create required environment variables.

The first is `CIF_TOKEN` which will contain a randomly generated string.  This string ultimately becomes the bearer token passed into for all of your `GET` and `POST` requests via the request header for security. You can generate a random string with the following command on Ubuntu:

`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'`

The following is an example output string.

`525ff70def1b2b4eff3119451eabfa0ce3fa6316efb55fda075db08ac4a2feda`

The other two required environment variables are `MAXMIND_USER_ID` and `MAXMIND_LICENSE_KEY`, as explained [here](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton). [Maxmind](https://www.maxmind.com/en/home) will allow a user to create a free account within their settings, and provide an account ID and license for the two environment variables.

*Note: Maxmind will only display the full license key once, as stated on their page. Please be sure to save this securely save this key.*

![maxmind_key](https://user-images.githubusercontent.com/38234505/75952477-74fa4f00-5e74-11ea-8ace-ab3a8f594e15.PNG)

```
## MAXMIND Credentials
username: nthorne@unomaha.edu
Account_user ID: *****
License Key: *****
```

Here is an example command to set up these environment variables.  Note that you'll want to swap out the values for `MAXMIND_USER_ID` and `MAXMIND_LICENSE_KEY`.

```
export CIF_TOKEN=`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'
export MAXMIND_USER_ID=201001
export MAXMIND_LICENSE_KEY=3r8ESHRiFIsF
```

### Run CIF Container

With the environment variables all setup, the CIF docker image can now be run.

```
sudo docker run -e CIF_TOKEN="${CIF_TOKEN}" -e MAXMIND_USER_ID="${MAXMIND_USER_ID}" -e MAXMIND_LICENSE_KEY="${MAXMIND_LICENSE_KEY}" -it -p 5000:5000 -d --name verbose-robot csirtgadgets/verbose-robot:latest
```

* User will pass into the running docker container the three environment variables as specified above with the `-e` flag
* User will setup port forwarding on port 5000 with the `-p` flag
* User will need to run the docker container in a  daemon with `-d`
* For ease of referencing the docker container in the future, the container name will be referenced as `verbose-robot`

To confirm the docker container is running, the user can run `sudo docker ps`.

### Execute CIF Commands

To interact with CIF, the user can do so in two ways: the command prompt or with Swagger.

#### Command Prompt

For this option, `bash` needs to be running in the docker container. This can be accomplished with the following command:

`sudo docker exec -it verbose-robot /bin/bash`

* Now in a command prompt window within the container, [as indicated here](https://github.com/csirtgadgets/verbose-robot/wiki/Where-do-I-start), install the CIF client via:  `pip install 'cifsdk>=4.0.0a0'`

Within the container at this point, the `cif` command can be executed with various options to query the CIF database. Here are some example commands:

`cif --itype ipv4 --tags scanner`  
`cif --itype url --tags phishing`  
`cif --itype url --tags malware`  
`cif --itype ipv4 --tags botnet`  

![example_output](https://user-images.githubusercontent.com/38234505/75954931-70389980-5e7a-11ea-978a-03042c36aef5.PNG)

Note that by default, CIF is pulling feeds from preset specified providers every three minutes.  

#### Swagger

The other option is Swagger. On the VM running CIF, you can visit http://localhost:5000 to display a rest API GUI.

![swagger](https://user-images.githubusercontent.com/38234505/75951890-cb668e00-5e72-11ea-9d7d-0d9364429e6c.PNG)

It is important to note that the lock symbol next to each endpoint indicates that a token is required to be passed in for each request.  This is the string that was created and stored within the `CIF_TOKEN` environment variable earlier. Click the **Authorize** button and add the token.

Once the token has been added, you should be able to interact with the API in the GUI.  Click the **Try it Out** button which toggles the endpoint, then click **Execute**.

![execute_swagger](https://user-images.githubusercontent.com/38234505/75952373-29e03c00-5e74-11ea-88e8-4272a9dc2bf8.PNG)

Scrolling down will display the response: 

![swagger_response](https://user-images.githubusercontent.com/38234505/75952410-4a0ffb00-5e74-11ea-9208-89ef01f53014.PNG)

### Create Endpoints

The CIF file that specifies endpoints is in `app.py`.  We believe, in this docker container, the specific file is located here:

`/usr/local/lib/python3.6/site-packages/verbose_robot-4.0.1-py3.6.egg/cif/httpd/app.py`

Adding an endpoint should be as simple as the following:
```
@app.route('/')
  def hello_world():
    return 'Hello, World!'
```

Restart the server and try it out. Initial attempts did not work.

One possible explanation is because CIF is using [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html#), so the config might be this:
```
@api.route('/hello')
  class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}
```

We will have to try this.

-----

## Roadblocks

### Getting CIF4 Environment Setup and Familiarizing ourselves with how it Works

#### Setup Steps Taken

* Setup account on Maxmind because it is a [dependency for CIF4](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton)
* Installed VMware
* Installed Ubuntu 16.04 server on VMWare
  * (Note: [Cannot run on 16.04 Desktop](https://github.com/csirtgadgets/verbose-robot/wiki/FAQ#ubuntu-lts-desktop))
* Inside 16.04 server: installed Docker
* With Docker installed on the 16.04 Server: installed the CIF image from dockerhub
  * Follow [documentation installation steps under docker strategy](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton)
* Run the container
    * Command to run the container with necessary options [specified in documentation](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton)
* Open up a shell on the running container to query the running CIF server
  * [Command from documentation](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton): `sudo docker exec -it verbose-robot /bin/bash`
  *  [Step to install the CIF CLI/Client inside the container](https://github.com/csirtgadgets/verbose-robot/wiki/Where-do-I-start) appears to be unnecessary because the image already contains it, but ran the command anyway just in case: `pip install 'cifsdk>=4.0.0a0'`
* Specify queries against the CIF server

#### Issues Encountered

* Documentation contains gaps in explanations (implication that the reader already has significant familiarity with the topic and related technology).
* Majority of [code examples specified in documentation](https://github.com/csirtgadgets/verbose-robot/wiki/Introducing-the-CIF-client) do not work as specified.  Almost always require additional options
* It appears we can successfully query `CIF` at this time, but the issue is that in our test environment: there are no existing feeds, so it doesn't return anything.
  * Example: `cif --itype ipv4 --tags malware`
![example](https://user-images.githubusercontent.com/38234505/74463773-f4899500-4e57-11ea-9c73-cdd43b43e466.PNG)

#### Questions to be Answered

**- Is CIF currently pulling feeds in real-time, Or is pulling from feeds disabled by default?  If it is disabled, how do we enable it?**
  * It appears like the [Rules Directory](https://github.com/csirtgadgets/verbose-robot/tree/master/rules) is where the feeds are specified

**- How do we add additional feeds?**

#### Currently Known CIF Resources/Tutorials/Documentation

* [CIFv4 Server Code](https://github.com/csirtgadgets/verbose-robot)
* [CIFv4 CLI Client in Python](https://github.com/csirtgadgets/cifsdk-py-v4)
* [CIFv4 CLI Client in Go](https://github.com/JustinAzoff/cifsdk-go)
* [CIFv4 Wiki](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book)
* [CIFv3 Wiki](https://github.com/csirtgadgets/bearded-avenger-deploymentkit/wiki/The-CIFv3-Book)
* [CIF Maintainer's Blog](https://csirtgadgets.com/collective-intelligence-framework)
  * Wes Young (appears to be the creator behind CIF4)
  * Posts are not tutorials, mostly like journal entries/reflection on topics such as threat intelligence and writing open-source code.  
  * [Payment required to answer questions surrounding CIF](https://csirtg.io/support)
* [Presentation on CIF](https://www.youtube.com/watch?v=wrfMnGyQIU8)
  * Video discussing version 2 of CIF, provides a good overview of CIF, but beyond an introduction to CIF, the processes/procedures mentioned are outdated.

#### Forcasted Obstacles

* Our middleware will need to be in an environment where it has the necessary privileges to talk to both the Palo Alto API and to access the CIF CLI
  *  We will need to work closely with Brian to make sure that this environment exists, or we will need to work together to create this environment.

-----

## Project Realization

To fully realize the project what is needed is to gain a full understanding of both the CIF framework and Palo Alto.  Setting up a functional CIF test environment was the first step that needed to be realized as we are looking into using a newer version of the framework. At this time, there is not a need to set up a Palo Alto test environment as all the necessary work involved for the project will be on the CIF server environment. As we have done more research and gained a better understanding of Palo Alto and the interaction with CIF, we have come to the understanding that middleware is not an ideal solution. We have, however, came to a new plan objective for this project that involves Palo Alto retrieving threat information from CIF directly through a new API for us to design on CIF. This new API would respond to requests for paginated threat information.

### CIF Test Environment

The first task that needed to be accomplished to go forward with project realization was to set up the CIF environment.  The documentation for setting up the CIF environment is relatively sparse and thus it was necessary to create our installation document that allowed for more consistent installation.  The completed instructions, as well as the issues that had to be overcome, are documented [above](#Environment-Setup-and-Hardships).

### Palo Alto

Along with setting up the CIF environment was to research Palo Alto to understand how to interface between the two systems.  Since Palo Alto is a system that is enterprise-grade paid software/hardware, we couldn't set up a test environment.  We were able to understand how Palo Alto functions in retrieving new threat information from the documentation due to extensive documentation available online. It was through this that it was discovered that our original plan of creating a middleware to interface between Palo Alto and CIF would be not the most optimal method of realizing our project.

### API Endpoint

The final form that our project has taken after accomplishing the previous tasks is to have Palo Alto use Dynamic Block Lists to directly access the CIF server.  The CIF server will then respond to an HTTP request to an API that will be created with the threat information.  To create this API endpoint, it is necessary to get an understanding of how the CIF server serves its APIs.  CIF uses the Flask framework to serve APIs so it should be as simple as creating a new API with Flask that responds to an HTTP request with the paginated threat information.  This task is not as simple as first thought due to the CIF server requiring a bearer token for access to its APIs.  Unfortunately, the Palo Alto system for Dynamic Block Lists does not allow for the insertion of the header information in the requests that would have allowed for the insertion of a bearer token, and thus another solution had to be found.  

Instead of having Palo Alto give a token somehow, it was decided that the better solution would be to have an API that did not require a token at all.  Creating the new API endpoint was a relatively easy task that only required copying another API endpoint and editing it so it is now an endpoint called “Palo”.  To allow the API to be accessed without authentication required researching Flask and analyzing the current API endpoints.  The process that ended up being the correct one was discovered by adding logging which allowed the specific API endpoint to be whitelisted as not being authenticated within the system.

-----

## Research Outline

* Introduction

  * Problem Context
    * Explain CIF and its goals (high level)
      * Sharing malicious IPs with other universities to block
      * Explain how information is only exchanged once a day with other universities
      * This once-a-day exchange is not ideal, as some potential threats or attacks could be mitigated if the organizations and hardware is made aware of them within a more acceptable time window
  * Goal of paper/project
    * Answer Research question(s): To what extent does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting? If there are security efficacy outcomes, what are the costs?
  * The Rest of the paper will flow as...
    * Previous research/work
    * Methodology
    * Results and findings
    * Conclusion and further research considerations

* Background/Literature Review
  * Cyber Crime effects
    * 90% of organization have increased budgets (Bissell, et. al, 2018)
    * Ransomware attacks, phishing, breaches, etc. are increasing (Bissell, et. al, 2019)
    * Companies blocking IP addresses by using honeywords, fake passwords entered (K. Naik, V. Bhosale, and V. D. Shinde)
    * Other companies sharing intel reports for possible threats (J. Elmellas, “Knowledge is power: the evolution of threat intelligence”)
    * Security intelligence and threat sharing have the highest cost savings. 67% of respondents use it, average 2.26 million savings (includes costs of tech) (Bissell, et al. 2020)
    * Average cost of successful cyber attack is $1.1 million (Radware, 2018)
    * Equifax hack as so far cost $439 million and projected to exceed $600 million
  * Collective Intelligence
    * Describe the goals
      * Multiple organizations collecting and sharing information could benefit all members better than individually
    * Zhao and White try to define and create a baseline for a collaborative intelligence framework in their paper, based on the g-SIS model (2012)
  * University setting relevant to CIF project
    * In 2012, there was a GhostShell hack that attacked educational institutions from Australia to Korean music services. It caused the release of 13,000 users' details online (Stevenson, 2015).
    * Unnamed University in Japan announced a large-scale personal leak, caused by unauthorized access to Office365 (Kashiwazaki, 2018).
      * 24,000+ students, 23,000+ alumni, 12,451 members of staff, etc. laked information
        * Included name, affiliation, Email. For students, it also included the year of entrance and student ID
      * Information from insiders such as spreadsheets for internal work, and information from outsiders such as job applicants.

* CIF Information
  * CIF Architecture
    * Display diagram of current CIF process
      * Current pull and push process with Palo Alto firewalls
      * Explain CIF process
        * YML files with tokens from each university within CIF
        * Cron job that is run daily to retrieve updated information
        * Python and Flask details
      * Explain why current process is not most efficient
        * Current cron job works in a roundabout way
  * CIF Versions
    * Explain our reasoning to use CIFv4 and not v3
      * CIFv3 is in process of getting deprecated, so v4 is preferred
      * Mention CIFv3 server we were given access to for getting familiar with CIF

* Methodology
  * CIF Environment Research
    * Iterate again the research question
    * CIF Research
      * Uses Python >3.6 and Flask framework
      * Mention resources we used to learn more about Python and Flask
      * Getting familiar with Python and Flask
        * Used Lynda to research
  * CIF Test Environment Setup
    * VMs for v4
      * Built on Ubuntu Serer 16.04
    * Refer to Environment setup in Milestone 2 document for reference

  * Project goals to improve CIF
    * Build plug-in to listen from Palo Alto for database update requests
      * Take request, pull up-to-date data from CIF database and send to Palo Alto
    * CIF server should request updated information from other universities every 15 minutes, and put any retrieved information into the database in a Palo Alto ingestible file format

  * Developing and Testing
    * Implement goals mentioned previously into python script in CIFv4 environment
      * Document small fixes, issues, challenges, etc. we had to do for the script
    * Document testing is done
      * Add python script to the existing CIF environment, and record if it is listening to Palo Alto and sending an expected text file
    * Collect metric information about IP indicators being collected to block within the 15-minute intervals

* Results/Findings
  * Metric Analysis

    * Collect metrics from CIF about IPs that were blocked on just a day-to-day basis
    * Collect metrics from CIF about IPs that were blocked every 15 minutes (as often as Palo Alto should request updated information)
    * Compare findings and summarize differences found between the metrics
  * MORE INFORMATION PENDING

* Conclusion and further research considerations

  * Summarize findings, metrics, lessons learned, etc.
  * Submit a pull request for CIFv4
  * Areas for further research

-----

## Research Abstract

Malicious cyber-attacks on organizations have increased in frequency. Intrusion detection systems, network monitors, and threat intelligence sharing frameworks have struggled to handle the increased load of information. Timeliness of firewall updates is a crucial issue. Updates are taking hours instead of minutes and can leave the system and individuals vulnerable to attacks. This paper will delve into the effects of threat intelligence sharing timeliness with a university enterprise setting and a development effort focused on the rapid dissemination of threat intelligence to perimeter firewalls. This paper addresses the security efficacy and cost of updating the firewalls in a timely and consistent manner.

-----

## Visuals and Diagrams

### Basic CIF Infrastructure

![Diagram of CIF](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-basic.png)

* CIF is constantly making requests to the various threat feeds you configure it to pull from.  It takes the results from those threat feeds and stores them in a database.  

* Feed configurations are specified in `/etc/cif/rules` directory
* Clients will make requests to your CIF server too, at which point the server will pull out data from its local database, format it, and return it as a response.

### CIF Challenge

![CIF Challenge](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-challenge.png)

* The challenge is that CIF is not immediately able to integrate into popular firewalls such as Palo Alto
* Work is required to pull in indicators from CIF, format the output, and push those indicators to your network's firewall

### Middleware Solution

![Middleware Solution](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-middle_solution.png)

* Existing middleware solutions exist, such as MindMeld and panhandler

* Concern is about the maintainability of the middleware.  Is there a solution where middleware isn't needed?

### Suggested API Solution

![API Solution](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-api-solution.png)

* API solution: have an endpoint that a firewall calls, which returns indicators in an ingestible format for that firewall

### NU CIF Infrastructure

![NU CIF Infrastructure](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-nu-setup.png)

* NU uses the Palo Alto framework
* Currently, a CIF server sits on the UNL network

-----

## References

J. Elmellas, “Knowledge is power: the evolution of threat intelligence” ScienceDirect, pp. 1–5, Jul. 2016.

K. Naik, V. Bhosale, and V. D. Shinde, “Detection of Intruder using Honeywords and IP Blocking,” International Conference on “Computing for Sustainable Global Development,” vol. 4th, pp. 1819–1822, Mar. 2017.

Kashiwazaki, Hiroki. “Personal Information Leak in a University, and it's Cleanup.” ACM Digital Library, Proceedings of the 2018 ACM SIGUCCS Annual Conference (SIGUCCS ’18), Sept. 2018, dl-acm-org.leo.lib.unomaha.edu/doi/abs/10.1145/3235715.3235727.

Kelly Bissell, Ryan Lasalle, Floris Van Den Dool, and Josh Kennedy-White. 2018. Gaining Ground on the Cyber Attacker: 2018 State of Cyber Resilience. (April 2018). Retrieved February 23, 2020, from https://www.accenture.com/in-en/insights/security/2018-state-of-cyber-resilience-index

Kelly Bissell, Ryan M. Lasalle, and Paolo Dal Cin. 2019. Ninth Annual Cost of Cybercrime Study. (March 2019). Retrieved February 23, 2020, from https://www.accenture.com/us-en/insights/security/cost-cybercrime-study

Radware. “The Trust Factor.” Radware, www.radware.com/ert-report-2018/.

Stevenson, Alastair. “A Hacker Group Claims It Breached over 300 Websites and Leaked 13,000 People's Details Online.” Business Insider, Business Insider, 1 July 2015, www.businessinsider.com/ghostshell-hackers-hack-300-websites.

W. Zhao and G. White, "A collaborative information sharing framework for Community Cyber Security," 2012 IEEE Conference on Technologies for Homeland Security (HST), Waltham, MA, 2012, pp. 457-462.
DOI: 10.1109/THS.2012.6459892.
