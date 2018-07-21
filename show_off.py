# -*- coding: utf-8 -*-
## show_off.py
"""
Created on Fri Jul 20 17:54:34 2018

@author: acoombs
"""

def show_off(original, new, form):
    brags = []
    for idx in range(0, len(original)):
        brag = "The " + form + " of " + original[idx] + " is " + new[idx]
        brags.append(brag)
    return(brags)
