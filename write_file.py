# -*- coding: utf-8 -*-
## write_file.py
"""
Created on Fri Jul 20 18:04:06 2018

@author: aftoncoombs
"""

def write_file(filename, words):
    file = open(filename, 'w')
    for item in words:
        file.write("%s\n" % item)
