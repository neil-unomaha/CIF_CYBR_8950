# Improving the Collective Intelligence Framework

Talon Flynn  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, tflynn@unomaha.edu  
Amber Makovicka  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, ambermakovicka@unomaha.edu  
Neil Thorne  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States,  nthorne@email.com  
Jackson Urrutia  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Department of Cybersecurity, University of Nebraska at Omaha, Omaha, Nebraska, United States, jurrutia@unomaha.edu

## Abstract

Malicious cyber-attacks on organizations have increased in frequency. Intrusion detection systems, network monitors, and threat intelligence sharing frameworks have struggled to handle the increased load of information. Timeliness of firewall updates is a crucial issue. Updates are taking hours instead of minutes and can leave the system and individuals vulnerable to attacks. This paper will delve into the effects of threat intelligence sharing timeliness within a university enterprise setting and a development effort focused on the rapid dissemination of threat intelligence to perimeter firewalls. This paper addresses the security efficacy and cost of updating the firewalls in a timely and consistent manner.

### CCS Concepts

Networks → Networks Services → Network Management  
Networks → Networks Services → Network Monitoring  
Security and Privacy → Network Security → Firewalls

### Keywords

Collective Intelligence Framework, Palo Alto, IP Management, Information Sharing, Intrusion Detection System

## 1. Introduction

The Collective Intelligence Framework [1] is a threat intelligence management system that utilizes many sources to collect and maintain a database of known malicious threat information. The sources used to provide threat intelligence information are from participants of the framework, such as universities and other organizations. For example, if one university discovers a malicious attack on their network, they can forward any available information to CIF for other parties. The other parties can use the information for identification, detection, and mitigation. Most commonly, IP address, fully qualified domain names (FQDNs), and URLs are seen to be associated with the malicious activity.

Currently, CIF is set up in a way that the different participants send their collected malicious information once a day to other participating parties. Although to some this may seem sufficient, at least one of the participants of CIF, the University of Nebraska, has expressed the desire to send and receive threat information more than once a day to and from other organizations in CIF. If threat information can be sent multiple times a day, potential attacks or threats could be mitigated if the organizations' networks could be made aware of them quickly and blocked within an acceptable time window.

Within this research paper, we will aim to answer the questions: to what extent does the timeliness of threat intelligence gathering, aggregation, and sharing affect risk profile reduction within a university enterprise setting? If there are security efficacy outcomes, what are the costs?

The rest of the paper will be organized as follows. Section 2 will introduce previous work that is relevant to this research paper. Section 3 describes CIF in better detail so that the reader may better understand the framework. Section 4 will be the setup and project methodology of our research and project. Section 5 describes what results and findings were made as a result of the research and project. Finally, section 6 will conclude the paper and give recommendations for further research.

## 2. Background Research

* Background/Literature Review
  * Cyber Crime effects
    * 90% of organization have increased budgets [2]
    * Ransomware attacks, phishing, breaches, etc. are increasing [3]
    * Companies blocking IP addresses by using honeywords, fake passwords entered [4]
    * Other companies sharing intel reports for possible threats [5]
    * Security intelligence and threat sharing have the highest cost savings. 67% of respondents use it, average 2.26 million savings (includes costs of tech) [3]
    * Average cost of successful cyber attack is $1.1 million [6]

Many organizations and researchers have been looking at collective intelligence solutions. With collective intelligence, multiple organizations work in conjunction to collect and share information that could be useful for others. Zhao and White in their paper talk about how collective information sharing can help a community prevent cyberattacks and detect any potential risks in an early stage. They define different types of information sources (internal and external), different methods of communication, etc. The model is very defined with various aspects however the framework is not applied in a test environment for further evaluation [7].

For previous research that pertains to an academic setting, in 2012 there was a large attack from a hacker group, Team GhostShell, that claimed to have attacked over 300 websites and more than 13,000 users' data. The attack reached institutions in areas such as Australia and Korean music services [8].

Another paper from the author Hiroki Hashiwazaki goes into detail in his report about an unnamed Japanese university that had a large-scale leak due to unauthorized access to Office365. Over 24,000 students, 23,000 alumni, 12,000 staff members, etc. had their information leaked. This information included their name, affiliation, email, Student ID, and others. Other information leaked was internal spreadsheets and job applicants who applied to the university. The university learned a hard lesson and in its cleanup implemented new preventative measures, such as next-generation endpoint security solutions, increase log generation from systems and network equipment, and testing for a new vulnerability scanner [9].

