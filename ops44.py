#!/usr/bin/python3

# Dom Moore
# ops challenge 44
# 12/7/20

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = socket.getdefaulttimeout() # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input('Enter IP Address: \n ')# TODO: Collect a host IP from the user.
portno = int(input('Enter Port Number: \n '))# TODO: Collect a port number from the user, then convert it to an integer data type.






def portScanner(portno):
    if sockmod.connect((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)