#!/usr/bin/python3

# Dom Moore
# ops challenge 45
# 12/8/20


import socket

def bannergrab(host, port):
    timeout = 50 #TODO: Set a timeout value.
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockmod.connect((host,port)) #TODO: Insert the correct `socket` function name here that accepts the host IP, then port number as parameters.
    sockmod.settimeout(timeout)
    print(sockmod.recv(1024))

def main():
    host = input('Enter your IP Address: \n')  #TODO: Prompt the user to type an IP.
    port = int(input('Enter ypur Port number: \n'))  #TODO: Prompt the user to type a port number that we'll convert to a "string" data type.
    bannergrab(host, port)

main()