"""
tuple aka readonly list
  - immutable list
  - write once, read many times

"""

t = (12, "pam", 3.4, "kim", "pam", "andy")
print(t)
print(type(t))
print(len(t))

print(t[-3])
print(t[:-3])
print(len(t))

for item in t[:-3]:
    print(item)
