#!/usr/bin/env python
# Part 1

from datetime import datetime as dt
from sortedcontainers import SortedDict as sd


records = []
ts_format = "%Y-%m-%d %H:%M"

with open('input') as f:
    for l in f:
        records.append(l[:-1])

print "First record, unsorted:", records[0]

# sort records by timestamp
# first we need a sample breakdown

# raw timestamp portion of first record
raw_dt = records[0][1:17]

print "Raw datetime:", raw_dt

# datetime object version
ts0 = dt.strptime(raw_dt, ts_format)

# make sure the above works
print "Datetime Object Interpretation:", ts0

# sort the records
sorted_records = sd()

for r in records:
    raw_dt = r[1:17]
    ts = dt.strptime(raw_dt, ts_format)

    sorted_records[ts] = r[19:]

# testing
#print "First record:", sorted_records.popitem(index=0)
#print "Last record:", sorted_records.popitem(index=-1)

sleep_map = dict()
current_guard = ""
start_time = 0
delta = 0

print '\n'

for time, info in sorted_records.items():
    log = info.split(" ")

    if "Guard" in log:
        if "begins" in log:
            current_guard = log[1]

            if current_guard not in sleep_map.keys():
                sleep_map[current_guard] = 0

    if "falls" in log:
        start_time = time

    if "wakes" in log:
        delta = (time - start_time).total_seconds() / 60

        sleep_map[current_guard] = sleep_map[current_guard] + delta

max = -1
chosen_guard = ""

for guard, time_slept in sleep_map.items():
    if time_slept > max:
        max = time_slept
        chosen_guard = guard

print "Chosen guard:", chosen_guard
print "Time slept:", max
