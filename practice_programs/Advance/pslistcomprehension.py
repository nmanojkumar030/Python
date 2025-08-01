"""
    List Comprehension:

    [Expression for val in Collection]

    [Expression for val in Collection  if <condition>]

    [Expression for val in Collection if <condition1> and <condition2>]

    [Expression for val1 in Collection1 and val2 in Collection2]

"""

squares = []

for n in range(1, 101):
    squares.append(n ** 2)

print(squares)

squares2 = [n ** 2 for n in range(1, 101)]
print(squares2)

remainders5 = [n ** 2 % 5 for n in range(1, 101)]
print(remainders5)

remainders11 = [n ** 2 % 11 for n in range(1, 101)]
print(remainders11)

divisible_by_5 = [n for n in range(1, 101) if n % 5 == 0]
print(divisible_by_5)

employees = [("Manoj", 1987), ("Kumar", 1990)]
test = [name for (name, year) in employees if year == 1987]

print(test)

lista = [1, 2, 3, 4, 5]
listb = [6, 7, 8, 9, 10]

cartesian_product = [(a, b) for a in lista for b in listb]
print(cartesian_product)
