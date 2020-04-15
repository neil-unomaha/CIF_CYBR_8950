# CIF Installation Walkthrough
This guide provides step-by-step instructions on how to install [CIF version 4](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book) on a virtual machine.  
* [Official CIF 4 installation instructions can be found here](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton).  This walkthrough provides supplemental details and screenshots in hopes of making installation more user-friendly.

## Maxmind Account Prerequisite
* CIF version 4 has a dependency on [Maxmind](https://www.maxmind.com/en/home), so you must setup an account.  We setup the free account, specifically for the [Geolite2 Databases product](https://dev.maxmind.com/geoip/geoip2/geolite2/).
* After you setup your Maxmind account for the Geolite2 Databases product, you need to generate your license key.  On the sidepanel, click "My Lcense Key" and follow the instructions:

![Maxmind My License Key link](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-1.PNG)
![Maxmind Generate License Key Button](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-2.PNG)
![Maxmind Generate License Key Cpnfirm](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-license-key.PNG)
* It is critical that in this version of `CIF` you specify the options depicted in the picture.  This is because CIF version 4 utilizes geoipupdate version 2.3.1, so it will not work for the GEolite2 Databases product unless you specify those options.  This issue is (addressed by the existing CIF maintainer here)[https://github.com/csirtgadgets/verbose-robot/issues/87].   

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

## Setup environnment variables
Before running the CIF docker container, you need to create some environment variables.

The first environment variable is `CIF_TOKEN` which will contain a randomly generated string. This string ultimately becomes the bearer token passed in for all of your GET and POST requests via the request header for security (exception: we made our palo endpoint not require a bearer token be passed in). You can generate a random string with the following command on Ubuntu:

    head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'
    
An example output is the following:

    ce52fd26bc3d3f7a1f73dfddeeb36a4a7a59586aef40205df8f55c170b6b2e46
    
The other two required environment variables are `MAXMIND_USER_ID` AND `MAXMIND_LICENSE_KEY`. Each of these environment variables capture your Maxmind Account ID and your Maxmind License Key that you were adised to copy down [in the instructions above](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#maxmind-account-prerequisite).

Here is an example command to setup these environment variables. **Note**: that you'll want to swap out the values for` MAXMIND_USER_ID` and `MAXMIND_LICENSE_KEY`!

    export CIF_TOKEN=`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'`
    export MAXMIND_USER_ID=YOUR-ACCOUNT-ID
    export MAXMIND_LICENSE_KEY=YOUR-LICENSE-KEY
    
## Run the CIF docker container
With the environment variables all setup, you can now run your CIF docker image:

    sudo docker run -e CIF_TOKEN="${CIF_TOKEN}" -e MAXMIND_USER_ID="${MAXMIND_USER_ID}" -e MAXMIND_LICENSE_KEY="${MAXMIND_LICENSE_KEY}" -it -p 5000:5000 -d --name verbose-robot csirtgadgets/verbose-robot:latest

* This command will go out to docker hub and install the CIF version 4 image

**Explaining the above options**:
* We pass into the running docker container the three environment variables we specified above with the `-e` flag
* We setup port forwarding on port 5000 with the `-p` flag
* We run the docker container in a daemon with `-d`
* For ease of referencing our docker container in the future, we labeled the container `verbose-robot`

