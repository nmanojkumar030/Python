def demo(*args):
    #  Variable arguments
    print(type(args))
    print(args)


demo()
demo(100)

items = (1, 2, 3, 4)
demo(items)  # Entire items is passed as a single argument to the method.
demo(*items)  # Each item of the items collection is passed as arguments to the method.
