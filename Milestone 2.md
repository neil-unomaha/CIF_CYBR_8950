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
