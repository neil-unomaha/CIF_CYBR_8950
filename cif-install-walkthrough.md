# CIF Installation Walkthrough
This guide provides step-by-step instructions on how to install [CIF version 4](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book) on a virtual machine.  
* [Official CIF 4 installation instructions can be found here](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton).  This walkthrough provides supplemental details and screenshots in hopes of making installation more user-friendly.

## Maxmind Account Prerequisite
* CIF version 4 has a dependency on [Maxmind](https://www.maxmind.com/en/home), so you must setup an account.  We setup the free account, specifically for the [Geolite2 Databases product](https://dev.maxmind.com/geoip/geoip2/geolite2/).
* After you setup your Maxmind account for the Geolite2 Databases product, you need to generate your license key.  On the sidepanel, click "My Lcense Key" and follow the instructions:

![Maxmind My License Key link](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-1.PNG)
![Maxmind Generate License Key Button](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-2.PNG)
![Maxmind Generate License Key Cpnfirm](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-3.PNG)
![Maxmind Generate License Key](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-4.PNG)

* The screenshot above has our Account ID and License key censored out.  
* **Write down your Account ID and License key.  You will need to specify it as an environment variable within your CIF VM later on.**


## Install Ubuntu 16.04 server
* Head over to https://releases.ubuntu.com/16.04 to install Ubuntu server, version 16.04
* [As detailed here](https://github.com/csirtgadgets/verbose-robot/wiki/FAQ#ubuntu-lts-desktop) the desktop version is not supported.  We also found that the 32-bit server versionw as having issues
* Specifically, we installed the 64-bit PC (AMD64) server install image: **16.04.6**
![Screenshot of Ubuntu server download](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif1.PNG)
* After you install the image, create your virtual machine with your preferred virtualization product (i.e. VMware, Virtualbox, etc)

## Install additional software within your Ubuntu server virtual machine
* After you startup your VM for the first time, we commend installing the `ubuntu-desktop` gui plugin for ease of use:

      sudo apt-get update
      sudo apt-get install ubuntu-desktop
* After the install you will likely need to restart the VM in order for the changes to take effect
* Next you will need to install docker

      sudo apt install docker.io
* Now that docker is installed, you can install the cif version 4 docker image from docker hub

      sudo docker pull csirtgadgets/verbose-robot
## Create Maxmind Account
