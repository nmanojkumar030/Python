items = [2.2, 'pam', '1.2', 'kim', 'eva', 2.3, .98, 'tim', 'pat']

print(items)
print(type(items))
print(len(items))

items[-1] = 'patric'
print(items)

items.append('amadeus')
print(items)

items.insert(0, 'bengaluru')
print(items)

items2 = [2.2, 'pam', '1.2', 'kim', 'eva', 2.3, .98, 'kim', 'pat']
item2 = 'bengaluru'

start = 0
try:
    while True:
        # print(items2.index('kim'))
        kims_index = items2.index('kim', start)
        items2.insert(kims_index, item2)
        start = kims_index + 2
        print(items2)
except ValueError as err:
    pass

print(items2)

value = items2.pop(-5)

print(value)

item3 = 'pam'
while item3 in items2:
    items2.remove(item3)

print(items2)

print(items2 * 3)
print(list(set(items2)))

items4 = [2.2, 4.5, 1.2, 2.3, .98]
items4.sort()
items4.reverse()

print(items4)
