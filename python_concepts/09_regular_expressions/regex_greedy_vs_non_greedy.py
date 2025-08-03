import re

s = 'the python and the perl scripting'
pattern = 'P.+N'  # Greedy match

m = re.search(pattern, s, re.IGNORECASE)

if m:
    print(m)
else:
    print('Failed to Match')

print(m)

pattern = 'P.+?N'  # Non-greedy match

m = re.search(pattern, s, re.IGNORECASE)

if m:
    print('Match String :', m.group())
    print(m.start())
    print(m.end())
else:
    print('Failed to Match')

print(m)
