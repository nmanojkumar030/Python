"""demo for generator function"""


def demo():
    print('Before 1')
    # return 123
    yield 123
    print('After 1')

    print('Before 2')
    # return 12.21
    yield 12.21
    print("After 2")

    print('Before 3')
    # return 'pam'
    yield 'pam'
    print('After 3')


# demo()
g = demo()
print(next(g))
print('-' * 22)

print(next(g))
print('-' * 22)

print(next(g))
print('-' * 22)

print(next(g))
