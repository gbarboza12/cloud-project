#!/usr/bin/env python
from operator import itemgetter
import sys

countsDict = {"cubs": 0, "indians":0, "both":0}
currentTime = None
currentCount = 0
currentTeam = None

for line in sys.stdin:
    line = line.strip()
    timeTeam, count = line.split("\t")
    time, team = timeTeam.split(",")

    # remove surrounding punctuation
    time = time[2:-1]
    team = team[2:-3]

    try:
        count = int(count)
    except ValueError:
        continue

    if currentTime == time:
        if currentTeam:
            countsDict[currentTeam] += count
            currentTeam = team
    else:
        if currentTime:
            countsDict[currentTeam] += count
            print currentTime,
            # write result to STDOUT
            for k,v in countsDict.items():
                print v,
            print ""

        currentTime = time
        currentTeam = team
        countsDict = {"cubs": 0, "indians":0, "both":0}

# print the last time frame
if currentTime== time:
    countsDict[currentTeam] += count
    print currentTime,
    # write result to STDOUT
    for k,v in countsDict.items():
        print v,
    print ""
