# Literature and Research Material

### Process Automation Articles

J. K. Visser and H. T. Malan, “Identification of risk associated with process automation systems,” Int. J. Econ. Manag. Eng, vol. 13, no. 7, pp. 1044–1051, 2019. \
Keywords - Process Automation, Risk, System Performance, Third-Party Communication, Interface Compatibility \
(Add Paragraph with info)
URL - https://pdfs.semanticscholar.org/b845/bde145526fb9fff7517161337533982defc9.pdf \

### API Integration / Middleware for Connecting APIs

S. Chang-Woo, L. Daesung, C. Kyung-Yong, R. Kee-Wook, and L. Jung-Hyun, “Interactive middleware architecture for lifelog based context awareness,” Multimedia Tools and Applications, vol. 71, Jan. 2013. \
Keyword - Middleware, Centralized Storage, DBMS, Multiple Middleware, Mobile Devices, Logs \
(Add Paragraph with info)
URL - https://link.springer.com/article/10.1007/s11042-013-1362-7 \

### Systems Architecture Integration

R. T. Tiburski, L. A. Amaral, E. D. Matos, and F. Hessel, “The importance of a standard security architecture for SOA-based IoT middleware,” Institute of Electrical and Electronics Engineers, vol. 53, no. 12, pp. 20–26, Dec. 2015. \
Keyword – IoT, System Architecture, Middleware, Security, Standard Architecture \
(Add Paragraph with info)
URL: https://www.researchgate.net/publication/290378256_The_Importance_of_a_Standard_Security_Architecture_for_SOA-based_IoT_Middleware \

### Web Services Literature

E. B. Fernandez, N. Yoshioka, and H. Washizaki, “Patterns For Cloud Firewalls” AsianPLoP (pattern languages of programs), pp. 1–11. \
Keyword - Firewalls, Security patterns, Network security, Cloud Computing, Services \
This paper gives a generalized view of different firewall configurations for single businesses and multiple businesses. They discuss how one firewall can filter traffic to one customer differently than it filters to another customer. By setting group rules for any traffic going to certain IP ranges or domains. They talk about in detail about cloud-based firewalls like amazon uses their firewalls and how they are configured. It gives a nice explanation of the configuration and how every business is a little different. The paper also talks about having multiple firewalls and each one does something different. Some firewalls only do security groups while others are for whitelisting. It gives detail on why the configuration is made like this and have a lot of good images to visualize this. \
URL - https://www.researchgate.net/publication/266385038_Patterns_for_cloud_firewalls \

-----