To prevent this type of information leakage, along with many other types of vulnerabilities from being exploited, firewalls are some of the best types of components that can be added to a system.  In order to prevent unauthorized outside access to a network, firewalls block malicious IP addresses.  For firewalls to be effective the IP definitions need to be updated constantly to have the most accurate threat information available.  Many firewalls can access the threat of incoming IP addresses and block them, but the limitation upon this is that the threat data is localized to each firewall and not across several.  It is often the case that multiple firewalls within the same organization can be combined to share threat data between themselves making the threat blocking potential much greater than any firewall on its own.  Combining threat data across entirely different organizations would allow companies that operate in the same space to block IP addresses more effectively than one organization.  Educational institutions, for example, could expect to face attacks from similar malicious actors. If they shared threat data between each other, all participants colletively could have their threat vectors reduced[..]. Implementing a firewall within a system is fairly easy on a surface level, but for integration within a system, it may become an issue if integration was not a key point in the design of each of the components [..]

Systems are oftentimes not designed to allow multiple systems to be combined, and a custom solution must be created to fit each situation.  One method that is often used is middleware and can be used for almost every application.  Middleware is a custom application running separately from each system and is a link between each, and thus requires the most effort to create and implement.  Instead of middleware, if it is available, the easier solution to integrating systems is an Application Programming Interface.  APIs are an interface that allows for requests to be made and custom responses can be created that would fit to integrate a system [..].  If one component within a system can easily have new APIs added, and if another component such as a firewall were able to make a request of some sort, a new API that can respond to that request makes integrating both systems a simple task.

## 3. CIF Environment

The project was developed by REN-ISAC. For all intents and purposes, CIF is a server that pulls threat feeds from multiple sources and stores them in an internal database. The server then allows authorized clients to pull the threat feeds from said database. It utilizes what are called indicators to represent attributes associated with malicious activity. A few examples of indicators permitted by CIF include IPv4 and IPv6 addresses, email addresses, and URLs. To describe these indicators, tags are used. Tags are used to describe the malicious activity associated with the indicator, such as malware or phishing, and multiple tags can be associated with each indicator. Lastly, CIF uses a four-point scale to give a confidence level to the specified indicator. This is to assure the specified indicator is malicious. On the scale, a 4 represents absolute certainty, and a 0 or 1 may just represent informational data. Clients that are wanting to pull threat data from a CIF server can specify the minimum confidence level for pulling indicators in a threat feed. Figure 1 is a diagram to represent this basic setup. The threat feeds to pull from can be specified in its configuration, and by default will include a few pre-configured sources that can be adjusted. CIF gives users the choice to expose their server to allow clients to pull from it as well.

