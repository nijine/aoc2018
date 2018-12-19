#!/usr/bin/env python
# Part 1

input_string = ""

with open('input') as f:
    input_string = f.read()

# actual number of characters is 1 less than len(string) (excludes the \0)
print "Starting string length:", len(input_string) - 1

changesMade = True

while changesMade:
    changesMade = False
    for i in xrange(1, len(input_string) - 1):
        if i - 1 >= 0 and len(input_string) > i:
            if abs(ord(input_string[i-1]) - ord(input_string[i])) == 32:
                # this pair gets removed
                if i + 1 == len(input_string):
                    input_string = input_string[:i-1]
                else:
                    input_string = input_string[:i-1] + input_string[i+1:]
                changesMade = True

print "Final string:", input_string, "Length:", len(input_string) - 1
