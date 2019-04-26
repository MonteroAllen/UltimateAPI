#!python

import requests
import re
import itertools

def createDict(cleanList):
  weightDict = {}
  for clean in cleanList:
    singleColumn = ''.join(ch for ch, _ in itertools.groupby(clean))
    charEntry = singleColumn.split(';')
    if (len(charEntry) > 3):
      weightDict[charEntry[2]] = charEntry[3]
  return weightDict

def parseResponse(responseText):
  entries = re.findall(r"<tr>(.*?)<\/tr>", responseText, re.MULTILINE | re.DOTALL)
  cleaned = []
  for entry in entries:
    cleaned.append(re.sub(r'<(.*?)>', ';', entry.replace('\t', '').replace('\n', ''), count=15, flags=(re.MULTILINE | re.DOTALL)))
  cleaned.pop(0)
  cleaned.pop(0)
  return cleaned

if __name__ == "__main__":
  weigthUrl = "http://kuroganehammer.com/Ultimate/Weight"
  response = requests.get(weigthUrl)
  cleaned = parseResponse(response.text)
  weightDict = createDict(cleaned)
  print(weightDict)