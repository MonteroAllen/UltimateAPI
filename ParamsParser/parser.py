#!python

import requests
import re

weigthUrl = "http://kuroganehammer.com/Ultimate/Weight"
runSpeedUrl = "http://kuroganehammer.com/Ultimate/RunSpeed"
walkSpeedUrl = "http://kuroganehammer.com/Ultimate/WalkSpeed"
airSpeedUrl = "http://kuroganehammer.com/Ultimate/AirSpeed"
airAccelUrl = "http://kuroganehammer.com/Ultimate/AirAcceleration"
fallSpeedUrl = "http://kuroganehammer.com/Ultimate/FallSpeed"
initDashUrl = "http://kuroganehammer.com/Ultimate/DashSpeed"

def createDict(cleanList, valueCol=3):
  weightDict = {}
  for clean in cleanList:
    singleColumn = clean.replace(';;', ';')
    for ch in clean:
      singleColumn = singleColumn.replace(';;', ';')
    charEntry = singleColumn.split(';')
    if (len(charEntry) > 3):
      if charEntry[2] == "Dedede":
        charEntry[2] = "King Dedede"
      if charEntry[2] == "Dank Samus":
        charEntry[2] = "Dark Samus"
      if charEntry[2] == "Mii Swordspider":
        charEntry[2] = "Mii Swordfighter"
      if charEntry[2] == "Educated Mario" or charEntry[2] == "Dr Mario":
        charEntry[2] = "Dr. Mario"
      if charEntry[2] == "Pit, but edgy":
        charEntry[2] = "Dark Pit"
      if charEntry[2] == "Popo":
        charEntry[2] = "Ice Climbers"
      if charEntry[2] == "M. Game & Watch":
        charEntry[2] = "Mr. Game & Watch"
      weightDict[charEntry[2]] = charEntry[valueCol]
  return weightDict

def parseResponse(responseText):
  tbody = re.findall(r"<tbody>(.*?)<\/tbody>", responseText, re.MULTILINE | re.DOTALL)
  entries = re.findall(r"<tr>(.*?)<\/tr>", tbody[0], re.MULTILINE | re.DOTALL)
  cleaned = []
  for entry in entries:
    cleaned.append(re.sub(r'<(.*?)>', ';', entry.replace('\t', '').replace('\n', ''), count=15, flags=(re.MULTILINE | re.DOTALL)))
  return cleaned

if __name__ == "__main__":
  ########################## Weight #################################
  weightresponse = requests.get(weigthUrl)
  weightcleaned = parseResponse(weightresponse.text)
  weightDict = createDict(weightcleaned)
  # print(weightDict)
  ######################### RunSpeed ################################
  runSpeedResponse = requests.get(runSpeedUrl)
  runSpeedCleaned = parseResponse(runSpeedResponse.text)
  runSpeedDict = createDict(runSpeedCleaned)
  # print(runSpeedDict)
  ######################## WalkSpeed ###############################
  walkSpeedResponse = requests.get(walkSpeedUrl)
  walkSpeedCleaned = parseResponse(walkSpeedResponse.text)
  walkSpeedDict = createDict(walkSpeedCleaned)
  # print(walkSpeedDict)
  ######################## AirSpeed ###############################
  airSpeedResponse = requests.get(airSpeedUrl)
  airSpeedCleaned = parseResponse(airSpeedResponse.text)
  airSpeedDict = createDict(airSpeedCleaned)
  # print(airSpeedDict)
  #################### Air Accceleration ###########################
  airAccelResponse = requests.get(airAccelUrl)
  airAccelCleaned = parseResponse(airAccelResponse.text)
  airAccelDict = createDict(airAccelCleaned, 5)
  # print(airAccelDict)
  ####################### Fall Speed ##############################
  fallSpeedResponse = requests.get(fallSpeedUrl)
  fallSpeedCleaned = parseResponse(fallSpeedResponse.text)
  fallSpeedDict = createDict(fallSpeedCleaned)
  # print(fallSpeedDict)
  ################### Initial Dash Speed ##########################
  initDashResponse = requests.get(initDashUrl)
  initDashCleaned = parseResponse(initDashResponse.text)
  initDashDict = createDict(initDashCleaned)
  # print(initDashDict)
  #################### Rest of the code ###########################
  finalDict = {}
  for character in weightDict.keys():
    finalDict[character] = [weightDict[character], runSpeedDict[character], walkSpeedDict[character], airSpeedDict[character], airAccelDict[character], fallSpeedDict[character], initDashDict[character]]
  print(finalDict)