n = 123  # global scope


def demo():
    n = 'pip'  # local scope
    print(n)


demo()
print(n)
