""" Multiple Match"""

import re

s = 'the python and the perl scripting'
pattern = 'P.+?N'  # Greedy match

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()

print(re.findall(pattern, s, re.I))  # List of match strings
