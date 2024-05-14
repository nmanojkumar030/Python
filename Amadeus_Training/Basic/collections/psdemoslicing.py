"""
Slicing -> name[start-index:end-index:step]
"""

s = 'manoj'

print(s[0:4])
print(s[:4])

print(s[1:4])

print(s[-1:])
print(s[4:])

print(s[1:-1])

print(s[-4:-1])

print(s[::-1])  # Reverse string

print(s[::-1] == s)

print(s[::2])