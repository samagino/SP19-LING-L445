"""
bad_ja_segmenter.py

bad Japanese segmenter
This only segments by full stops because I don't know how Japanese works
"""

import sys
SAMPLE_SIZE = 4096 # 1 page of memory (assuming 1 char == 1 byte)


sample = sys.stdin.read(SAMPLE_SIZE)
while sample:

    # \u3002 == japanese full stop
    sample = sample.replace('\u3002', '\u3002\n')
    sys.stdout.write(sample)
    
    sample = sys.stdin.read(SAMPLE_SIZE)
