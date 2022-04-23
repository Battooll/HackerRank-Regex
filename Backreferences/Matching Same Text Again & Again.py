# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:19:35 2022

@author: FPCC
"""

Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEOIU])(\S)\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.


import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