![Basic setup Diagram](https://raw.githubusercontent.com/neil-unomaha/CIF_CYBR_8950/master/Assets/cif-basic.png)
<br>
Figure 1: Basic Setup

The CIF server itself is built upon Python and requires Python 3.6 or higher. In addition, CIF uses Flask as the web framework along with the Flask-RESTplus extension. For sending information between different devices, CIFv4 requires a token to be used for authorization when requests are made. Before any new implementations from this team, CIF would use a script to run daily to pull and push the latest feeds to and from Palo Alto firewalls, the clients in this case. Typically, these feeds would contain a list of IP addresses for Palo Alto to put on their blocklist. The retrieved feeds are shared feeds from other members of the framework. Figure 2 is a diagram outlining the current setup.

![Existing Setup Diagram](https://raw.githubusercontent.com/neil-unomaha/CIF_CYBR_8950/master/Assets/Existing_Setup.png)
<br>
Figure 2: Existing Setup

As explained earlier, the goal of this project is to implement a new process to replace the daily script to retrieve the latest feeds several times a day. The question did come up about updating the existing script to run several times a day, but it was decided not to go this route. The script works to request the data from CIF's database, but Flask could be used to internally request and send this data. This would be a better implementation than to run a script separate from the Flask framework.

At the start of the project, CIFv4 was still in beta, but it was decided to follow through in testing to have the implementation work on CIFv4. CIFv3 was in the process of getting deprecated at this point as well.

## 4. Methodology

The beginning of the project began with researching the CIF working environment. At the initial start of the project, online resources were used such as Lynda to get familiar with Python and the Flask web framework. Within CIF itself, virtual machines were set up with Ubuntu Server 16.04, and CIFv4 was installed using docker within the setup. This was all done in reference to CIF's Wiki page [10].

Following the setup of the CIF test environment, the next step was to address the project goal: to update feeds multiple times a day rather than once a day. Figure 3 represents the environment the team was working with. Somehow, without using the daily script, the desire was to push and pull feeds between the CIF server's internal database and Palo Alto firewalls.

![Environment](https://raw.githubusercontent.com/neil-unomaha/CIF_CYBR_8950/master/Assets/cif-challenge.png)
<br>
Figure 3: Test Environment

The solution chosen was to use an endpoint built into the CIF software directly for the firewall to invoke. A few restraints in creating this endpoint were quick to present themselves. The preferred solution was to utilize Palo Alto's external blocklist [11], where Palo Alto can request a file of IP addresses to block from a specific URL source. In requesting these files, it was realized per file there was a 5,000 IP limit per external block list, with a maximum of 150,000 IP addresses via the blocklists [12]. This would imply that multiple external blocklist files would have to be sent to Palo Alto if the IP addresses to be blocked exceeded 5,000. In addition, it was mentioned earlier that CIF requires a token in the request header whenever a request is being made. The external block lists are not able to send this token that CIF requires. In the test environment setup, a new endpoint file was created to listen for Palo Alto request feeds. Figure 4 below is a diagram to visually represent this idea. To allow this new endpoint to run in this test environment, it had to be imported, added to the API, and whitelisted in the driver python script, app.py. In the testing and examining logs from the CIF server, we were able to implement a solution to the token issue mentioned before. This endpoint file was named palo.py and placed in the same directory as the app.py file.

![Palo Alto Endpoint Diagram](https://raw.githubusercontent.com/neil-unomaha/CIF_CYBR_8950/master/Assets/cif-api-solution.png)
<br>
Figure 4: Palo Alto Endpoint Implementation

In the process, the Palo Alto endpoint had gone under three revisions.

* The first version essentially used a curl command within the endpoint itself which called another existing endpoint in the CIF environment. The results of the curl command were outputted and formatted into a file following Palo Alto's constraints to be sent. However, there were two issues identified with this solution. It was that it was inefficient and it made an unnecessary dependency for the Palo Alto endpoint.

* The second version removed the curl implementation and instead queried the database directly using an existing object-relational mapper. It was an immense improvement, but some vulnerabilities in this implementation existed. For both the first and second versions, they outputted results to a file and when sent, caused the server to crash. Also, this implementation was still inefficient.

* Version three was built upon version two and implemented a few improvements. The output of the database query was not written to a file but wrote into a file in memory via the python module. The other major change was regarding a passed parameter. It was found to be better designed to pass a page number as an actual parameter (i.e. `/?page_num=1`) as opposed to using a variable rule to represent it (i.e. `/1`). The variable rule was not as self-explanatory as passing in a page number as a parameter.

Following the development of version three and labeling it as being in a satisfactory state, the stakeholder was informed of this solution. The next step in this project was to ask of the stakeholder to collect metric data of the CIF environment before any implementing this new endpoint. Following, it was asked of them to also follow the setup walkthrough guide the team had generated in setting up this new CIF test environment with the new Palo Alto endpoint. The aim was to collect new metric data following the new endpoint's implementation and compare the results.

## 5. Metric Analysis

The team was able to communicate with the stakeholder of the project and retrieve reports from their existing Palo Alto Firewall and CIF setup. The report contained traffic for a 2.5-hour timeframe. The team also got ahold of a report of the previous day's newly added blocked IPs from CIF. A filter was then applied to the 2.5-hour network traffic data to identify when each indicator was first seen. To simulate a 15-minute blocking strategy, all times those indicators were seen 15-minutes after their first siting was considered "blocked".

There were 59 unique IP addresses that were added from the previous day's CIF server.  Out of those 59 indicators, 44 indicators were observed within the 2.5-hour sample of network traffic, and those 44 indicators were observed in 162 total packets within that network traffic sample. Our analysis found that if Palo Alto was implementing a 15-minute blocking strategy instead of a daily blocking strategy, 93 of the 162 malicious packets would have been dropped.  In other words: 57% of the known 162 malicious packets would have been dropped with a 15-minute strategy.

It should be noted that the data utilized for our analysis is a limited view of the network traffic, so it is important to be careful about generalizing this finding. Malicious traffic can vary on a day-by-day basis, and our 2.5-hour sample of network traffic is not representative of all network traffic within UNL.

## 6. Conclusion

The need for cyber security is a problem that will become only more necessary. Annually, cyber-attacks can cause damage and cost businesses millions of dollars. To combat attacks, many have implemented technologies such as intrusion detection systems, network monitors, and firewalls. This paper focused on tools used to better implement firewalls in a university setting. The tool was a threat intelligence sharing framework where participants can share their threat data among others within the framework. It has been shown using this type of threat intelligence sharing can benefit all members of the community to help reduce malicious threat traffic. At the beginning of this project, the shared threat feeds are only shared once a day with other members. This project's aimed to introduce new technology into the existing framework to have threat feeds be shared multiple times a day. This was to better make use of the shared data and to have it shared in a more timely manner.

As a result of this project, the team was able to create a new endpoint within the existing CIF infrastructure. It was designed to assist Palo Alto firewalls when requesting the latest threat feeds and returning them in an ingestible format. The endpoint within the CIF server can listen to requests for the latest threat feeds. The metric analysis was performed on a 2.5-hour packet capture without the endpoint implementation. After manual analysis, it was found within the packet capture, the endpoint could help eliminate 50-60% of malicious traffic over the network. It is believed this number could vary if the analysis was performed on a 24-hour packet capture or a 7-day packet capture.

For further research, it has been advised to implement the endpoint is a larger test environment to test for any bugs or issues in addition to its effectiveness.

## References

[1] Csirtgadgets. 2015. csirtgadgets/massive-octo-spice. (February 2015). Retrieved May 4, 2020 from https://github.com/csirtgadgets/massive-octo-spice/wiki/What-is-the-Collective-Intelligence-Framework%3F  
[2] Kelly Bissell, Ryan M. Lasalle, Floris Van Den Dool, and Josh Kennedy-White. 2018. Gaining ground on the cyber attacker. (April 2018). Retrieved May 4, 2020 from https://www.accenture.com/in-en/insights/security/2018-state-of-cyber-resilience-index  
[3] Kelly Bissell, Ryan M. Lasalle, and Paolo Dal Cin. 2019. Ninth Annual Cost of Cybercrime Study. (March 2019). Retrieved May 4, 2020 from https://www.accenture.com/us-en/insights/security/cost-cybercrime-study  
[4] Komal Naik, Varsha Bhosale, and Vinayak Shinde. 2017. Detection of Intruder using Honeywords and IP Blocking. (March 2017). Retrieved May 3, 2020 from https://www.bvicam.ac.in/news/INDIACom 2017 Proceedings/Main/papers/803.pdf  
[5] Jamal Elmellas. 2016. Knowledge is power: the evolution of threat intelligence. (July 2016). Retrieved May 4, 2020 from https://www.sciencedirect.com/science/article/pii/S1361372316300513  
[6] Radware. The Trust Factor: Cybersecurity's Role in Sustaining Business Momentum. Retrieved May 4, 2020 from http://www.radware.com/ert-report-2018/  
[7] Wanying Zhao and Gregory White. 2013. A collaborative information sharing framework for Community Cyber Security. (February 2013). Retrieved May 4, 2020 from https://ieeexplore.ieee.org/document/6459892  
[8] Alastair Stevenson. 2015. A hacker group claims it breached over 300 websites and leaked 13,000 people's details online. (July 2015). Retrieved May 4, 2020 from http://www.businessinsider.com/ghostshell-hackers-hack-300-websites  
[9] Hiroki Kashiwazaki. 2018. Personal Information Leak in a University, and Its Cleanup. In Proceedings of the 2018 ACM SIGUCCS Annual Conference (SIGUCCS ’18). Association for Computing Machinery, New York, NY, USA, 43–50. DOI:https://doi.org/10.1145/3235715.3235727  
[10] Csirtgadgets. 2018. csirtgadgets/massive-octo-spice. (January 2018). Retrieved May 4, 2020 from https://github.com/csirtgadgets/massive-octo-spice/wiki  
[11] Palo Alto. Use an External Dynamic List in Policy. Retrieved May 4, 2020 from https://docs.paloaltonetworks.com/pan-os/8-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy  
[12] Palo Alto. 2019. DotW: Dynamic Block List - Limited Number of Entries? (July 2019). Retrieved May 4, 2020 from https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClS7CAK
