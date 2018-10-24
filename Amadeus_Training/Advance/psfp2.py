items = list(range(1, 200))
print(items)

m = filter(lambda n: n % 7 == 0, items)
print(list(m))
