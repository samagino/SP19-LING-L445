###Max Match###

Max match is an algorithm that is supposed to be pretty good at tokenizing words
in languages that don't dilineate words with anything in written text.

This algorithm is implemented in maxmatch.py. 

###WER###

maxmatch.py was tested using a perl script (WER.pl) obtained from [here](http://svn.code.sf.net/p/apertium/svn/trunk/apertium-eval-translator/).
According to WER.pl, my implementation of max match has a WER of ~1.07 percent (I think), so that's pretty good.


Here's the command I ran to get the WER:

```
perl WER.pl -r ja_test_wordDump.txt -t maxmatch_WordDump.txt
```
