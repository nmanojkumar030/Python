from copy import deepcopy

# Same reference shared
n = 12
a = n
print(id(n))
print(id(a))

items = [1, 2, 3, 4, 5]
# backup = items  # Shallow copy
# backup = items.copy()  # Deep copy

backup = deepcopy(items)

items.pop()

print(items)
print(backup)
