from mininet.term import makeTerm
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mn_wifi.net import Mininet_wifi
from WifiForge import print_banner
import os

def WPS_Pixie_attack():
    net = Mininet_wifi()

    print("Creating nodes...")
    attacker = net.addStation('a', encrypt='wpa2')
    host1 = net.addStation('host1', encrypt='wpa2')
    ap1 = net.addAccessPoint('ap1', ssid="secure_wifi", mode="g", channel="1",
                             passwd='123456789a', encrypt='wpa2',
                             failMode="standalone", datapath='user', wps_state='2',
                             config_methods='label display push_button keypad')

    print("Configuring nodes...")
    net.configureNodes()

    print("Associating Stations...")
    net.addLink(attacker, ap1)
    net.addLink(host1, ap1)

    print("Starting network...")
    net.build()
    ap1.start([])


    ap1.cmd('hostapd_cli -i ap1-wlan1 wps_ap_pin set 12345670')
    attacker.cmd('iw dev a-wlan0 interface add mon0 type monitor')
    attacker.cmd('ip link set mon0 up')
    makeTerm(attacker)  #reaver -i mon0 -b 02:00:00:00:02:00 -vv

    print_banner()
    print("\n")
    print('                      +-_-_-_- WPS pixie attack started Sucessfully -_-_-_-+')
    print('                             Type "xterm a" and press enter to begin')
    print('                            Type exit when the simulation is completed\n')

    CLI(net)

    net.stop()
    exit()