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

# assemble "sleep map"
for time, info in sorted_records.items():
    log = info.split(" ")

    if "Guard" in log:
        if "begins" in log:
            current_guard = log[1]

            if current_guard not in sleep_map.keys():
                sleep_map[current_guard] = dict()

    if "falls" in log:
        start_time = time

    if "wakes" in log:
        start_minute = start_time.minute
        end_minute = time.minute - 1

        for m in range(start_minute, end_minute):
            if m not in sleep_map[current_guard]:
                sleep_map[current_guard][m] = 1
            else:
                sleep_map[current_guard][m] = sleep_map[current_guard][m] + 1

# find the sleepiest guard
sleepiest_guard = ""
max_slept_time = -1

for guard, time_map in sleep_map.items():
    total_sleep = sum(time_map.values())
    if total_sleep > max_slept_time:
        max_slept_time = total_sleep
        sleepiest_guard = guard

print "Sleepiest guard:", sleepiest_guard
print "Time spent sleeping:", max_slept_time

max_slept_time = -1
target_minute = 0

for minute, time_spent in sleep_map[guard].items():
    if time_spent >= max_slept_time:
        max_slept_time = time_spent
        target_minute = minute

print "Slept most during minute:", target_minute

# generate checksum
checksum = int(sleepiest_guard[1:]) * int(target_minute)

print "Checksum:", checksum

# alternative calculation
# find the guard that slept the most on a given minute

sleepiest_minute = 0
max_slept_time = 0

for guard, time_map in sleep_map.items():
    for minute, sleep_time in time_map.items():
        if sleep_time >= max_slept_time:
            max_slept_time = sleep_time
            sleepiest_minute = minute
            sleepiest_guard = guard

print "Alternative sleepiest guard:", sleepiest_guard
print "Alternative sleepiest minute:", sleepiest_minute
print "Time spent:", max_slept_time

# checksum
checksum = int(sleepiest_guard[1:]) * int(sleepiest_minute)

print "Checksum:", checksum
