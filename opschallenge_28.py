#!/usr/bin/env python3


# Script Name               ops challange-401 28
# Author                    Dom Moore
# Date                      11/11/20
# Description of purpose    Logging tool p3 Handlers


# Import Libraries
from scapy import all
from scapy import ICMP, IP, sr1, TCP, sr
import random
from ipaddress import IPv4Network
import logging
import ops_scapy

# creating loggers
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# setting format for level / timestamp 
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# create file handlers
file_handler = logging.FileHandler('pass.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# Delcare host and variable
host = "scanme.nmap.org"
port_range = [21, 22, 23, 80, 443, 3389]




def port_scan():
    for dst_port in port_range:
        scr_port = random.randint(1025,65653)
        response = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1,verbose=0,)
        
        if response is None:
            print(f" {host}:{dst_port} is filtered. ")

        elif (response.haslayer(TCP)):
            if(response.getlayer(TCP).flags == 0x12):
                # send RST to close
                send_rst = sr(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flads='R'),timeout=1, verbose=0,)

                print(f"{host}:{dst_port} is open. ")

            elif(response.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed. ")

        elif(response.haslayer(ICMP)):
            if( int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,7,10,13]):
                logger.exception('Try another Port! ')
                print(f"{host}: {dst_port} is filtred and has been dropped.")


if __name__ == "__main__":
    print(" What would you like to scan? enter 1 for port. 2 for IP ")
    response = int(input('Enter 1 or 2 to begin scan:'))

    if response == 1:
        port_scan()
        print("checking for open ports")

