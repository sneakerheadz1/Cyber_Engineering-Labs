#!/usr/bin/env python3


# Script Name               ops challange-401 31
# Author                    Dom Moore
# Date                      11/17/20
# Description of purpose    Antivirus p2


# Import Libraries
import os
import subprocess
from subprocess import call
from subprocess import check_output
import hashlib


# variable 
dirName = "/home/ubuntu/Documents/python"	
fileHash = hashlib.md5()

# Function

def listDir(dir):
    fileNames= os.listdir(dir)
    for fileName in fileNames:
        print("File Name: " + fileName)
        print( "Folder Path: " +os.path.abspath(os.path.join(dir, fileName)), sep="\n")
    with open('passwd.txt', 'rb') as afile:
        buf = afile.read()
        fileHash.update(buf)
        print(fileHash.hexdigest())
        print(fileName.hexdigest())

if __name__ == "__main__":
    listDir(dirName)
    print(fileHash.hexdigest())
