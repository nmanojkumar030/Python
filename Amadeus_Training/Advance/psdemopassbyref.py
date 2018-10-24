def demo(n, value):
    print(id(n))
    n += 1
    print(id(n))
    value.append(6)
    print(id(value))


items = [1, 2, 3, 4, 5]
print(id(items))

scalar = 10
print(id(scalar))

demo(scalar, items)
