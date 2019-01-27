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
    SAMPLE_SIZE = 1024
    dictionary = set()

    # open dictionary file
    with open(filePath, "r") as f:

        sample = f.read(SAMPLE_SIZE)
        while sample:

            # split sample into lines
            sample = sample.split('\n')
            # word entries begin with a number in CoNLLu format
            if sample[0].isdigit() and len(sample[1]) > 1 and not sample[1].isdigit():
                # the second collumn in word entries contain the word literal
                dictionary.add(sample[1])

            sample = f.read(SAMPLE_SIZE)



def maxMatch(sentence, dictionary):
    if len(sentence) == 0:
        return "" # or some other empty list

    # reversed, so start at end of sentence and work back
    for i in reversed(range(2, len(sentence) - 1)):
        # first i chars in sentence
        firstword = sentence[0 : i]
        # rest of chars in sentence
        remainder = sentence[i+1 : len(sentence)]

        # TODO somehow make this not recursive
        if firstword in dictionary or firstword.isdigit():
            return firstword + '\n' + maxMatch(remainder, dictionary)

    # also this one
    return firstword + maxMatch(remainder, dictionary)


dictionary = makeDictionary(argv[1])
# dunno if I should align samples with sentece boundaries
SAMPLE_SIZE = 1024

sample = sys.stdin.read(SAMPLE_SIZE)
while sample:
    # assume input has been segmented
    sentences = sample.split('\n')

    for sentence in sentences:
        sys.stdout.write(maxMatch(sentence, dictionary) + '\n')

    sample = stdin.read(SAMPLE_SIZE)
