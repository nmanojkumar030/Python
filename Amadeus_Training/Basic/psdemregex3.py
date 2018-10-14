import re
from fileinput import input, filelineno, filename


def grep_me(pattern, *args):
    for line in input(args):
        if re.search(pattern, line, re.I):
            print('{}:{}:{}'.format(filename(), filelineno(), line), end='')


grep_me('^root', 'folderspath.txt')
