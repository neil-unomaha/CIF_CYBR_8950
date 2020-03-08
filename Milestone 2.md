# Milestone 2


## Research Outline

* Introduction

  * Explain CIF and its goals (high level)
    * Sharing malicious IPs with other universities to block

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

* Metric Analysis

  * Collect metrics from CIF about IPs that were blocked on just a day-to-day basis
  * Collect metrics from CIF about IPs that were blocked every 15 minutes (as often as Palo Alto should request updated information)
  * Compare findings and summarize differences found between the metrics

* Other notable challenges/issues?
  * Issues with environment setup
  * Issues with scripting
  * etc.

* Conclusion/Wrap up

  * Summarize findings, metrics, lessons learned, etc.
  * Submit pull request for CIFv4

-----

## Research Abstract
