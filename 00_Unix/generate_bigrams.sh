# tokenize words, get rid of empty lines
sed 's/[^А-Яа-яЇїЄєҮүӨө]\+/\n/g' | grep -v '^$'  > $$words
# generate nextwords
tail -n +2 $$words > $$nextwords
# paste nextwords next to words, then count unique words, then sort by count
paste $$words $$nextwords | sort | uniq -c | sort -rn

rm $$words $$nextwords
