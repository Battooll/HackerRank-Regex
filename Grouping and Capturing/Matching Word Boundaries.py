# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:19:35 2022

@author: FPCC
"""

regex_pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
