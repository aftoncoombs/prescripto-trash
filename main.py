## main.py
## Gets words from corncob list and applies "proper" ending
from read_words import read_words
from find_by_endings import find_by_endings
from make_correct_endings import make_correct_endings
from show_off import show_off
from write_file import write_file

words = read_words("corncob_lowercase.txt")
latin_us = find_by_endings(words, "us")
latin_us_plurals = make_correct_endings(latin_us, "us", "i")
show_off_with_latin_plurals = show_off(latin_us, latin_us_plurals, "plural")
write_file("latin_plurals.txt", show_off_with_latin_plurals)