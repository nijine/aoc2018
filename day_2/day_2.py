#!/usr/bin/env python

ids = []
counts = dict()
counts[2] = 0
counts[3] = 0

with open('input') as f:
    for line in f:
        ids.append(str(line))

for i in ids:
    ref = dict()

    for c in i:
        if c not in ref:
            ref[c] = 1
        else:
            ref[c] = ref[c] + 1

    #print(ref)

    local_counts = dict()
    local_counts[2] = 0
    local_counts[3] = 0

    for v in ref.itervalues():
        #print(v)
        if v is 2:
            local_counts[2] = local_counts[2] + 1
        elif v is 3:
            local_counts[3] = local_counts[3] + 1

    if local_counts[2] > 0:
        counts[2] = counts[2] + 1
    
    if local_counts[3] > 0:
        counts[3] = counts[3] + 1

print(counts)
print('checksum: %s' % (counts[2] * counts[3]))
