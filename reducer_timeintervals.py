#!/usr/bin/env python
from operator import itemgetter
import sys


current_interval = None
current_count = 0
time_interval= None

for line in sys.stdin:
    line = line.strip()
    time_interval, count = line.split("\t")

    try:
        count = int(count)
        time_interval = int(time_interval)
    except ValueError:
        continue


    if current_interval == time_interval:
        current_count += count
    else:
        if current_interval:
            print current_interval,"\t",current_count

        current_count = count
        current_interval = time_interval

# print the last time interval
if current_interval == time_interval:
    print current_interval,"\t",current_count
