"""
Functional Programming
syntax for the lambda functions
lambda arg1, arg2,......: expression
"""

ascii_values = [112, 101, 116, 101, 114, 32, 112, 97, 110]

"""
<ascii char="p">112</ascii>
"""


def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av), av)


# m = map(tag_it, items)

m = map(lambda av: '<ascii char="{}">{}</ascii>'.format(chr(av), av), ascii_values)  # Lambda

for tag in m:
    print(tag)
