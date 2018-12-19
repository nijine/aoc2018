#!/usr/bin/env python
# Part 1


def readInput():
    i = ""    

    with open('input') as f:
        i = f.read()

    return i


def react(input_string):
    print "Starting string length:", len(input_string) - 1  # account for '\0'
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


#if __name__ in "__main__":
#    react(readInput())    


# Part 2
# count to see which polymer unit is most prevalent
def getCounts(input_string):
    counts = dict()

    for a in xrange(ord('A'), ord('Z') + 1):
        counts[chr(a)] = input_string.count(chr(a))
        counts[chr(a)] += input_string.count(chr(a + 32))  # count lowercase

    return counts


if __name__ in "__main__":
    print getCounts(readInput())
