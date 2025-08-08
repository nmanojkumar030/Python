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

name = "pam", "eva", "walle", "tim", "jane"
print(name)
print(type(name))

n = 1000  # type is int
print(n)

n = (1000,)
print(n)

s = ("peter",)
print(s)

# Parallel assignment

name, age, gender = t = "pam", 3, "female"
age = 45

print(name)
print(age)
print(gender)

print(t)

# To return more values from the functions
print(divmod(5, 2))
q, r = divmod(5, 2)

print(q)
print(r)
