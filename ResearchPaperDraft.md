# Title in progress
### Subtitle here

Talon Flynn  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, tflynn@unomaha.edu  
Amber Makovicka  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, ambermakovicka@unomaha.edu  
Neil Thorne  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States,  email@email.com  
Jackson Urrutia  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, email@email.com

## Abstract

Malicious cyber-attacks on organizations have increased in frequency. Intrusion detection systems, network monitors, and threat intelligence sharing frameworks have struggled to handle the increased load of information. Timeliness of firewall updates is a crucial issue. Updates are taking hours instead of minutes and can leave the system and individuals vulnerable to attacks. This paper will delve into the effects of threat intelligence sharing timeliness with a university enterprise setting and a development effort focused on the rapid dissemination of threat intelligence to perimeter firewalls. This paper addresses the security efficacy and cost of updating the firewalls in a timely and consistent manner.

### CCS Concepts
*insert ACM Computing Classification System using indexing support tool*

### Keywords
*Collective Intelligence Framework, Palo Alto, IP Management, Information Sharing, Intrusion Detection System*

## 1. Introduction

The Collective Intelligence Framework (https://github.com/csirtgadgets/massive-octo-spice/wiki/What-is-the-Collective-Intelligence-Framework%3F) is a threat intelligence management system that utilizes many sources to collect and maintain a database of known malicious threat information. The sources used to provide threat intelligence information are from participants of the framework, such as universities and other organizations. For example, if one university discovers a malicious attack on their network, they can forward any available information to CIF for other parties. The other parties can use the information for identification, detection, and mitigation. Most commonly, IP address, fully qualified domain names (FQDNs), URLs are seen to be associated with the malicious activity.

Currently, CIF is setup in a way that the different participants send their collected malicious information once a day to other participating parties. Although to some this may seem sufficient, at least one of the participants of CIF, the University of Nebraska, has expressed the desire to send and receive threat information more than once a day to and from other organizations in CIF. If threat information can be sent multiple times a day, potential attacks or threats could be mitigated if the organizations' networks could be made aware of them quickly and blocked within an acceptable time window.

Within this research paper, we will aim to answer the questions: to what extent does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting? If there are security efficacy outcomes, what are the costs?

The rest of the paper will be organized as follows. Section 2 will introduce previous work that is relevant to this research paper. Section 3 describes CIF in better detail so that the reader may better understand the framework. Section 4 will be the setup and project methodology of our research and project. Section 5 describes what results and findings were made as a result of the research and project. Finally, section 6 will conclude the paper and give recommendations on further research.

## 2. Background Research

* Background/Literature Review
  * Cyber Crime effects
    * 90% of organization have increased budgets (Bissell, et. al, 2018)
    * Ransomware attacks, phishing, breaches, etc. are increasing (Bissell, et. al, 2019)
    * Companies blocking IP addresses by using honeywords, fake passwords entered (K. Naik, V. Bhosale, and V. D. Shinde)
    * Other companies sharing intel reports for possible threats (J. Elmellas, “Knowledge is power: the evolution of threat intelligence”)
    * Security intelligence and threat sharing has the highest cost savings. 67% respondents use it, average 2.26 million savings (includes costs of tech) (Bissell, et al. 2019)
    * Average cost of successful cyber attack is $1.1 million (Radware, 2018)

Many organizations and researchers have been looking at collective intelligence solutions. With collective intelligence, multiple organizations work in conjunction to collect and sharing information that could be useful for others. Zhao and White in their paper talk about how collective information sharing can help a community prevent cyber attacks and detect any potential risks in an early stage. They define different types of information sources (internal and external), different methods of communication, etc. The model is very defined with various aspects however the framework is not applied in a test environment for further evaluation (2012).

For previous research that pertains to an academic setting, in 2012 there was a large attack from a hacker group, Team GhostShell, that claimed to have attacked over 300 websites and more than 13,000 users' data. The attack reached institutions in areas such as Australia and Korean music services (Stevenson, 2015).

Another paper from the author Hiroki Hashiwazaki goes into detail in his report about an unnamed Japanese university that had a large-scale leak due to unauthorized access to Office365. Over 24,000 students, 23,000 alumni, 12,000 staff members, etc. had their information leaked. This information included their name, affiliation, email, Student ID, and others. Other information leaked was internal spreadsheets and job applicants who applied at the university. The university learned a hard lesson and in its cleanup implemented new preventative measures, such as next generation endpoint security solutions, increase log generation from systems and network equipment, and testing for a new vulnerability scanner (Kashiwazaki, 2018).

## 3. CIF Information

The project is built upon Python, and the system it is installed on must be Python 3.6 or higher. CIF also uses Flask as the web framework. Before this project, CIF would use a script to run on a daily basis to pull and push the latest feeds to and from Palo Alto firewalls. The retrieved feeds are shared feeds from other members of the framework. Figure 1 is a diagram outlining the current setup.

![Existing Setup Diagram](https://raw.githubusercontent.com/neil-unomaha/CIF_CYBR_8950/master/Assets/Existing_Setup.png)
<br>
Figure 1: Existing Setup

As explained earlier, the goal of this project is to implement a new process to replace the daily script to retrieve the latest feeds several times a day. The question did come up about updating the existing script to run several times a day, but it was decided not to go this route. The script works to request the data from CIF's database, but Flask could be used to internally request and send this data. This would be a better implementation than to run a script separate from the Flask framework.

At the start of the project, CIFv4 was still in beta, but it was decided to follow through in testing to have the implementation work on CIFv4. CIFv3 was in the process of getting deprecated at this point as well.

## 4. Methodology

The beginning of the project begun with conducting research about the CIF working environment. CIF is built upon the Flask framework and requires at least Python version 3.6. At the initial start of the project, we used online resources such as Lynda to get familiar with Python and the Flask web framework. Within CIF itself, virtual machines were set up with Ubuntu Server 16.04 and CIFv4 was installed using docker within the setup. ***(reference CIF installation walkthorugh?)***

Following the setup of the CIF test environment, progress for realizing the project goal: to update feeds multiple times a day rather than once a day. To realize this goal, a plug-in was added to the existing CIF software. This plug-in was designed to listen for database update requests from Palo Alto, and in response, pull up-to-date data from the CIF database and return the data. The data returned would have to be formatted in such a way that Palo Alto could digest it. In addition, it was documented that Palo Alto receives at most 5,000 IP addresses to block at one time. The hardware that was being used in this environment can block up to 150,000 IP addresses, but the feed information from the database to be sent to Palo Alto must be partitioned into files of no more than 5,000 IP addresses per file.

***Not sure about this paragraph since we just did the plug-in?*** *Another goal for the project was to have the CIF server at the University of Nebraska to request updated information from other participating members of CIF in 15 minute intervals. Once received, the information retrieved would be put into the CIF database.*

In developing a solution, a new endpoint file was created in the CIF environment for listening to Palo Alto feed requests. The endpoint requires a page number to specify which block of 5,000 IP addresses to send. In addition, to allow this new endpoint to interact as expected in the test environment, it must be imported, added in the API, and whitelisted in the driver python script, app.py. ***Can someone more familiar with palo.py add in details of the endpoint here in terms of testing it in the CIF test environment***

Following testing of the palo.py file and verifying it works as expected, the next step was to collect metrics within an active CIF environment.

## 5. Results/Findings

The results were compiled from Palo Alto Firewall. It will be a 1-day traffic capture that will have all the threat alerts captured for the day as well. A filter will be applied to these results that identify when the threat first is seen and then 15 minutes later all traffic from that threat will be removed for the rest of the day. This will simulate the CIF palo.py actually running and doing what it was designed for. After all the filters are applied this should simulate a day of traffic while the palo.py is running. This will show an accurate layout of what will happen. Since before and after would show different possible traffic and possible threats because every day is different.

    * Collect metrics from CIF about IPs that were blocked on just a day-to-day basis
    * Collect metrics from CIF about IPs that were blocked every 15 minutes (as often as Palo Alto should request updated information)
    * Compare findings and summarize differences found between the metrics
  * MORE INFORMATION PENDING

## 6. Conclusion and further research considerations

  * Summarize findings, metrics, lessons learned, etc.
  * Submit pull request for CIFv4
  * Areas for further research

## References

[1] Reference  
[2] Reference
