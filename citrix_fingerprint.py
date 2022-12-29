#!/usr/bin/env python3

import argparse
import csv
import re
import requests
import termcolor
import urllib3
from bs4 import BeautifulSoup

# Suppress SSL warning messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL to the Citrix VPN gateway")
args = parser.parse_args()

# URL to the Citrix VPN gateway
url = args.url + "/vpn/index.html"

# Download the CSV file with version hashes
response = requests.get("https://gist.githubusercontent.com/fox-srt/c7eb3cbc6b4bf9bb5a874fa208277e86/raw/20c413676b8ad8b3327040b2b3120fadc128acc1/citrix-adc-version-hashes.csv")
csv_data = response.text

# Parse the CSV file
reader = csv.reader(csv_data.splitlines(), delimiter=',')
version_hashes = {}
for row in reader:
    version_hashes[row[1]] = row[2]

# Download the HTML source of the website
response = requests.get(url, verify=False)
html = response.text

# Use BeautifulSoup to find the first <link> tag with the 'href' attribute that ends with the version hash
soup = BeautifulSoup(html, 'html.parser')
link_tag = soup.find('link', href=re.compile(r"v=[a-z0-9]{32}"))

# Extract the version hash from the 'href' attribute
if link_tag:
    version_hash = link_tag['href'].split("v=")[1]
    if version_hash in version_hashes:
        print(termcolor.colored(version_hashes[version_hash], "green"))
    else:
        print(termcolor.colored("No match found for version hash: " + version_hash, "red"))
else:
    print(termcolor.colored("No <link> tag found with a 'href' attribute ending in a version hash.", "red"))
