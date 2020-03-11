# Milestone 2

## Environment Setup and Hardships

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
    * Set up test environment in such a way that the universities may exchange information every 15 minutes
  * Rest of paper will flow as...
    * Previous research/work
    * Methodology
    * Results and findings
    * Conclusion and further research considerations

* Background/Literature Review
  * *TO BE FILLED IN WHEN MORE LITERATURE REVIEW IS AVAILABLE*

* Methodology
  * CIF Architecture
    * Display diagram of current CIF process
      * Current pull and push process with Palo Alto firewalls
    * Explain CIF process
      * YML files with tokens from each university within CIF
      * Cron job that is run daily to retrieve updated information
      * Python and Flask details
    * Explain why current process is not most efficient
      * Current cron job works in roundabout way

  * CIF Environment Research and Setup

    * Explain our reasoning to use CIFv4 and not v3
      * CIFv3 is in process of getting deprecated, so v4 is preferred
    * Explain environment setup
      * VMs for v4
        * Built on Ubuntu Server 16.04
        * Document challenges and issues that came about
          * [Challenges Issue for CIF](https://github.com/neil-unomaha/CIF_CYBR_8950/issues/20)
      * Mention CIFv3 server we were given access to for getting familiar with CIF
    * CIF Research
      * Uses Python >3.6 and Flask framework
      * Mention resources we used to learn more about Python and Flask
    * Challenges in research and setup
      * CIFv3 connection issues
        * Unable to connect with VPN most of the time
          * Connection refuse messages abound
      * Getting familiar with Python and Flask
        * Used Lynda to research
          * Free with Omaha Public Library card

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

The Universities of Nebraska have a shared IP database management system call CIF (Collective Intelligence Framework). That it uses to manage IPs that will be blocked across all the university’s campus by Pal Alto Firewall. The problem with this system that it is only updating the firewall once a day when it is run by a cron job. This is allowing IP addresses that need to be blocked to continually enter the network for a day before it can be stopped. Some companies are using blocking IP addresses by possible attacks on the network by using honeywords which are fake passwords when entered while triggering the system to block the IP address associated with the user who entered the password. (K. Naik, V. Bhosale, and V. D. Shinde) Other companies share intel reports to see possible threats and even sell reports so others can block malicious sources. (J. Elmellas, “Knowledge is power: the evolution of threat intelligence”) This is to prevent a malicious source before it ever touches one’s networks. Our capstone group is aiming to reduce the time for the blocks to be put into effect to reduce the potential traffic from these malicious IP addresses. To achieve this goal our group is building a plug-in for the CIF database to do these IP blocks every 15 minutes without having to have human interference. To show that this solution will provide a positive effect on the network the capstone group will be doing a 7-day report before and after on network traffic metrics to show if traffic is changed from adding in our plugin to the system. (INSERT FINDING HERE) (Conclusion)

-----

## Visuals and Diagrams


-----
