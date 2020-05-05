# CIF CYBR
## Executive Summary
The Collective Intelligence Framework, or CIF, is built to intelligently retrieve threat information from various sources, and use that information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based on these observations. The process is split into seven parts: parse, normalize, post-process, store, query, share, and produce.

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF holds a database of millions of records of threat intelligence. One source of the threat intelligence information is from Palo Alto hardware. Information is pulled from Palo Alto devices and pushed to CIF, then pushed to Palo Alto devices within CIF. At this time, a script is run once a day to automatically copy threats into a file, then manually added to the CIF. For this project, it is the aim to make this threat pulling process more automatic. Palo Alto will update their threat information numerous times a day, and it would be more effective to collect this information and push to CIF numerous times a day, rather than once a day. The goal is to pull information from Palo Alto every 15 minutes and update CIF with the information pulled.

## Project Goals

* Familiarize ourselves with the CIF framework to better understand the system
* Setup sandbox environment with CIF
* Research Palo Alto documentation and other resources to better understand the API
* Reduce threat intelligence collection and distribution from one day to 15 minutes
* Enable process automation between CIF framework and Palo Alto by using/creating appropriate APIs
* Document key findings and processes that were attempted in the sandbox environment

## Project Methodology
### Baseline Measurement

* Measure the number of new threats ingested into Palo Alto firewalls within a 24hr period within the current system.
  * Spoke with customer and he confirmed he can set up a Palo Alto firewall with a rule to collect a 7-day log report for us to use as a baseline measurement for blocked IPs during that period to show how much traffic is being passed during that timeframe.

### Build and Implement Solution

* Extend CIFv4 API

  * Build an additional endpoint into CIF server which outputs a list of IP indicators in Palo Alto ingestible format
    * Indicators are retrieved from other universities under the CIF framework

### Conduct Post-Solution Measurement

* Generate Palo Alto report to show blocked IPs after endpoint implementation and compare with baseline metrics gathered from the original baseline. This is to show that bocking the IPs every 15 minutes can cut down on traffic that is making its way into the network. This will require a 7-day log of post implmentation. 

* Calculate and document any differences perceived following implementation

## Results / Findings

--------------------------------[Needs To Be Added]-----------------------

## Install Instructions
A github repostitory containing only materials needed for installation has been created:
https://github.com/Jacksonurrutia/CIF-V4-PALO

