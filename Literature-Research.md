# Literature and Research Material

### Process Automation Articles

J. K. Visser and H. T. Malan, “Identification of risk associated with process automation systems,” Int. J. Econ. Manag. Eng, vol. 13, no. 7, pp. 1044–1051, 2019. \
Keyword - Process Automation, Risk, System Performance, Third-Party Communication, Interface Compatibility \
This paper was a study that was sent to 172 instrument technicians and technology managers. This was to identify risk in process automation systems. The focused 5 areas of risk: lack of skilled technicians, integration of capability of the third-party system software, reliability of the process automation hardware, excessive costs pertaining to performing maintenance and migrations on the automation systems, and requirements of having third-party communication interfacing compatibility as well as real-time communication networks. This works addresses these problems and gives a conceptual framework in a way to follow to remedy these issues. \
URL - https://pdfs.semanticscholar.org/b845/bde145526fb9fff7517161337533982defc9.pdf \

### API Integration / Middleware for Connecting APIs

S. Chang-Woo, L. Daesung, C. Kyung-Yong, R. Kee-Wook, and L. Jung-Hyun, “Interactive middleware architecture for lifelog based context awareness,” Multimedia Tools and Applications, vol. 71, Jan. 2013. \
Keyword - Middleware, Centralized Storage, DBMS, Multiple Middleware, Mobile Devices, Logs \
This paper reference all the different forms of information being made today. There is a need for middleware to be able to obtain it from all sources and store it in a centralized location or DBMS. The research shows how effective middleware is an important issue that needs to be addressed. The paper goes on to address the distributed environment and how they communicate, and the middleware needed to allow a different type of hardware to talk. They talk about a lot of other work and explain there experiment fairly well for the common reader to understand. \
URL - https://link.springer.com/article/10.1007/s11042-013-1362-7 \

-----

Keywords: API development, API maintenance, software platform APIs, API review, multi-device API

1. Problem Statement: In the beginning, the Tizen API had simple submissions and approvals via emails between the developers and reviewers. There was no way to effectively track changes or share with other stakeholders of the API unless explicitly made a recipient of the email chain.

2. Research Question(s)

  - Can the process of updating Tizen API be improved?
  - How can they share information about Tizen API with other stakeholders if changes are made?

3. Contribution:

  - JIRA bug system was implemented to provide a submission-based/approval-based workflow, task search ability, status-change notifications, etc.
  - API Change Requests (ACR) had different states in JIRA system for updates, reviews, preparations, approvals, etc. Stakeholders are applied with specified responsibilities/tasks for each state.

4. Rationale: The paper argues that research has been done improving API usability frameworks, but no report of API process that is designed and used in a large-scale software platform.

5. Investigative Approach

  - They took their time to come up with a detailed process of ACR when it came to the API and recognizing the environment it operates in. The paper claims the new process helps stakeholders work more efficiently while maintaining API consistency for usability and backward compatibility.

6. Lessons learned

  - There are various ways and methods organizations and individuals try to improve their APIs and update process. Different organizations/devices will have different needs from each API

H. Kwon, J. Ahn, S. Choi, J. Siewierski, P. Kosko and P. Szydelko, "An Experience Report of the API Evolution and Maintenance for Software Platforms," 2018 IEEE International Conference on Software Maintenance and Evolution (ICSME), Madrid, 2018, pp. 587-590.
doi: 10.1109/ICSME.2018.00034
URL: http://ieeexplore.ieee.org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=8530070&isnumber=8529823

-----

