import re

s = 'root x:0;0,root;/root,/bin/bash'

items = re.split(',|:|;|\s+', s)
print(items)
