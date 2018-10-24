items = ['0b0', '0b1', '0b10']

for item in items:
    print(item)

print(iter(items))
li = iter(items)
print(next(li))
print(next(li))
print(next(li))
# print(next(li)) # When all element iteration is done raises Stop Iteration
