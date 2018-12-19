#!/usr/bin/env python
# Part 1


def readInput():
    i = ""    

    with open('input') as f:
        i = f.read()

    return i


def react(input_string):
    # debug
    #print "Starting string length:", len(input_string) - 1  # account for '\0'
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

    # debug
    #print "Final string:", input_string, "Length:", len(input_string) - 1
    return input_string


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


def getLargest(input_dict):
    max_value = -1
    max_item = ""

    for k, v in input_dict.items():
        if v > max_value:
            max_value = v
            max_item = k

    return (max_item, max_value)


# this only works if char is passed in upper case
def removeChar(input_text, char):
    output_text = input_text

    # debug
    #print "Char to remove:",  char
    #print "Pre-removal string length:", len(output_text) - 1

    output_text = output_text.replace(char, "")
    output_text = output_text.replace(chr(ord(char) + 32), "")  # lower case

    # debug
    #print "Post-removal string length:", len(output_text) - 1

    return output_text


# Strategy 1
#if __name__ in "__main__":
#    # find most common letter
#    input_text = readInput()
#    most_common = getLargest(getCounts(input_text))
#    print "Most common:", most_common[0], "Occurrences:", most_common[1]
#
#    # remove that letter
#    input_text = removeChar(input_text, most_common[0])
#
#    # run react
#    output_text = react(input_text)
#
#    print "Reacted string length:", len(output_text) - 1


# Strategy 2 (brute force)
if __name__ in "__main__":
    input_text = readInput()
    print "Input size:", len(input_text) - 1

    sizes = []

    for c in xrange(ord('A'), ord('Z') + 1):
        temp_text = removeChar(input_text, chr(c))
        temp_text = react(temp_text)
        # debug
        print "Removed:", chr(c), "Output size:", len(temp_text) - 1
        sizes.append(len(temp_text) - 1)

    print "Smallest size:", min(sizes)