keywords: {application program interfaces;financial data processing;Internet;service-oriented architecture;Web APIs;Adyen's payment service;API consumer applications;API related problems;API integration;invalid request data;large-scale payment company;service-oriented architectures;API error responses;Stakeholders;Production;Fault diagnosis;Companies;Complexity theory;Servers;web engineering;web API integration;webservices},
1.	Problem Statement
As Web APIs grow in complexity, so too does quantity and type of errors. At the time of this publication, no large scale evaluation has been conducted that identies and classifies all types of API errors that can happen.
2.	Research Question(s)
    - What types of faults are impacting API consumers?
    - What is the prevalence of these fault types, and how many API consumers are impacted by them?
    - What are the current practices and challenges to avoid and reduce the impact of problems caused by faultus in API integration?
3.	Contribution:
  * Classification of API faults
    - invalid user input
    - missing user input
    - expired request data
    - invalid request data
    - missing request data
    - insufficient permissions
    - double processing
    - configuration
    - missing server data
    - internal and third party
  * Recommendations for API providers and API consumers to reduce faults
4.	Rationale
By identifying beforehand all possible API errors a user might run into, it can facilitate good documentation and help developers develop good API design which helps prevent errors from occurring.
5.	Investigative Approach:
  * Evaluated error responses to a large scale webserve (Adyen webservices)
  * Evaluated 2.43 million error responses from the logs
  * Surveyed API consumers
6.	Lessons Learned:
  * Most faults are caused by the following:
    - invalid request data (received input that cannot be handled)
    - missing request data (consumer fails to send needed info required for action)
    - double processing (send same request to delete the same resource twice: second request produces a fault because the resource no longer exists)
  * Faults caused by the API provider and third parties are must impactful (those originating by end user: not so much)
    - API documentation is critical, followed by code examples
    - Provide common implementation scenarios (instead of merely stating the different options of the API calls)
    - Identify the most common API mistakes, and how to prevent them
    - Details on error codes
    
J. Aué, M. Aniche, M. Lobbezoo and A. van Deursen, "An Exploratory Study on Faults inWeb API Integration in a Large-Scale Payment Company," 2018 IEEE/ACM 40th International Conference on Software Engineering: Software Engineering in Practice Track (ICSE-SEIP), Gothenburg, 2018, pp. 13-22. URL: http://ieeexplore.ieee.org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=8449231&isnumber=8449161


### Dockerization Hardening

P. Ranaweera, V. N. Imirth, M. Liyanage, and A. D. Jurcut, “Security as a Service Platform Leveraging Multi-Access Edge Computing Infrastructure Provisions,” researchgate.net, pp. 1–7. \
Keyword – Security as a Service, Docker, Dockerization, Security, IoT \
This paper talks about docker as security as a service. They first talk about why they choose docker for this investigation was that it was lightweight and fairly secure in their default configuration. They all used edge cases to test the docker container for performance and to see how it would handle these. They found that docker was suitable for there test even when scraping and building the containers for an app it was relatively quick and effective. The end of the paper talking about optimizing security service provisioning. This was showing that using docker to launch multiple security instances is viable when date rates are increased. This helps to show the docker can be used securely in an organization. \
URL - https://www.researchgate.net/profile/Madhusanka_Liyanage/publication/338853880_Security_as_a_Service_Platform_Leveraging_Multi-Access_Edge_Computing_Infrastructure_Provisions/links/5e2fc88ea6fdcc309695b451/Security-as-a-Service-Platform-Leveraging-Multi-Access-Edge-Computing-Infrastructure-Provisions.pdf \

### CIF Literature

J. Elmellas, “Knowledge is power: the evolution of threat intelligence,” ScienceDirect, pp. 1–5, Jul. 2016. \
Keyword - CIF, Security, Threat Intelligence \
This paper starts by talking about threat intelligence and how the need for the collaboration came about the birth of the Collective Intelligence Framework. And how CIF can be used for IP, Autonomous System Numbers, email addresses, domain names, and URLs. The researcher talks about the ease that CIF allows for automating the use of dating being brought to it. The researcher goes into detail about using SIEM (Security Information and Event Management) Software to gather multiple tools logs and pass the correct data to the CIF. Then share it with others. He ends the paper talking about TAXII(Trusted Automated Exchange of Indicator Information) standard that is being adopted for the situation for multiple organizations to share information. \
URL - PDF is in issue No. 12 \

----------

Keywords - Cyber Threat Intelligence Capability, Super SEIM

This book services as guidance for successful development and implementation of cyber threat intelligence capability. It derives its conclusions from the personal observations of the author.
Two critical take aways:
* It is critical that business objectives are clearly defined so that the most appropriate cyber threat intelligence capability can be built.
* Threat Intelligence feed is different from data feed. Often intelligence is sold when in fact it is just data. Threat intelligence is data that has been vetted by some process or procedure and it satisfies three different requirements:
  *	Relevant
  *	Actionable
  *	Valuable
  
H. Dalziel, E. Olson, and J. Carnall, How to define and build an effective cyber threat intelligence capability. Amsterdam: Syngress, an imprint of Elsevier, 2015.

----------

Keywords: Collective Intelligence, Web 2.0 Applications

1.	Problem Statement
There is currently no applications specifically tailored to the special education sector. An information system needs to be designed surrounding special education data—one which ingests data from a variety of different contexts and settings. Data input must have good UX design so as to easily sift through data and to easily utilize the data to make strategic and informed decisions for the clients.
2.	Research Question(s)
What is a design and implementation strategy for developing a special-purpose collective intelligence application within the domain of special education data?
3.	Contribution:
There is value in using the collective intelligence model in the special education sector because data is often collected in silos. A single application that ingests data from all the different sources can identify patterns and make more informed decisions on future endeavors.
This paper identifies seven principle collective intelligence requirements:
    - Task specific representations
    - Data is the key
    - Users add value
    - Facilitate data aggregation
    - Facilitate data access
    - Facilitate access for all devices
    - The perpetual beta (continuous improvement)
4.	Rationale
Researchers claim that, at the time of this publication, there did not exist a tailored application to the special education sector.
5.	Investigative Approach:
Developed over 18 month field trial with one student with autism. Started with a prototype and with feedback made tweaks and increased features over time.
6.	Lessons Learned:
A collective intelligence model can be applied to many different contexts—likely any context where the aggregated information from various contexts all surrounding the same issue or problem can yield revealing insights.

D. G. Gregg, “Designing for collective intelligence,” Communications of the ACM, vol. 53, no. 4, p. 134, Jan. 2010.




