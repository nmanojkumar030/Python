"""
Functional Programming
syntax for the lambda functions
lambda arg1, arg2,......: expression

"""

# power = lambda x, n: x ** n
power = lambda x, n=0: x**n
print(power)
print(power(3, 4))
print(power(3))
