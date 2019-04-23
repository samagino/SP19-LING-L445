"""
notes: don't know how big dictionary is gonna be, has to be stored in memory, dunno
       if that's gonna be a problem
it's prolly not, the training data file is 9 MiB, so that's not that big


TODO:
make stuff iterative, not recursive (maybe, but I guess sentences don't usually get that big)
"""

import sys

def makeDictionary(filePath):
    # want a set because they have constant lookup time complexity in python
    #    (hash table thing)
    dictionary = set()

    # open dictionary file
    with open(filePath, "r") as f:

        sample = f.read()

        # split sample into lines
        sample = sample.split('\n')
        
        #sys.stderr.write(str(sample) + '\n')
        for line in sample:
            fields = line.split('\t')
                
            # if line is empty, continue
            if len(fields) < 2:
                continue
            
            # word entries begin with a number in CoNLLu format (first condition)
            # don't want to populate dictionary with single character words
            #    because in maxmatch we assume that if we get down to a single
            #    character, then it's a word (otherwise waste memory) (second
            #    condition)
            # don't want to populate dictionary with numbers because in maxmatch
            #    I assume all numbers are words (second condition)
            if fields[0].isdigit() and (len(fields[1]) > 1) and (not fields[1].isdigit()):
                # the second collumn in word entries contain the word literal
                dictionary.add(fields[1])

    return dictionary

# [string, set] -> string
# take tokenized sentence and dictionary,
# return tokenized words in sentence split by newlines
def maxmatch(sentence, dictionary):

    # if sentence is empty, return empty string (base case for recursion)
    if len(sentence) == 0:
        return ''

    # reversed because want to start at end of sentence and work back
    # range begins at 2 because str[0:0] is an empty string (useless to check)
    #    and str[0:1] is always a string of one character (which we always assume
    #    is a word so it's pointless search for it in the dictionary)
    # range ends at len(sentence) + 1 because len(sentence) excludes last
    #    character
    for i in reversed(range(2, len(sentence) + 1)):
        # first i characters in sentence
        firstword = sentence[0 : i]
        # remaining characters in sentence
        remainder = sentence[i : len(sentence)]

        # if firstword is in dictionary, then it's a word (first condition)
        # if firstword is a continuous string of numbers, then it's a word
        #    (second condition); note that this doesn't work for phone numbers
        #    and equations and stuff, need something more sophisticated for that
        if (firstword in dictionary) or firstword.isdigit():
            return firstword + '\n' + maxmatch(remainder, dictionary)

    firstword = sentence[0 : 1]
    remainder = sentence[1 : len(sentence)]
    return firstword + '\n' + maxmatch(remainder, dictionary)
    

if len(sys.argv) != 2 :
    print('error: not enough args')
    print('maxmatch.py needs a file make a dictionary from.')
    print('usage:\n\tpython maxmatch.py path/to/file')
    print('maxmatch.py reads the text you want to segment from stdin')
else :
    dictionary = makeDictionary(sys.argv[1])

    sample = sys.stdin.read()
    # assume input has been segmented
    sentences = sample.split('\n')

    for sentence in sentences:
        tokens = maxmatch(sentence, dictionary)
        sys.stdout.write(tokens)
    
