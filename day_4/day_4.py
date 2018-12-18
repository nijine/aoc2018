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
        end_minute = time.minute #  originally tried this value minus 1 but for some reason that didn't yield the right answer

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

max_slept_minute = -1
max_slept_time = -1

for minute, time_spent in sleep_map[sleepiest_guard].items():
    if time_spent >= max_slept_time:
        max_slept_time = time_spent
        max_slept_minute = minute

print "Minute slept the most:", max_slept_minute

print "Checksum:", int(sleepiest_guard[1:]) * max_slept_minute


# Part 2
print "\n"


# find the guard asleep the most on a given minute

max_time_spent = -1
minute_slept_on = -1
target_guard = ""

for guard, time_map in sleep_map.items():
    for minute, time_spent in time_map.items():
        if time_spent > max_time_spent:
            max_time_spent = time_spent
            minute_slept_on = minute
            target_guard = guard

print "Guard", target_guard, "spent a lot of time sleeping during minute", minute_slept_on
print "Checksum:", int(target_guard[1:]) * minute_slept_on
