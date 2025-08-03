"""Generator using expression"""

items = [bin(item) for item in range(10)]  # list comprehension
print(items)

items = (bin(item) for item in range(10))  # Generator expression
print(items)

for item in items:
    print(item)
