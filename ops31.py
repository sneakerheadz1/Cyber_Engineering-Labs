#!/usr/bin/env python3


# Script Name               ops challange-401 31
# Author                    Dom Moore
# Date                      11/16/20
# Description of purpose    Antivirus p1


# Import Libraries
import os
import subprocess
from subprocess import call
from subprocess import check_output

# variable 

#fileName = input("Enter the name of your file \n")
#dirName = input(" Enter the Directory path \n")
dirName = "/home/ubuntu/Documents/python"

def listDir(dir):
    fileNames= os.listdir(dir)
    for fileName in fileNames:
        print("File Name: " + fileName)
        print( "Folder Path: " +os.path.abspath(os.path.join(dir, fileName)), sep="\n")


    


if __name__ == "__main__":
    listDir(dirName)
