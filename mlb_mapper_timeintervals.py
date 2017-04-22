#!/usr/bin/env python
import sys

# returns the minute time interval that the tweet falls in
def getTimeInterval(minutes):
    if minutes >= 0 and minutes < 12:
        return 0
    elif minutes >= 12 and minutes < 24:
        return 1
    elif minutes >= 24 and minutes < 36:
        return 2
    elif minutes >= 36 and minutes < 48:
        return 3
    elif minutes >= 48 and minutes < 60:
        return 4
    # error
    else:
        return 5


for line in sys.stdin:
    line = line.strip()
    # skip line if tweet doesn't have correct date
    if "2 Nov 2016" not in line and "PM" not in line:
        continue

    words = line.split()
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

    # skip tweet if it is not between 7pm-11:50 pm
    if hour < 7 or hour > 11:
        continue

    timeInterval = ""
    minuteInteval = getTimeInterval(minutes)
    timeInterval = str(hour) + str(minuteInteval)

    # skip invalid minute interval
    if timeInterval[1] == "5":
        continue

    print timeInterval,"\t",1
