#!/usr/bin/env python3


# Script Name               ops challange 37
# Author                    Dom Moore
# Date                      11/24/20
# Description of purpose    Cookie Capture Capades


# Import Libraries

import requests

# variable for site destination 

targetsite = "http://www.dommocreative.com"
response = requests.get(targetsite)
cookie = response.cookies

r = requests.post(targetsite, cookies=cookies)
raw = requests.get('http://www.dommocreative.com', stream=True)

print("Target site is " + targetsite)
print(cookie)




resources: https://stackoverflow.com/questions/7164679/how-to-send-cookies-in-a-post-request-with-the-python-requests-library