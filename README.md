Authentication Script
=====================

This script automates logging in to IIT Mandi gateway server. It works both with python2 and python3.
You can run the scipt as an executable on Linux or Mac OSX, as './login.py'. On windows, you can run it via 'python login.py'. The prompts are self explanatory.
Killing the script via Ctrl-C or kill will log you out. This is done to ensure no unnecessary sessions are maintained.

#### Dependencies
1. The script requires that the http_proxy and https_proxy environment variables be correctly set.
2. The script depends on the python requests library. You can install it by running
``` sh
pip install --user requests
```
