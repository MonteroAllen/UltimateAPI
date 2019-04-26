#!python

import requests
import re

# <tr>(.*?)<\/tr>
url = "http://kuroganehammer.com/Ultimate/Weight"
response = requests.get(url)

entries = re.findall(r"<tr>(.*?)<\/tr>", response.text, re.MULTILINE | re.DOTALL)

cleaned = []
for entry in entries:
  cleaned.append(re.sub(r'<(.*?)>', ';', entry.replace('\t', '').replace('\n', ''), count=15, flags=(re.MULTILINE | re.DOTALL)))

print(cleaned)