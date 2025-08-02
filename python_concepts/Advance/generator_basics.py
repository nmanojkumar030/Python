def gen_integers():
    """Infinite Streams"""
    i = 1
    while True:
        yield i
        i += 1


square = (element ** 2 for element in gen_integers())


def take_n(seq, n):
    for item in range(n):
        yield next(seq)


for item in take_n(square, 5):
    print('-' * item)
    print(item)

# for item in gen_integers():
#   print(item)
