# -*- coding: utf-8 -*-
## make_correct_ending.py
"""
Created on Fri Jul 20 17:48:17 2018

@author: acoombs
"""
import re

def make_correct_endings(singulars, ending, plural):
    re_ending = ending + "$"
    correct_forms = []
    for idx in range(0, len(singulars)):
        correct_form = re.sub(re_ending, plural, singulars[idx])
        correct_forms.append(correct_form)
    return(correct_forms)
