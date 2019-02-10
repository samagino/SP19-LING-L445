"""
desegment.py:

takes a Connlu file and returns original text segmented by
    sentences
"""


import sys

def desegment(filePath):

    # open file
    with open(filePath, "r") as f:

        sample = f.read()

        # split sample into lines
        sample = sample.split('\n')
        
        for line in sample :
            if line[0 : 9] == '# text = ' :
                sys.stdout.write(line[9 : len(line)] + '\n')

if len(sys.argv) != 2 :
    print('desegment needs a file to desegment.')
    print('usage:\n\tpython desegment.py path/to/file')
else :
    desegment(sys.argv[1])
