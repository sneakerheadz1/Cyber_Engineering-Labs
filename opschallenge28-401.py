#!/usr/bin/env python3


# Script Name               ops401 challange 27 
# Author                    Dom Moore
# Date                      11/10/20
# Description of purpose    Event Logging too P2


# Import Libraries
import time
import cryptPass
import logging
from logging.handlers import RotatingFileHandler
import glob


# Declare Variable

pass_wd = input('Enter your Password: \n')
file_path = "/home/ubuntu/Desktop/passwd.txt"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# roll to new file after 2KB, keep backup logs
# handler = RotatingFileHandler('pass.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

### set logger handler
logName = 'pass_log'
myLogger =logging.getLogger()
myLogger.setLevel(logging.INFO)
handler = logging.handles.RotatingFileHandler('pass.log', maxBytes=2000, backupCount=5)
myLogger.addHandler(handler)

###

# intentional rollover

handler.doRollover()


# retrieve files
logFile = glob.glob ('%s*' % logName)

for names in logFile:
    print(names)



# Define Function

def usr_wrd(): # validate password is correct
        print('Enter password')
        ps_wrd = input()
        try:
            ps_wrd = str(ps_wrd)
        except:
            print('Enter correct password ')

        if ps_wrd == pass_wd:
            print("Password valid")
        else:
            print("Password incorrect, Enter correct password! ")


logging.basicConfig(filename='file_log.txt', level=logging.INFO)
def main_pw():
    passFile = open('passwd.txt', 'r+')
    for line in passFile.readlines():
        if " " in line:
            user = line.split(';')[1]
            cyptyPass = line.split(':')[2].strip(' ')
            time.sleep(2)
            print('[*]', +user)
            testPass(cryptPass, passwd.txt)

            try:
                s.login(ipAddress, user, cyptyPass)
                login.info('Password', + cryptPass)
                break
            except cryptPass.Exception as e:
                logging.info(e)
                print('login failed')
                print(e)
    loggin.info('Finished')




# Declare functions


