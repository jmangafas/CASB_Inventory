#!/usr/bin/env python
# Jim Mangafas - HGEN inventory Zone 4

#import libs
from netmiko import Netmiko
from netmiko import NetmikoTimeoutException

iplist = open('iplist.txt', mode='r')
data = open('data.txt', mode='a')

for device in iplist:
    try:
        cisco = {
            "host": device,
            "username": "didata",
            "password": "D@rliNGP@rk1@3$",
            "device_type": "cisco_ios",
        }
        net_connect = Netmiko(**cisco)
        hostname = (net_connect.find_prompt())
        output = net_connect.send_command("show inventory", use_textfsm=True)
        # data.write('\n' + str(output) + '\n')
        # print(output[0].get('pid'), output[0].get('sn'))
        data.write(hostname[0:23] + ',' + output[0].get('pid') + ',' + output[0].get('sn') + '\n')
        data.write(hostname[0:23] + ',' + output[2].get('pid') + ',' + output[2].get('sn') + '\n')
        data.write(hostname[0:23] + ',' + output[3].get('pid') + ',' + output[3].get('sn') + '\n')
        data.write(hostname[0:23] + ',' + output[4].get('pid') + ',' + output[4].get('sn') + '\n')
        data.write(hostname[0:23] + ',' + output[5].get('pid') + ',' + output[5].get('sn') + '\n')

    except (NetmikoTimeoutException):
        print(f'unable to connect to {cisco} device')

#close both data files
iplist.close()
data.close()
