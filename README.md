<a href="https://blackhillsinfosec.com"><img width="100%" src="https://github.com/her3ticAVI/MiniNet-Framework/blob/main/images/Wififorgev2logo.png" alt="Wifi Forge Logo" /></a>
<br />
<br />

<p align="left">
  <a href="https://github.com/blackhillsinfosec/Wifi-Forge/actions"><img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/blackhillsinfosec/Wifi-Forge/main.yml?style=flat-square"></a>
  &nbsp;
  <a href="https://discord.com/invite/bhis"><img alt="Discord" src="https://img.shields.io/discord/967097582721572934?label=Discord&color=7289da&style=flat-square" /></a>
  &nbsp;
  <a href="https://github.com/blackhillsinfosec/Wifi-Forge/graphs/contributors"><img alt="npm" src="https://img.shields.io/github/contributors-anon/blackhillsinfosec/Wifi-Forge?color=yellow&style=flat-square" /></a>
  &nbsp;
  <a href="https://x.com/BHinfoSecurity"><img src="https://img.shields.io/badge/follow-BHIS-1DA1F2?logo=twitter&style=flat-square" alt="BHIS Twitter" /></a>
    &nbsp;
  <a href="https://x.com/BHinfoSecurity"><img src="https://img.shields.io/github/stars/blackhillsinfosec/Wifi-Forge?style=flat-square&color=rgb(255%2C218%2C185)" alt="Wifi Forge Stars" /></a>
</p>
<hr/>

<div style="text-align: center;">
  <h4>
    <a target="_blank" href="https://google.com" rel="dofollow"><strong>Explore the Docs</strong></a>&nbsp;·&nbsp;
    <a target="_blank" href="https://discord.com/invite/bhis" rel="dofollow"><strong>Community Help</strong></a>&nbsp;·&nbsp;
    <a target="_blank" href="https://google.com" rel="dofollow"><strong>Roadmap</strong></a>
  </h4>
</div>

<hr/>

# Wi-Fi Forge
Wi-Fi Forge provides a safe and legal environment for learning WiFi hacking. Based on the open source [Mininet-Wifi](https://github.com/intrig-unicamp/mininet-wifi/tree/master?tab=readme-ov-file), this project automatically sets up the networks and tools needed to run a variety of WiFi exploitation labs, removing the need for the overhead and hardware normally required to perform these attacks. 

## Disclaimer/Notes
- The installation script will only run on Ubuntu, Debian, Fedora, or Kali. 
- It is suggested to run Wifi Forge on Ubuntu version 24.04 or the lastest version of Kali. 
- The Wifi Forge installation script may disrupt normal operating system use, it is suggested to use a fresh install, virtual machine, or build using the provided dockerfile (see Set-Up Guide/Docker)

## Compatibility
Wifi-Forge should work on any linux operating system using the docker image. The following Operating Systems have been tested and are confirmed to work.
- Kali Linux 
- Parrot OS
- Ubuntu

## Installation

### Docker (recommended)
Note: Dockerfile will fail if mininet-wifi is already installed locally

#### Install from release (best option)
1. Pull image from dockerhub
```bash
sudo docker pull redblackbird/wififorge:v2.0
```
2. Start a new container
  ```bash
  sudo docker run --privileged=true -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /sys/:/sys -v /lib/modules/:/lib/modules/ --name mininet-wifi --network=host --hostname mininet-wifi redblackbird/wififorge:v2.0 /bin/bash
  ```
3. Within docker, initiate the controller to simulate APs
```bash
service openvswitch-switch start
```
4. Run wififorge.py
```python
cd /Wifi-Forge/Framework/
sudo python3 WifiForge.py
```
#### Build from Dockerfile
1. Install Docker
```bash
sudo snap install docker
```

2. Clone the repository
```bash
git clone https://github.com/her3ticAVI/Wifi-Forge
```

3. Run the Dockerfile (may take up to 10 minutes)
```bash
sudo docker build -t wififorge .
```

4. Start a new container (command should automatically initiate a docker shell)
```bash
sudo docker run --privileged=true -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /sys/:/sys -v /lib/modules/:/lib/modules/ --name mininet-wifi --network=host --hostname mininet-wifi wififorge /bin/bash
```

5. Within docker, initiate the controller to simulate APs
```bash
RUN service openvswitch-switch start
```

6. Within docker, run WifiForge.py
```bash
sudo python3 Framework/WifiForge.py
```

### Build from Source
NOTE: While the setup script is stable it is *highly* recommended to only use this install method within a virtual machine. The setup.sh script enables pip's "--break-system-packages," which may break packages important to your machine. 

NOTE: The setup script does not install all the necessary tools to complete the labs - using a kali linux operating system will provide all the required tools. Otherwise, tools will have to be installed manually.

1. Clone the repository
```bash
git clone https://github.com/her3ticAVI/Wifi-Forge
```
2. Run setup.sh
```bash
cd Wifi-Forge/Framework/materials
sudo ./setup.sh
```

2. Run Wi-Fi Forge
```bash
cd ..
sudo python3 WifiForge.py
```

## Labs and Featured Tools
Wi-Fi Forge provides pre-built labs that cover the following:

- Evil twin AP
- WEP PIN Recovery
- WPA2 4 Way Handshake
- WPS Pixie Attacks
- WifiPhisher
- Eaphammer
- etc...

## Common Issues
### Xterm does not work!
Intializing graphical interfaces as root between the docker image and host machine is restricted on most modern distributions. Run the following command to provide the appropriate permissions - 
```bash
xhost si:localuser:root
```
If other issues are encountered, start a thread in the issues section of the repo! :) 

### Dockerfile stops at apt update!
Once in a while, the dockerfile will fail before installing packages. Though unconfirmed, this error usually occurs after running Wifi-forge (either on baremetal or within a docker). Rebooting and running the Dockerfile again typically solves the issue. 

## Links and Further Reading 
- https://mininet-wifi.github.io/ 
- [https://www.hackingarticles.in/wireless-penetration-testing-pmkid-attack/](https://www.hackingarticles.in/wireless-penetration-testing-pmkid-attack/)
- [https://en.wikipedia.org/wiki/IEEE_802.11i-2004](https://en.wikipedia.org/wiki/IEEE_802.11i-2004)
- [https://www.wildwesthackinfest.com](https://www.wildwesthackinfest.com)
- [https://nmap.org/](https://nmap.org/)
- [https://en.wikipedia.org/wiki/Situation_awareness](https://en.wikipedia.org/wiki/Situation_awareness)
- [https://www.educba.com/linux-network-manager/](https://www.educba.com/linux-network-manager/)
- [https://www.aircrack-ng.org/](https://www.aircrack-ng.org/)
- [https://www.aircrack-ng.org/doku.php?id=airodump-ng](https://www.aircrack-ng.org/doku.php?id=airodump-ng)
- [https://www.aircrack-ng.org/doku.php?id=cracking_wpa](https://www.aircrack-ng.org/doku.php?id=cracking_wpa)
- [https://charlesreid1.com/wiki/Aircrack_and_John_the_Ripper](https://charlesreid1.com/wiki/Aircrack_and_John_the_Ripper)


