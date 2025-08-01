from builtins import zip
from itertools import zip_longest

name = ['sam', 'pam', 'tim']
age = [2, 3, 4]
gender = ['male', 'female', 'male']

for n, a, g in zip(name, age, gender):
    print(n, a, g)

for n, a, g in zip_longest(name, age, gender):
    print(n, a, g)
