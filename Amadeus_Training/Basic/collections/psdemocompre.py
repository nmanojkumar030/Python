"""List Comprehension"""

items = [1, 3, 4, 2, 5, 6, 7]

temp1 = [hex(item) for item in items]
print(temp1)

temp1 = [item ** item for item in items]
print(temp1)

temp3 = [ord(i) for i in 'peter pan']
print(temp3)
