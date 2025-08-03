import copy

l1 = [1, 2, 3, [4]]  # Nested List
l2 = list(l1)  # shallow copy, will show 4 in both l1 and l2

l2[3][0] = 10
print(l1)
print(l2)

print(id(l1) == id(l2))

l1 = [1, 2, 3, 4]
l2 = list(l1)  # shallow copy

l2[3] = 10
print(l1)
print(l2)

print(id(l1) == id(l2))

l1 = [1, 2, 3, [4]]  # Nested List
l2 = copy.deepcopy(l1)  # shallow copy, will show 4 in both l1 and l2

print(l1)
print(l2)

print(l1 == l2)

a = list((45,) * 4)
print(a)

values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]

for lst in values:
    for elme in lst:
        if v > elme:
            v = elme
print(v)
