## read_words.py
"""
Created on Fri Jul 20 16:52:40 2018

@author: aftoncoombs
"""
import csv

def read_words(filename):
    words = []
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for word in reader:
            words.append(word[0])
    return words