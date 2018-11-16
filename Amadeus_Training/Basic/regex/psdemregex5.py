import re

from fileinput import input, filelineno

for line in input('folderspath1.txt', inplace=True, backup='.bak'):
    if filelineno() < 10:
        line = re.sub(':', ',', line)

    print(line, end='')
