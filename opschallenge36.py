#!/usr/bin/env python3


# Script Name               ops challange 36
# Author                    Dom Moore
# Date                      11/23/20
# Description of purpose    web fingerprint p1


# Import Libraries
import socket
import telnetlib

# Variables 

ipAdd = input('Enter your IP Address: \n')
port = str(input('Enter your Port number: \n'))



def main(ipAdd,port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    tn = telnetlib.Telnet(ipAdd)
    print(str(s.recv(1024)).strip('b'))


main()


resource: https://www.pythonforbeginners.com/code-snippets-source-code/python-using-telnet