#!/usr/bin/env python
# Part 1

from sys import exit

frequency = int(0)
changes = []
results = []

with open('input') as i:
    for line in i:
        changes.append(int(line))

results.append(frequency)

for c in changes:
    frequency += c
    results.append(frequency)

print "Resulting change: ", frequency

# Part 2

while True:
    for c in changes:
        frequency += c
        if frequency in results:
            print "duplicate found: ", frequency
            exit(0)

print "no duplicates found"
