#!/usr/bin/env python
"""
A simple python script to automate IIT Mandi Gateway Authentication
Author : Abhishek Pandey, Sahil Arora, Shikhar Gupta
"""
from __future__ import print_function
import getpass
import signal
import sys
import time
import requests

if sys.version_info[0] < 3:
    input = raw_input


def main():
    """
    This function does pretty much everything.
    """
    client = requests.session()
    gateways = ['stgw.iitmandi.ac.in/ug', 'gateway.iitmandi.ac.in/facstaff']
    auths = ['https://' + url + '/authenticate.php' for url in gateways]
    logouts = ['http://' + url + '/logout.php' for url in gateways]
    success_urls = ['http://' + url + '/success.php' for url in gateways]
    print("Please Choose your proxy server")
    for i, auth in enumerate(auths):
        print("[{}] {}".format(i + 1, auth))
    ans = input().strip()
    if ans not in ('1', '2'):
        print("Only 1 or 2 accepted as answers")
        return
    ans = int(ans) - 1
    auth = auths[ans]

    def logout(signal, frame):
        """
        SIGINT handler. Is run on Ctrl-C or kill by User
        Logs out the user.
        """
        print("Logging Out")
        client.get(logouts[ans])
        sys.exit(0)

    signal.signal(signal.SIGINT, logout)
    print("Username: ")
    user = input()
    passwd = getpass.getpass()
    resp = client.post(auth, dict(username=user, password=passwd, url=""))
    email = "{}@students.iitmandi.ac.in".format(user)
    if email in resp.text:
        print("Login Successful")
    else:
        print("Login Failed. Please try again")
        return
    while True:
        time.sleep(20 * 60)
        client.get(success_urls[ans])


if __name__ == '__main__':
    main()
