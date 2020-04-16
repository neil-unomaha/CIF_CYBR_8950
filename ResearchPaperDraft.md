# Title in progress
### Subtitle here

Talon Flynn  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, tflynn@unomaha.edu  
Amber Makovicka  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First Department Name, First Institution/University Name, City, State, Country, email@email.com  
Neil Thorne  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First Department Name, First Institution/University Name, City, State, Country, email@email.com  
Jackson Urrutia  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First Department Name, First Institution/University Name, City, State, Country, email@email.com

## Abstract
Malicious cyber-attacks on organizations have increased in frequency. Intrusion detection systems, network monitors, and threat intelligence sharing frameworks have struggled to handle the increased load of information. Timeliness of firewall updates is a crucial issue. Updates are taking hours instead of minutes and can leave the system and individuals vulnerable to attacks. This paper will delve into the effects of threat intelligence sharing timeliness with a university enterprise setting and a development effort focused on the rapid dissemination of threat intelligence to perimeter firewalls. This paper addresses the security efficacy and cost of updating the firewalls in a timely and consistent manner.

### CCS Concepts
*insert ACM Computing Classification System using indexing support tool*

### Keywords
*Collective Intelligence Framework, Palo Alto, IP Management, Information Sharing, Intrusion Detection System*

## 1. Introduction

The Collective Intelligence Framework (https://github.com/csirtgadgets/massive-octo-spice/wiki/What-is-the-Collective-Intelligence-Framework%3F) is a threat intelligence management system that utilizes many sources to collect and maintain a database of known malicious threat information. The sources used to provide threat intelligence information are from participants of the framework, such as universities and other organizations. For example, if one university discovers a malicious attack on their network, they can forward any available information to CIF for other parties. The other parties can use the information for identification, detection, and mitigation. Most commonly, IP address, fully qualified domain names (FQDNs), URLs are seen to be associated with the malicious activity.

Currently, CIF is setup in a way that the different participants send their collected malicious information once a day to other participating parties. Although to some this may seem sufficient, at least one of the participants of CIF, the University of Nebraska, has expressed the desire to send and receive threat information more than once a day to and from other organizations in CIF. If threat information can be sent multiple times a day, potential attacks or threats could be mitigated if the organizations' networks could be made aware of them quickly and blocked within an acceptable time window.

Within this research paper, we will aim to answer the questions: to what extend does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting? If there are security efficacy outcomes, what are the costs?

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

## 4. Methodology
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

## 5. Results/Findings
  * Metric Analysis

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
