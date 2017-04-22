#!/usr/bin/env python
import sys

indiansArr = ["indians", "@indians", "#indians"]
cubsArr = ["cubs", "@cubs", "#cubs"]

for line in sys.stdin:
    line = line.strip()
    # skip if tweet is from different day or if from AM
    if "PM - 5 Feb 2017" not in line:
        continue

    words = line.split()

    indians = 0
    cubs = 0
    # check if tweet mentions a team
    for word in words:
        if word.lower() in indiansArr:
            indians += 1
        if word.lower() in cubsArr:
            cubs += 1

    team = ""
    # skip tweet if neither team is mentioned
    if cubs == 0 and indians == 0:
        continue
    # check if both teams are mentioned
    elif cubs > 0 and indians > 0:
        team = "both"
    elif cubs > 0 and indians == 0:
        team = "cubs"
    elif cubs == 0 and indians > 0:
        team = "indians"

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
    if hour <= 9 and minutes < 25:
        timeFrame = "first"
    else:
        timeFrame = "second"

    # create tuple containing the time and team
    timeTeam = (timeFrame, team)

    print timeTeam,"\t",1
