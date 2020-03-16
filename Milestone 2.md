# Milestone 2

## Environment Setup and Hardships

## CIF Installation and Commands Notes

### Installation

The installation notes specifically for the [Docker installation strategy](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton) worked very well for me.  I will provide a few pointers I gathered along the way

*  I did **first** have to create an account on Maxmind.

```
## MAXMIND Credentials
username: nthorne@unomaha.edu
Account_user ID: *****
License Key: *****
```

* Install on `Ubuntu 16.04 Server` (example: Ubuntu 16.04 Desktop doesn't work)
* Install the docker image via `docker pull csirtgadgets/verbose-robot`
* As indicated in the instructions, either `export` your Maxmind credientals, or (as I did) put them in your `.bashrc` file and `source` it
* Run your docker container:

```
sudo docker run -e CIF_TOKEN="${CIF_TOKEN}" -e MAXMIND_USER_ID="${MAXMIND_USER_ID}" -e MAXMIND_LICENSE_KEY="${MAXMIND_LICENSE_KEY}" -it -p 5000:5000 -d --name verbose-robot csirtgadgets/verbose-robot:latest
```

* Remember that `CIF 4` is running in a docker container.  You still need to shell into the container in order to install additional software.  
  * Shell into your running container via:

```
  sudo docker exec -it verbose-robot /bin/bash
```

* Now that you are at a command prompt inside the container, [as indicated here](https://github.com/csirtgadgets/verbose-robot/wiki/Where-do-I-start) install the CIF client via:  `pip install 'cifsdk>=4.0.0a0'`

Now that you have the  Python CIF SDK installed, you should be good to go!  Be sure that all your CIF commands are run within the docker container.

### Usage / Commands

* The main command is `cif`.  The client specifies a number of different options and arguments in order to get the desired response.  [Good Examples Here](https://github.com/csirtgadgets/verbose-robot/wiki/Introducing-the-CIF-client).
* The process of ingesting threats/sharing threats within a network is unclear to me via the documentation
* Appending to CIF threats is also unclear to me via the documentation.
* The provided examples don't work because they are missing required options (apparently you must provide `--tags` now

```
cif --itype ipv4 --tags phishing --format table
```

The `--feed` option as [specified here is unrecognized](https://github.com/csirtgadgets/verbose-robot/wiki/Where-do-I-start-Feeds).  Apparently that is how you pull data from feeds in CIF?

-----

## Setup CIF 4 Test Environment

The following example shows how to setup a CIF test environment with Ubuntu 16.04 server running in a virtual machine

### Installation

#### Install Ubuntu 16.04 server

First you will need to download an [Ubuntu 16.04 server image](http://releases.ubuntu.com/16.04/) and create a virtual machine.  

Once you startup your virtual machine and login, there are a couple more steps for our guide.  We wanted a GUI, so we installed the ubuntu-desktop extension:

`sudo apt-get update`  
`sudo apt-get install ubuntu-desktop`

#### Install Docker

Next you need to install docker:

`sudo apt install docker.io`

#### Install CIF4 Docker Image

Install the CIF 4 container from docker hub

`sudo docker pull csirtgadgets/verbose-robot`

### Setup Prior to running Docker Container

Before running the docker container, you need to create some environment variables.

The first is `CIF_TOKEN` which will contain a randomly generated string.  This string ultimately becomes the bearer token passed into for all of your `GET` and `POST` requests via the request header for security. You can generate a random string with the following command on Ubuntu:

`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'`

An example ouptut string is the following:

`525ff70def1b2b4eff3119451eabfa0ce3fa6316efb55fda075db08ac4a2feda`

The other two required environment variables are `MAXMIND_USER_ID` AND `MAXMIND_LICENSE_KEY`.  CIF depends on [as mentioned here](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton). Head over to [Maxmind](https://www.maxmind.com/en/home), create a free account, and within the settings you can find your account id and license key.

![maxmind_key](https://user-images.githubusercontent.com/38234505/75952477-74fa4f00-5e74-11ea-8ace-ab3a8f594e15.PNG)


Here is an example command to setup these environment variables.  Note that you'll want to swap out the values for `MAXMIND_USER_ID` and `MAXMIND_LICENSE_KEY`

Setup those environment variables.

```
export CIF_TOKEN=`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'
export MAXMIND_USER_ID=201001
export MAXMIND_LICENSE_KEY=3r8ESHRiFIsF
```

### Run CIF Container

With the environment variables all setup, you can now run your CIF docker image:

```
sudo docker run -e CIF_TOKEN="${CIF_TOKEN}" -e MAXMIND_USER_ID="${MAXMIND_USER_ID}" -e MAXMIND_LICENSE_KEY="${MAXMIND_LICENSE_KEY}" -it -p 5000:5000 -d --name verbose-robot csirtgadgets/verbose-robot:latest
```

* We pass into the running docker container the three environment variables we specified above with the `-e` flag
* We setup port forwarding on port 5000 with the `-p` flag
* We run the docker container in a  daemon with `-d`
* For ease of referencing our docker container in the future, we labeled the container `verbose-robot`

To confirm our docker container is running, we can run `sudo docker ps`

### Execute CIF Commands

In order to interact with CIF, we can do so in two ways: the command prompt or with Swagger.

#### Command Prompt

To do this we need to `bash` into our running container.  We can do that with the following:

`sudo docker exec -it verbose-robot /bin/bash`

Now that we are inside the container, we can execute the `cif` command with various options in order to query the CIF database.  Here are some example commands:

`cif --itype ipv4 --tags scanner`  
`cif --itype url --tags phishing`  
`cif --itype url --tags malware`  
`cif --itype ipv4 --tags botnet`  

![example_output](https://user-images.githubusercontent.com/38234505/75954931-70389980-5e7a-11ea-978a-03042c36aef5.PNG)

Note that by default, CIF is pulling feeds from providers you specified every three minutes.  

#### Swagger

On the VM running CIF you can visit http://localhost:5000 which displays a rest api gui.

![swagger](https://user-images.githubusercontent.com/38234505/75951890-cb668e00-5e72-11ea-9d7d-0d9364429e6c.PNG)

It is important to note that the lock symbol next to each endpoint indicates that the a token is required to be passed in for each request.  This is the string that we created and stored within the `CIF_TOKEN` environment variable earlier.  Click the **Authorize** button and add the token.

Once you add the token, you should be able to interact with the api in the GUI.  click the **Try it Out** button which toggles the endpoint, then click **Execute**.

![execute_swagger](https://user-images.githubusercontent.com/38234505/75952373-29e03c00-5e74-11ea-88e8-4272a9dc2bf8.PNG)

You can then scroll down to see the response:

![swagger_response](https://user-images.githubusercontent.com/38234505/75952410-4a0ffb00-5e74-11ea-9208-89ef01f53014.PNG)

### Create Endpoints

The CIF file that specifies endpoints is in `app.py`.  We think, in this docker container, the specific file is located here:

`/usr/local/lib/python3.6/site-packages/verbose_robot-4.0.1-py3.6.egg/cif/httpd/app.py`

Adding an endpoint should be as simple as the following:
```
@app.route('/')
  def hello_world():
    return 'Hello, World!'
```

Restart the server and try it out. Initial attempts did not work.

One possible explanation is becuase CIF is using [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html#), so the config might actually be this:
```
@api.route('/hello')
  class HelloWorld(Resource):
  def get(self):
    return {'hello': 'world'}
```

We will have to try this.

-----

## Roadblocks:

### Getting CIF4 Environment Setup and Familiarizing ourselves with How it Works

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
  *  [Step to install the CIF CLI/Client inside the container](https://github.com/csirtgadgets/verbose-robot/wiki/Where-do-I-start) appears to be unnecessary because the image already contains it, but ran the command anyways just in case: `pip install 'cifsdk>=4.0.0a0'`
* Specify queries against the CIF server

#### Issues Encountered

* Documentation contains gaps in explanations (implication that reader already has significant familiarity with the topic and related technology).
* Majority of [code examples specified in documentation](https://github.com/csirtgadgets/verbose-robot/wiki/Introducing-the-CIF-client) do not work as specified.  Almost always require additional options
* It appears we can successfully query `CIF` right now, but the issue is that in our test environment: there are no existing feeds, so it doesn't return anything.
  * Example: `cif --itype ipv4 --tags malware`
![example](https://user-images.githubusercontent.com/38234505/74463773-f4899500-4e57-11ea-9c73-cdd43b43e466.PNG)

#### Questions to be Answered

**- Is CIF currently pulling feeds in real time, Or is pulling from feeds disabled by default?  If it is disabled, how do we enable it?**
  * It appears like the [Rules Directory](https://github.com/csirtgadgets/verbose-robot/tree/master/rules) is where the feeds are specified

**- How do we add additional feeds?**

#### Currently Known CIF Resources/Tutorials/Documentation

* [CIF4 Server Code](https://github.com/csirtgadgets/verbose-robot)
* [CIF4 CLI Client in Python](https://github.com/csirtgadgets/cifsdk-py-v4)
* [CIF4 CLI Client in Go](https://github.com/JustinAzoff/cifsdk-go)
* [CIF4 Wiki](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book)
* [CIF3 Wiki](https://github.com/csirtgadgets/bearded-avenger-deploymentkit/wiki/The-CIFv3-Book)
* [CIF Maintainer's Blog](https://csirtgadgets.com/collective-intelligence-framework)
  * Wes Young (appears to be the creator behind CIF4)
  * Posts are not tutorials, mostly like journal entries/reflection on topics such as threat intelligence and writing open source code.  
  * [Payment required to answer questions surrounding CIF](https://csirtg.io/support)
* [Presentation on CIF](https://www.youtube.com/watch?v=wrfMnGyQIU8)
  * Video discussing version 2 of CIF, provides a good overview of CIF, but beyond an introduction to CIF, the processes/procedures mentioned are outdated.

#### Forcasted Obstacles

* Our middleware will need to be in an environment where it has the necessary privileges to talk to both the Palo Alto API, and to access the CIF CLI
  *  We will need to work closely with Brian in order to make sure that this environment exists, or we will need to work together in order to create this environment.

-----

## Project Realization

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
  * Rest of paper will flow as...
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
    * Security intelligence and threat sharing has the highest cost savings. 67% respondents use it, average 2.26 million savings (includes costs of tech) (Bissell, et al. 2020)
    * Average cost of successful cyber attack is $1.1 million (Radware, 2018)
    * Equifax hack as so far cost $439 million, and projected to exceed $600 million
  * Collective Intelligence
    * Describe the goals
      * Multiple organizations collecting and sharing information could benefit all members better than individually
    * Zhao and White try to define and create a baseline for a collaborative intelligence framework in their paper, based of the g-SIS model (2012)
  * University setting relevant to CIF project
    * In 2012, there was a GhostShell hack that attacked educational institutions from Australia to Korean music services. It caused the release of 13,000 users' personal details online (Stevenson, 2015).
    * Unnamed university in Japan announced a large-scale personal leak, caused by unauthorized access to Office365 (Kashiwazaki, 2018).
      * 24,000+ students, 23,000+ alumni, 12,451 members of staff, etc. laked information
        * Included name, affiliation, Email. For students, it also included year of entrance and student ID
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
        * Current cron job works in roundabout way
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
    * CIF server should request updated information from other universities every 15 minutes, and put any retrieved information into database in a Palo Alto ingestible file format

  * Developing and Testing
    * Implement goals mentioned previously into python script in CIFv4 environment
      * Document small fixes, issues, challenges, etc. we had to do for the script
    * Document testing done
      * Add python script to the existing CIF environment, and record if it is listening to Palo Alto and sending expected text file
    * Collect metric information about IP indicators being collected to block within the 15 minute intervals

* Results/Findings
  * Metric Analysis

    * Collect metrics from CIF about IPs that were blocked on just a day-to-day basis
    * Collect metrics from CIF about IPs that were blocked every 15 minutes (as often as Palo Alto should request updated information)
    * Compare findings and summarize differences found between the metrics
  * MORE INFORMATION PENDING

* Conclusion and further research considerations

  * Summarize findings, metrics, lessons learned, etc.
  * Submit pull request for CIFv4
  * Areas for further research

-----

## Research Abstract

Recently, due to the amount of intelligence being collected by intrusion detection systems, network monitoring software and intelligence sharing the amount of data being brought into organizations are constantly growing. This creates a new problem for an organization to address, to what extent does the timeliness of the threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting? If there are security efficacy outcomes, what are the costs? This paper aims to show a possible solution to the timeliness of blocking intelligence of malicious IP addresses that are flagged. This is accomplished by using CIF (Collective Intelligence Framework) with Palo Alto Firewalls. CIF is used to pull threat feeds and use these feeds to update Palo Alto Firewall with new malicious IP blocks promptly. By doing this CIF shortens the time between first threat indication and block time to reduce the possible attack timeframe from a potential malicious threat.

-----

## Visuals and Diagrams

### Current CIF Infrastructure

### Goal CIF Infrastructure

![Diagram](https://user-images.githubusercontent.com/46516728/75945728-ad902d80-5e60-11ea-8fd1-db981db1027c.png)

-----

## References

J. Elmellas, “Knowledge is power: the evolution of threat intelligence” ScienceDirect, pp. 1–5, Jul. 2016.

K. Naik, V. Bhosale, and V. D. Shinde, “Detection of Intruder using Honeywords and IP Blocking,” International Conference on “Computing for Sustainable Global Development,” vol. 4th, pp. 1819–1822, Mar. 2017.

Kashiwazaki, Hiroki. “Personal Information Leak in a University, and Its Cleanup.” ACM Digital LIbrary, Proceedings of the 2018 ACM SIGUCCS Annual Conference (SIGUCCS ’18), Sept. 2018, dl-acm-org.leo.lib.unomaha.edu/doi/abs/10.1145/3235715.3235727.

Kelly Bissell, Ryan Lasalle, Floris Van Den Dool, and Josh Kennedy-White. 2018. Gaining Ground on the Cyber Attacker: 2018 State of Cyber Resilence. (April 2018). Retrieved February 23, 2020 from https://www.accenture.com/in-en/insights/security/2018-state-of-cyber-resilience-index

Kelly Bissell, Ryan M. Lasalle, and Paolo Dal Cin. 2019. Ninth Annual Cost of Cybercrime Study. (March 2019). Retrieved February 23, 2020 from https://www.accenture.com/us-en/insights/security/cost-cybercrime-study

Radware. “The Trust Factor.” Radware, www.radware.com/ert-report-2018/.

Stevenson, Alastair. “A Hacker Group Claims It Breached over 300 Websites and Leaked 13,000 People's Details Online.” Business Insider, Business Insider, 1 July 2015, www.businessinsider.com/ghostshell-hackers-hack-300-websites.

W. Zhao and G. White, "A collaborative information sharing framework for Community Cyber Security," 2012 IEEE Conference on Technologies for Homeland Security (HST), Waltham, MA, 2012, pp. 457-462.
doi: 10.1109/THS.2012.6459892.
