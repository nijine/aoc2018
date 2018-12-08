#!/usr/bin/env python

# levenshtein distance calc via matrix - source: https://www.python-course.eu/levenshtein_distance.php
def LD(s, t, costs=(1, 1, 1)):
    rows = len(s)+1
    cols = len(t)+1
    deletes, inserts, substitutes = costs
    
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings 
    # by deletions:
    for row in range(1, rows):
        dist[row][0] = row * deletes
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for col in range(1, cols):
        dist[0][col] = col * inserts
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost) # substitution
    # for demo purposes
    #for r in range(rows):
    #    print(dist[r])
 
    return dist[row][col]

ids = []

with open('input') as f:
    for line in f:
        ids.append(line[:-1])

counter = 0
id1 = ""
id2 = ""

for i in ids:
    counter += 1
    ids_comp = ids[counter:]

    if len(ids_comp) > 0:
        for j in ids_comp:
            print("Comparing:", i, j)
            dist = LD(i, j)
            
            if dist == 1:
                id1 = i
                id2 = j
                break

    if len(id1) > 0:
        break

print("ID 1: %s" % id1)
print("ID 2: %s" % id2)
