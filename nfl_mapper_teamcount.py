#!/usr/bin/env python
import sys

patriotsArr = ["patriots", "@patriots", "#patriots", "#newenglandpatriots", "pats", "#pats"]
falconsArr = ["falcons", "@falcons", "#falcons", "#atlantafalcons"]

for line in sys.stdin:
    line = line.strip()
    # skip if tweet is from different day or if from AM
    if "PM - 5 Feb 2017" not in line:
        continue

    words = line.split()

    patriots = 0
    falcons = 0
    # check if tweet mentions a team
    for word in words:
        if word.lower() in patriotsArr:
            patriots += 1
        if word.lower() in falconsArr:
            falcons += 1

    team = ""
    # skip tweet if neither team is mentioned
    if falcons == 0 and patriots == 0:
        continue
    # check if both teams are mentioned
    elif falcons > 0 and patriots > 0:
        team = "both"
    elif falcons > 0 and patriots == 0:
        team = "falcons"
    elif falcons == 0 and patriots > 0:
        team = "patriots"

    time = words[0]
    # check if time value is valid
    if ":" not in time:
        continue

    hour, minutes = time.split(":")
    # convert values to intergers
    try:
        hour = int(hour)
        minutes = int(minutes)
    except ValueError:
        continue

    timeFrame = "" # if tweet is from first half of the game or second half
    if hour <= 7 and minutes < 48:
        timeFrame = "first"
    else:
        timeFrame = "second"

    # create tuple containing the time and team
    timeTeam = (timeFrame, team)

    print timeTeam,"\t",1
