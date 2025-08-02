from os import walk
from pprint import pprint as pp

for item in walk('D:/'):
    pp(item)

