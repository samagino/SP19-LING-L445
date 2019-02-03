"""
notes: don't know how big dictionary is gonna be, has to be stored in memory, dunno
       if that's gonna be a problem
it's prolly not, the training data file is 9 MiB, so that's not that big


TODO:
thing that unpacks dictionary file
make stuff iterative, not recursive (maybe, but I guess sentences don't usually get that big)
"""

import sys

def makeDictionary(filePath):
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
            
            # word entries begin with a number in CoNLLu format
            if fields[0].isdigit() and (len(fields[1]) > 1) and (not fields[1].isdigit()):
                # the second collumn in word entries contain the word literal
                dictionary.add(fields[1])

    return dictionary

# [string, set] -> string
# take tokenized sentence and dictionary,
# return tokenized words in sentence split by newlines
def maxMatch(sentence, dictionary):

    # base case for recursion
    if len(sentence) < 2:
        return "" # empty list of type string

    # reversed, so start at end of sentence and work back
    for i in reversed(range(2, len(sentence) - 1)):
        # first i chars in sentence
        firstword = sentence[0 : i]

        # rest of chars in sentence
        remainder = sentence[i : len(sentence)]

        # TODO somehow make this not recursive
        if (firstword in dictionary) or (firstword.isdigit()):
            return firstword + '\n' + maxMatch(remainder, dictionary)

        # also this one
        if i == 2:
            return firstword + maxMatch(remainder, dictionary)


dictionary = makeDictionary(sys.argv[1])

sample = sys.stdin.read()
# assume input has been segmented
sentences = sample.split('\n')

for sentence in sentences:
    tokens = maxMatch(sentence, dictionary)
    sys.stdout.write(tokens + '\n')
    
