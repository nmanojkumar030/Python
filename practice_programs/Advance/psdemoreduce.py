from functools import reduce

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = reduce(lambda a, b: a + b, items)
print(result)

result = reduce(lambda a, b: a if a > b else b, items)
print(result)
