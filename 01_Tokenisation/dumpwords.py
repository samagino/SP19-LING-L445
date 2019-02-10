"""
dumpwords.py:

takes a Connlu file and returns all words seperated by newlines
"""


import sys

def dumpWords(filePath):
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
            
            # word entries begin with a number in CoNLLu format
            if fields[0].isdigit() :
                # the second collumn in word entries contain the word literal
                sys.stdout.write(fields[1] + '\n')

if len(sys.argv) != 2 :
    print('error: not enough args')
    print('dumpwords needs a file to dump words from.')
    print('usage:\n\tpython dumpwords.py path/to/file')
else :
    dumpWords(sys.argv[1])
