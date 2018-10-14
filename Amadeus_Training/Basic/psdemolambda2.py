"""
Functional Programming
syntax for the lambda functions
lambda arg1, arg2,......: expression
"""

items = [2, 3, 1, 4, 5, 6, 7, 3, 4]

m = map(bin, items)  # Functional programming
print(m)

for item in m:
    print(item)
