import re

s = "root:x:0:0:root:/root:/bin/bash"
pattern = ':'
replacement = ','

s2 = re.sub(pattern, replacement, s)
print(s2)
print()

s3 = re.sub('[AEIOU]', '*', s2, flags=re.I, count=1)
print(s3)
