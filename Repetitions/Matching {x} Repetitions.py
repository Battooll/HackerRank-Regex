# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:19:35 2022

@author: FPCC
"""

Regex_Pattern = r'^[a-zA-Z0-8-2]{40}[1-9-2\s]{5}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
