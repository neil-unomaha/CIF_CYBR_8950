# NU CIF Capstone 
A Capstone project at the University of Nebraska-Omaha.  

We aspire to extend the functionality of [CIF version 4](https://github.com/csirtgadgets/verbose-robot/wiki/Introduction), a Cyber Threat Intelligence Management System, by adding an additional endpoint specific for Palo Alto firewalls.

## Features of Palo Alto Endpoint in CIF
#### Compliant to Palo Alto 
* Palo Alto External Block List requirements described [here](https://docs.paloaltonetworks.com/pan-os/8-1/pan-os-admin/policy/use-an-external-dynamic-list-in-policy/external-dynamic-list.html#idf36cb80a-77f1-4d17-9c4b-7efe9fe426af), as well as [here](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClVYCA0).
#### Paging
* Palo Alto External Block List requirements specify limit of 5,000 IP addresses per block list.
      
      # Example usage
      # Returns first set of 5,000 IP addresses
      localhost:5000/palo/?page_num=1
      
      # Returns second set of 5,000 IP addresses
      localhost:5000/?page_num=2

#### User Input Sanitization 
* For security, user input is validated

## Check Out the Feature Yourself
Checkout our [walk-through guide](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md) where we talk through, step-by-step, how to setup CIF version 4, and how to plug in our feature. Setup will take you less than one hour.
