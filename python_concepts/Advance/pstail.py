from collections import deque

for line in deque(open('folderspath.txt'), 3):
    print(line, end='')
