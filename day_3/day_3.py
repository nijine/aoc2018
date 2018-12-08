#!/usr/bin/env python
# Part 1

import numpy as np


def decode(entry):
    pieces = entry.split(' ')
    cord = pieces[2][:-1].split(',')
    size = pieces[3].split('x')
    decoded = cord + size
    decoded = [ int(x) for x in decoded ]

    return decoded


print "Day 3"

claims = []
max_x = 0
max_y = 0
min_x = 0
min_y = 0

with open('input') as f:
    for l in f:
        claims.append(l[:-1])

min_x = decode(claims[0])[0]
min_y = decode(claims[0])[1]

print "Min X first assignment: ", min_x
print "Min Y first assignment: ", min_y

print "# of Claims: ", len(claims)
print "First claim details: ", decode(claims[0])

details = list(list())

for c in claims:
    d = decode(c)
    x = d[0] + d[2]
    y = d[1] + d[3]
    details.append(d)

    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y

    x = d[0]
    y = d[1]

    if x < min_x:
        min_x = x

    if y < min_y:
        min_y = y

print "Details 0: ", details[0]
print "Details 0,0: ", details[0][0]

print "Max X: ", max_x
print "Max Y: ", max_y
print "Min X: ", min_x
print "Min Y: ", min_y

fabric = np.zeros((max_x, max_y))

print "Fabric array initialized: \n", fabric

for d in details:
    max_x = d[0] + d[2]
    max_y = d[1] + d[3]

    for dx in xrange(d[0], max_x):
        for dy in xrange(d[1], max_y):
            fabric[dx][dy] = fabric[dx][dy] + 1

overlap = 0

for f in fabric:
    for fx in f:
        if fx > 1:
            overlap += 1

print "Overlap: ", overlap

# Part 2

found = False
unique = []

for d in details:
    x = d[0]
    y = d[1]
    w = d[2]
    h = d[3]

    found = True

    for fx in xrange(x, x + w):
        if found:
            for fy in xrange(y, y + h):
                if fabric[fx][fy] > 1:
                    found = False
                    break

    if found:
        unique = d
        break

for c in claims:
    d = decode(c)

    if d == unique:
        print "Unique claim: ", c
