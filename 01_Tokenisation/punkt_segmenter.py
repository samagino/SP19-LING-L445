import sys
from nltk.tokenize import sent_tokenize

SAMPLE_SIZE = 1024

sample = sys.stdin.read(SAMPLE_SIZE)
while sample:

    tokenized_sents = sent_tokenize(sample)

    for sentence in tokenized_sents:
        sys.stdout.write(sentence + '\n')

    sample = sys.stdin.read(SAMPLE_SIZE)
