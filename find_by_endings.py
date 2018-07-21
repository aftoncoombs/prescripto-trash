## find_by_endings.py
## Finds words by ending
import re

def find_by_endings(words, ending):
    search_string = ".*" + ending + "$"
    search_term = re.compile(search_string)
    results = list(filter(search_term.match, words))
    return(results)
