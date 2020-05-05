# Improving the Collective intelligence Framework:
### Final Report
## Executive Summary
The Collective Intelligence Framework [CIF] is built to intelligently retrieve threat information from various sources.  CIF uses threat information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based on these observations. The process is split into seven parts: parse, normalize, post-process, store, query, share, and produce.

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF is able to hold a database of millions of records of threat intelligence. One source of the threat intelligence information can be from Palo Alto hardware. --Information is pulled from Palo Alto devices and pushed to CIF, then pushed to Palo Alto devices within CIF. At this time, a script is run once a day to automatically copy threats into a file, then manually added to the CIF. For this project, it is the aim to make this threat pulling process more automatic. Palo Alto will update their threat information numerous times a day, and it would be more effective to collect this information and push to CIF numerous times a day, rather than once a day. The goal is to pull information from Palo Alto every 15 minutes and update CIF with the information pulled.--

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
  * Spoke with the customer and he confirmed he can set up a Palo Alto firewall with a rule to collect a 7-day log report for us to use as a baseline measurement for blocked IPs during that period to show how much traffic is being passed during that timeframe.

### Build and Implement Solution

* Extend CIFv4 API

  * Build an additional endpoint into CIF server which outputs a list of IP indicators in Palo Alto ingestible format
    * Indicators are retrieved from other universities under the CIF framework

### Conduct Post-Solution Measurement

* Generate Palo Alto report to show blocked IPs after endpoint implementation and compare with baseline metrics gathered from the original baseline. This is to show that blocking the IPs every 15 minutes can cut down on traffic that is making its way into the network. This will require a 7-day log of post-implementation.  

* Calculate and document any differences perceived following implementation

## Results / Findings
The team was able to communicate with the stakeholder of the project and retrieve reports from their Palo Alto Firewall. The report contained traffic for a 2.5-hour timeframe, and will also include threat alerts for the day. A filter was applied to the report to identify when the threat was first seen, then 15 minutes after that timestamp, traffic from that threat will be ignored going forward. This is to simulate the expected operation of the new endpoint developed if implemented in the CIF environment.

A 2.5-hour spanned network packet capture was used and contained IP addresses that were deemed malicious. Each captured packet in the file from identified malicious sources was marked and their respective IP addresses recorded. Fifteen minutes after the initial timestamp, the rest of the packets from the malicious IP were willfully ignored, as to simulate the endpoint, and artificially considered blocked. From this capture, 44 unique IP addresses were marked as malicious. In total, 162 malicious packets were captured in the 2.5-hour duration. From this analysis, it was found if the endpoint was implemented, 93 of the packets would have been dropped. Potentially, 50%-60% of malicious traffic could be dropped. However, since this was a capture in a short duration of time, most of these IP addresses could have been attacking the network before the capture started, as well as after the packet capture stopped.

It should be noted that this is a limited view of the network traffic. Malicious traffic can vary on a day-by-day basis. This was a 2.5-hour capture of traffic. If the report was over a day or even a week, the results could be more impactful.

## Install Instructions
A Github repository containing only materials needed for installation has been created:
https://github.com/Jacksonurrutia/CIF-V4-PALO

