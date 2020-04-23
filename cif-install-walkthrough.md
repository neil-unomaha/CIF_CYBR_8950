# CIF Installation Walkthrough
This guide provides step-by-step instructions on how to install [CIF version 4](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book) on a virtual machine.  
* [Official CIF 4 installation instructions can be found here](https://github.com/csirtgadgets/verbose-robot/wiki#the-easybutton).  This walkthrough provides supplemental details and screenshots in hopes of making installation more user-friendly.

## Table of Contents
* [Maxmind Account Prerequisite](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#maxmind-account-prerequisite)
* [Install Ubuntu 16.04 server](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#install-ubuntu-1604-server)
* [Install additional software within your Ubuntu server virtual machine](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#install-additional-software-within-your-ubuntu-server-virtual-machine)
* [Setup environnment variables](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#setup-environnment-variables)
* [Run the CIF docker container](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#run-the-cif-docker-container)
* [Install software within running CIF docker container](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#install-software-within-running-cif-docker-container)
* [Copy Palo Endpoint Code into the CIF docker container](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#copy-palo-endpoint-code-into-the-cif-docker-container)
* [Restart CIF and test new palo endpoint](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#restart-cif-and-test-new-palo-endpoint)
* [Additional custom configurations and Final Thoughts](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#additional-custom-configurations-and-final-thoughts)

## Maxmind Account Prerequisite
* CIF version 4 has a dependency on [Maxmind](https://www.maxmind.com/en/home), so you must setup an account.  We setup the free account, specifically for the [Geolite2 Databases product](https://dev.maxmind.com/geoip/geoip2/geolite2/).
* After you setup your Maxmind account for the Geolite2 Databases product, you need to generate your license key.  On the sidepanel, click "My Lcense Key" and follow the instructions:

![Maxmind My License Key link](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-1.PNG)
![Maxmind Generate License Key Button](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-2.PNG)
![Maxmind Generate License Key Cpnfirm](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-license-key.PNG)
* It is critical that for CIF version 4 you specify the options depicted in the picture.  This is because CIF version 4 utilizes `geoipupdate` version **2.3.1**, so it will not work for the GEolite2 Databases product unless you specify those options.  This issue is [addressed by the existing CIF maintainer here](https://github.com/csirtgadgets/verbose-robot/issues/87).   

![Maxmind Generate License Key](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-maxmind-4.PNG)

* The screenshot above has our Account ID and License key censored out.  
* **Write down your Account ID and License key.  You will need to specify it as an environment variable within your CIF VM later on.**

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Install Ubuntu 16.04 server
* Head over to https://releases.ubuntu.com/16.04 to install Ubuntu server, version 16.04
* [As detailed here](https://github.com/csirtgadgets/verbose-robot/wiki/FAQ#ubuntu-lts-desktop) the desktop version is not supported.  
* Specifically, we installed the 64-bit PC (AMD64) server install image: **16.04.6**
![Screenshot of Ubuntu server download](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif1.PNG)
* After you install the image, create your virtual machine with your preferred virtualization product (i.e. VMware, Virtualbox, etc)

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Install additional software within your Ubuntu server virtual machine
* After you startup your VM for the first time, we recommend installing the `ubuntu-desktop` gui plugin for ease of use:

      sudo apt-get update
      sudo apt-get install ubuntu-desktop
* After the install you will likely need to restart the VM in order for the changes to take effect
* Next you will need to install docker

      sudo apt install docker.io

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Setup environnment variables
Before running the CIF docker container, you need to create some environment variables.

* You will set these environment variables on your _host_ virtual machine.  Later on when you execute the command to boot up the CIF docker container, you will pass these environment variables in as arguments.

The first environment variable is `CIF_TOKEN` which will contain a randomly generated string. This string ultimately becomes the bearer token passed in for all of your GET and POST requests via the request header for security (exception: we made our palo endpoint not require a bearer token be passed in). You can generate a random string with the following command on Ubuntu:

    head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'
    
An example output is the following:

    ce52fd26bc3d3f7a1f73dfddeeb36a4a7a59586aef40205df8f55c170b6b2e46
    
The other two required environment variables are `MAXMIND_USER_ID` AND `MAXMIND_LICENSE_KEY`. These two environment variables capture the Maxmind Account ID and your Maxmind License Key values you were advised to copy down [in the instructions above](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#maxmind-account-prerequisite).

Here is an example command to setup these environment variables. **Reminder**: you'll need to swap out the values for` MAXMIND_USER_ID` and `MAXMIND_LICENSE_KEY`!  

    export CIF_TOKEN=`head -n 25000 /dev/urandom | openssl dgst -sha256 | awk -F ' ' '{print $2}'`
    export MAXMIND_USER_ID=YOUR-ACCOUNT-ID
    export MAXMIND_LICENSE_KEY=YOUR-LICENSE-KEY

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Run the CIF docker container
With the environment variables all setup on your virtual machine, you can now run your CIF docker image:

    sudo docker run -e CIF_TOKEN="${CIF_TOKEN}" -e MAXMIND_USER_ID="${MAXMIND_USER_ID}" -e MAXMIND_LICENSE_KEY="${MAXMIND_LICENSE_KEY}" -it -p 5000:5000 -d --name verbose-robot csirtgadgets/verbose-robot:latest

* This command will go out to docker hub and install the CIF version 4 image, and then run it in a container

**Explaining the above options**:
* We pass into the running docker container the three environment variables we specified above with the `-e` flag
* We setup port forwarding on port 5000 with the `-p` flag
* We run the docker container in a daemon with `-d`
* For ease of referencing our docker container in the future, we labeled the container `verbose-robot`

To confirm our docker container is running, we can run `sudo docker ps`
![Show running CIF docker container](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/Assets/cif-install-walkthrough-assets/cif-running.PNG)

If you executed the above commands to run the container and the container is not listed, you can run `sudo docker logs <YOUR-CONTAINER-ID>` in order to debug.  Likely there is an issue with your maxmind license key because you didn't specify the correct options while creating the license key. [Reference this step for details](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#maxmind-account-prerequisite).

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Install software within running CIF docker container
You will need to `bash` into your CIF docker container with the following command:

    sudo docker exec -it verbose-robot /bin/bash

Once you are bashed in, install your favorite text editor.  We installed `nano`:

    apt-get update
    apt-get install nano

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Copy Palo Endpoint Code into the CIF docker container
While bashed into your CIF docker container, you will need to make two changes:
1. Add three changes to `/usr/local/lib/python3.6/site-packages/verbose_robot-4.0.1-py3.6.egg/cif/httpd/app.py`
    * [Here is the new app.py file with the changes](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-palo-changes/app.py).
    * There are three minor additions.  You can either manually add those three changes (located with comment `# PALO ENDPOINT`), or you can replace the entire app.py file

2. Add the new palo.py endpoint file to `/usr/local/lib/python3.6/site-packages/verbose_robot-4.0.1-py3.6.egg/cif/httpd/palo.py`
    * [The file can be found here](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-palo-changes/palo.py)

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Restart CIF and test new palo endpoint
`Supervisord` is the orchestator of all the running CIF processes.  The easiest way to restart CIF in order to load in all the changes is to kill the runninging Supervisord process.  After the process is killed, it will automatically restart:

    PID=`ps aux | grep supervisord | grep -v grep | awk -F ' ' '{print $2}'`
    kill -HUP $PID

It shouldn't take longer than about 30 seconds for CIF to restart all its processes.  You can confirm it is back up and running within your VM's browser by going to `localhost:5000`.
* If that works, then the final test is to confirm the palo endpoint is working with: `localhost:5000/palo/1`

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)

## Additional custom configurations and Final Thoughts
There are a number of custom configurations you might want to include in your specific instance of CIF.  [CIF version 4 has a decent overview of its features and configurations in its wiki](https://github.com/csirtgadgets/verbose-robot/wiki/The-CIFv4-Book).  

* One particular configuration worth mentioning: **threat feeds**.  When you originally boot up CIF, it immediately starts pulling indicators from the **default threat feeds**.  The configuration for these threat feeds is located in: `/etc/cif/rules/default`.  You may decide to remove a number of those threat feeds, or include additional threat feeds. 

[back to top](https://github.com/neil-unomaha/CIF_CYBR_8950/blob/master/cif-install-walkthrough.md#table-of-contents)
