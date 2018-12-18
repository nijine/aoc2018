#!/usr/bin/env python
# Part 1

test_string = 'aAbBccDd'
last = ''
final = ''

# testing
#for s in test_string:
#    if last in '':
#        last = s
#        continue
#
#    print "Difference between", s, last, abs(ord(s) - ord(last))
#    last = s

print "Starting string:", test_string

for i in xrange(1, len(test_string)):
    if i - 1 >= 0 and i + 1 < len(test_string):
        if abs(ord(test_string[i-1]) - ord(test_string[i])) == 32:
            # this pair gets removed
            test_string = test_string[:i-1] + test_string[i+1:]

print "Final string:", test_string

# on the right track, just need to continue making changes until there aren't any changes left to make
