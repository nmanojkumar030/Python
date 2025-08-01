# Usual List Iteration
def square_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n ** n)
    return result


output1 = square_numbers([1, 2, 3, 4, 5])
print(output1)

# The same thing as above but done in using List Comprehension
output2 = [n ** n for n in [1, 2, 3, 4, 5]]
print(output2)


# Generator
def square_numbers_gen(numbers):
    for n in numbers:
        yield n ** n


output3 = square_numbers_gen([1, 2, 3, 4, 5])
print(output3)

output4 = (n ** n for n in [1, 2, 3, 4, 5])  # Use () to create generator
print(output4)

# Convert the generator ti list
output5 = output4
print(list(output5))

# print(next(output3))
# print(next(output3))
# print(next(output3))
# print(next(output3))
# print(next(output3))
# print(next(output3))  # Raises StopIteration error
print(output4)  # This prints the generator object rather than entire list

for item in output4:
    print(item)
