def compute(a, b, c):
    print(a + b + c)


items = [11, 22, 33]
compute(items[0], items[1], items[2])
compute(*items)
