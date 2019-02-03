import sys
import nltk.data
from nltk.tokenize import sent_tokenize

tokenizer = nltk.data.load('tokenizers/punkt/japanese.pickle')
SAMPLE_SIZE = 1024

sample = sys.stdin.read(SAMPLE_SIZE)
while sample:

    tokenized_sents = tokenizer.tokenize(sample)

    for sentence in tokenized_sents:
        sys.stdout.write(sentence + '\n')

    sample = sys.stdin.read(SAMPLE_SIZE)
