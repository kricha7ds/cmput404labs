# Lab 1: Setup virtualenv and understand basic usage of curl.
import requests

# Print out the version of the requests library
print(requests.__version__)

# Modify the script to GET the Google homepage.
URL = "http://www.google.com/"
r = requests.get(URL)
print(r)

# Download scrip from GitHub and print out source code.
gitURL = "https://github.com/kricha7ds/cmput404labs/blob/main/lab1.py"
r = requests.get(gitURL, allow_redirects=True)
print(r.text)