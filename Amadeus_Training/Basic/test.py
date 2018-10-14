import math

from pip._internal.commands import list

l1 = [1, 2, 3, [4]]
l2 = list(l1)

print(id(l1) == id(l2))

print(round(math.pi))

a = list((45,) * 4)

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]

for lst in values:
    for elme in lst:
        if v > elme:
            v = elme

print(v)
