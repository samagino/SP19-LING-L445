"""
dumpwords.py:

takes a Connlu file and returns all words seperated by newlines
with empty lines marking sentence boundaries
"""

import sys

def dumpWords(filePath):

    # open file
    with open(filePath, "r") as f:

        sample = f.read()

        # split sample into lines
        sample = sample.split('\n')
        
        #sys.stderr.write(str(sample) + '\n')
        for line in sample:
            fields = line.split('\t')
                
            # if line is empty, continue
            if len(fields) < 2:
                sys.stdout.write('\n')
                continue
            
            # word entries begin with a number in CoNLLu format
            if fields[0].isdigit() :
                # the second collumn in word entries contain the word literal
                sys.stdout.write(fields[1] + '\n')

if len(sys.argv) != 2 :
    sys.stderr.write('error: not enough args\n')
    sys.stderr.write('dumpwords needs a file to dump words from.\n')
    sys.stderr.write('usage:\n\tpython3 dumpwords.py path/to/file\n')
else :
    dumpWords(sys.argv[1])
