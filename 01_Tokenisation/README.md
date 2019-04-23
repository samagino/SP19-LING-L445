###Max Match###

Max Match is an algorithm that is supposed to be pretty good at tokenizing
words in languages that don't dilineate words with any special character in
written text.

This algorithm is implemented in maxmatch.py. 

###WER###

maxmatch.py was tested using a perl script (WER.pl) obtained from
[here](http://svn.code.sf.net/p/apertium/svn/trunk/apertium-eval-translator/).
According to WER.pl, my implementation of max match has a WER of ~1.07 percent
(I think), so that's pretty good.

My implementation of Max Match takes a Conllu file to form a dictionary and
reads text segmented by sentences and writes the same text segmented by words
(split with newlines) to stdout.

To test it, I had to write one python script that takes Conllu files and strips
them down to the original text segmented by sentences split by newlines (to use
as input for maxmatach.py) and another that takes Conllu files and strips it
down to the original text segmented by words split by newlines (to compare to
maxmatch\_wordDump.txt to get the WER).

Here's the command I ran to get maxmatch\_WordDump.txt

```
cat ja_test_word_dump.txt | python3 maxmatch.py UD_Japanese-GSD/ja_gsd-ud-train.conllu > maxmatch_WordDump.txt
```

Here's the command I ran to get the WER:

```
perl WER.pl -r ja_test_wordDump.txt -t maxmatch_WordDump.txt > WER.txt
```
