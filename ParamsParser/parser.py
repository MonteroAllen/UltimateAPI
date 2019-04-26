#!python

import requests
import re
import itertools

# <tr>(.*?)<\/tr>
weigthUrl = "http://kuroganehammer.com/Ultimate/Weight"
response = requests.get(weigthUrl)

entries = re.findall(r"<tr>(.*?)<\/tr>", response.text, re.MULTILINE | re.DOTALL)

cleaned = []
for entry in entries:
  cleaned.append(re.sub(r'<(.*?)>', ';', entry.replace('\t', '').replace('\n', ''), count=15, flags=(re.MULTILINE | re.DOTALL)))

cleaned.pop(0)
cleaned.pop(0)

weightDict = {}
for clean in cleaned:
  singleColumn = ''.join(ch for ch, _ in itertools.groupby(clean))
  charEntry = singleColumn.split(';')
  if (len(charEntry) > 3):
    weightDict[charEntry[2]] = charEntry[3]

print(weightDict)