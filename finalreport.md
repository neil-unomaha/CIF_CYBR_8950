# Improving the Collective intelligence Framework:
### Final Report
## Executive Summary
The Collective Intelligence Framework [CIF] is built to intelligently retrieve threat information from various sources.  CIF uses threat information for incident response, intrusion detection, and mitigation. Most commonly, this framework works with IP addresses, domains, and URLs that have been suspected to be malicious. The framework works to analyze data at different times to make observations and build reputations based on these observations. The process is split into seven parts: parse, normalize, post-process, store, query, share, and produce.

Within this existing framework, the project will focus on the store portion of the process and thus will be discussing this part in more detail. CIF is able to hold a database of millions of records of threat intelligence. One source of the threat intelligence information can be from Palo Alto hardware. Within the existing setup of CIF at the Univesrsity of Nebraska-Lincoln, a script is written which pulls in new CIF indicators and writes them to a series of files.  Palo Alto then once per day pulls in these indicators.  Our goal was to reduce the burden on the UNL IT department, as well as other CIF end users, by removing the need to write a custom script to pull in the new CIF indicators.  Our goal was to write a new endpoint into CIF that Palo Alto can directly pulled from.  Palo Alto would then be re-configured to pull from this new endpoint every fifteen minutes.

## Project Goals

* Familiarize ourselves with the CIF framework to better understand the system
* Setup sandbox environment with CIF
* Research Palo Alto documentation and other resources to better understand the API
* Reduce threat intelligence collection and distribution from one day to 15 minutes
* Enable process automation between CIF framework and Palo Alto by using/creating appropriate APIs
* Document key findings and processes that were attempted in the sandbox environment


### Original Methodology
#### Baseline Measurement

* Measure the number of new threats ingested into Palo Alto firewalls within a 24hr period within the current system.

#### Build and Implement Solution

* Extend CIFv4 API

  * Build an additional endpoint into CIF server which outputs a list of IP indicators in Palo Alto ingestible format
    * Indicators are retrieved from other universities under the CIF framework

#### Conduct Post-Solution Measurement

* Generate Palo Alto report to show blocked IPs after endpoint implementation and compare with baseline metrics gathered from the original baseline. This is to show that blocking the IPs every 15 minutes can cut down on traffic that is making its way into the network. This will require a 7-day log of post-implementation.  

* Calculate and document any differences perceived following implementation

### Revised Methodology
Due to fallout from COVID-19, the manpower was unavailable from UNL to both provide the reports described in the original methodology, and to implement a CIFv4 instance with our solution.

Our revised methodology was was the following
#### Retrieve data to perform an analysis based upon a theoretical model
* Retrieve the previous day's CIF block list
* Retrieve 2.5hrs worth of network traffic
#### Analysis and compare blocking strategies
Compare the amount of blocked malicious IPs based upon a one day strategy vs. a 15-minute strategy


## Results / Findings
The team was able to communicate with the stakeholder of the project and retrieve reports from their Palo Alto Firewall. The report contained traffic for a 2.5-hour timeframe, and will also include threat alerts for the day. A filter was applied to the report to identify when the threat was first seen, then 15 minutes after that timestamp, traffic from that threat will be ignored going forward. This is to simulate the expected operation of the new endpoint developed if implemented in the CIF environment.

A 2.5-hour spanned network packet capture was used and contained IP addresses that were deemed malicious. Each captured packet in the file from identified malicious sources was marked and their respective IP addresses recorded. Fifteen minutes after the initial timestamp, the rest of the packets from the malicious IP were willfully ignored, as to simulate the endpoint, and artificially considered blocked. From this capture, 44 unique IP addresses were marked as malicious. In total, 162 malicious packets were captured in the 2.5-hour duration. From this analysis, it was found if the endpoint was implemented, 93 of the packets would have been dropped. Potentially, 50%-60% of malicious traffic could be dropped. However, since this was a capture in a short duration of time, most of these IP addresses could have been attacking the network before the capture started, as well as after the packet capture stopped.

It should be noted that this is a limited view of the network traffic. Malicious traffic can vary on a day-by-day basis. This was a 2.5-hour capture of traffic. If the report was over a day or even a week, the results could be more impactful.

## Install Instructions
A Github repository containing only materials needed for installation has been created:
https://github.com/Jacksonurrutia/CIF-V4-PALO