V. Chang, "Design of middleware platform to enhance abilities of application systems integration," International Conference on Information Technology: Coding and Computing (ITCC'05) - Volume II, Las Vegas, NV, 2005, pp. 461-466 Vol. 2.
doi: 10.1109/ITCC.2005.123
keywords - Linux;middleware;graphical user interfaces;software metrics;software development management;software maintenance;protocols;Linux/Unix base middleware platform design;application systems integration;GUI operating interface;software editing;software upgrading;software updating;software integration;software system development;data transmission;API;application software protocol;TCP/IP protocol;X.25 protocol;SNA protocol;Middleware;Application software;Technology management;Protocols;Pervasive computing;Switches;Condition monitoring;Operating systems;Costs;Cities and towns;GUI operating interface;TCP/IP;API;Linux;X.25;SNA  
(Add Paragraph with info)  
URL: http://ieeexplore.ieee.org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=1425186&isnumber=30769


### Systems Architecture Integration

R. T. Tiburski, L. A. Amaral, E. D. Matos, and F. Hessel, “The importance of a standard security architecture for SOA-based IoT middleware,” Institute of Electrical and Electronics Engineers, vol. 53, no. 12, pp. 20–26, Dec. 2015. \
Keyword – IoT, System Architecture, Middleware, Security, Standard Architecture \
This paper talks about integration into systems for IoT devices. It goes into detail about the middleware needed to monitor IoT devices on the systems. The paper reference how a Service-Oriented Architecture (SOA) is useful for integration from new devices. After the discussion of SOA, it talks about the company using Resource-Oriented Architecture alongside the SOA to bring the benefits of IoT devices into a company infrastructure. Then the paper talks about the security risks that come with the IoT devices and ways to mitigate them. This paper is a good reference for System Architecture Integration examples because it shows how to bring IoT devices into the mix. \
URL: https://www.researchgate.net/publication/290378256_The_Importance_of_a_Standard_Security_Architecture_for_SOA-based_IoT_Middleware \

### Web Services Literature

E. B. Fernandez, N. Yoshioka, and H. Washizaki, “Patterns For Cloud Firewalls” AsianPLoP (pattern languages of programs), pp. 1–11. \
Keyword - Firewalls, Security patterns, Network security, Cloud Computing, Services \
This paper gives a generalized view of different firewall configurations for single businesses and multiple businesses. They discuss how one firewall can filter traffic to one customer differently than it filters to another customer. By setting group rules for any traffic going to certain IP ranges or domains. They talk about in detail about cloud-based firewalls like amazon uses their firewalls and how they are configured. It gives a nice explanation of the configuration and how every business is a little different. The paper also talks about having multiple firewalls and each one does something different. Some firewalls only do security groups while others are for whitelisting. It gives detail on why the configuration is made like this and have a lot of good images to visualize this. \
URL - https://www.researchgate.net/publication/266385038_Patterns_for_cloud_firewalls \


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

----

keywords: {application program interfaces;software reusability;system documentation;systematic mapping study;API documentation generation approaches;software reuse;software developers;API documentation process;API documentation generation tools;natural language documentation;code examples;API users;API documentation approaches;Documentation;Data mining;Tools;Software;Libraries;Systematics;Application programming interfaces;API;API Documentation;Systematic mapping study}

1. Problem Statement
Maintaining API documentation is a burdensome task. Especially when code updates are frequent, documentation updates often get overlooked. Tools are required to aid in this process.

2. Research Question(s)
* What approaches exist for creating new and improving existing API documentation?
* How do the approaches contribute to API documentation?
* What are the sources for API documentation?
* What are the quality properties of the approaches?
* How are the documentation approaches evaluated?
3. Contribution:
A representation of what the current literature in the domain of API documentation expresses is important in order to maintain up-to-date API documentation.
4. Rationale
Documentation is crucial. Without an authoritative source providing documentation for their code artifacts, users will turn towards the internet on crowd-sourced platforms where it is not guaranteed they will receive the best guidance.
5. Investigative Approach:
Conducted a systematic mapping study regarding various search terms related to APIs. They then analyzed the API documentation strategies discussed in those papers. Most approaches to
6. Lessons Learned:
The results from the study suggest that, if the quality of the API documentation is to be maintained: tools to generate the API documentation must be used. The study suggests that a significant amount of API documentation generation tools focus on producing natural language and code examples. This article thus postulates that these are the two areas that are most lacking in API documentation.
Major of papers reference tools, while others use plugins, but which ultimately produce templates which include natural language documentation and code examples.

K. Nybom, A. Ashraf and I. Porres, "A Systematic Mapping Study on API Documentation Generation Approaches," 2018 44th Euromicro Conference on Software Engineering and Advanced Applications (SEAA), Prague, 2018, pp. 462-469.
doi: 10.1109/SEAA.2018.00081,
URL: http://ieeexplore.ieee.org.leo.lib.unomaha.edu/stamp/stamp.jsp?tp=&arnumber=8498248&isnumber=8498147

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

----

keywords: {multi-agent systems;human swarming method;parallel distributed intelligence;autonomous robots;simulated agents;UNU platform;artificial swarm intelligence;ASI;collective intelligence;Real-time systems;Sociology;Statistics;System recovery;Force;Decision making;Neurons}

1. Problem Statement
Aggregating individual opinion asynchronously, such as by polling, does not provide the opportunity for real-time collective intelligence to emerge. 
2. Research Question(s)
What is the comparison of human swarming to that of decision making done asynchronously?
What are the critical components that yield successful human swarms?
3. Contribution: 
Software makes it possible to conduct real-time negotiation 
4. Rationale
Various mechanisms in use can cause entrenchment, and polarizing view.  Hearding and snowballing effects are sometimes seen with existing mechanisms.
5. Investigative Approach:
Baseline was using surveys to ask participants asynchronously two pilot studies: the weight of a cow in a picture, and the 2015 academy aware winners. They then did the same thing but with their human swarm software UNU
6. Lessons Learned:
Collective intelligence has sub categories.  Collective intelligence such as polling is good for reviewing average sentiment and popular opinion, but it is not a mechanism for negotiation.   In fact, polling can cause entrenchment.   
Designed software where each user controls a magnet on a puck,  The puck is in the center of the screen.  A question is asked, and the various options are at the edges of their screen.  They position their magnet to pull in their direction of their choice, but lots of people are doing this at the same time which reveals realtime feedback.  
Human swarming, a type of collective intelligence, can be more efficient, and even more accurate, than individual experts, or even traditional statistical means of using averages. 

L. B. Rosenberg, "Human swarming, a real-time method for parallel distributed intelligence," 2015 Swarm/Human Blended Intelligence Workshop (SHBI), Cleveland, OH, 2015, pp. 1-7.
doi: 10.1109/SHBI.2015.7321685

