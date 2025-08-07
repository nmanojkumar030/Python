"""
Functional Programming
syntax for the lambda functions
lambda arg1, arg2,......: expression
"""

power = lambda x, n: x**n

print(power)
print(power(4, 3))

power = (lambda x, n: x**n)(2,3)
print(power)