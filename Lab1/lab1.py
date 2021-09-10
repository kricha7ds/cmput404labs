# Lab 1: Setup virtualenv and understand basic usage of curl.
import requests

# Print out the version of the requests library
print(requests.__version__)

# Modify the script to GET the Google homepage.
URL = "http://www.google.com/"
r = requests.get(URL)
print(r)

# Download script from GitHub and print out source code.
gitURL = "https://raw.githubusercontent.com/kricha7ds/cmput404labs/main/Lab1/lab1.py"
r = requests.get(gitURL, allow_redirects=True)
print(r.text)

# Access code on GitHub via this link:
# https://github.com/kricha7ds/cmput404labs/blob/main/Lab1/lab1.py