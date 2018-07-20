## main.py
## Gets words from corncob list and applies "proper" ending
import csv

filename = "corncob_lowercase.txt"
words = []
with open(filename, "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for word in reader:
        words.append(word)
