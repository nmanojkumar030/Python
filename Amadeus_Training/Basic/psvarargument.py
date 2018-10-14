def demo(*args):
    #  Variable arguments
    print(type(args))
    print(args)

demo()
demo(100)

items = (1, 2, 3, 4)
demo(items)
demo(*items)
