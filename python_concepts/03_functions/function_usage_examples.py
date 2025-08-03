def demo():
    print("null arguments")


print(demo)


def demo(a, b):
    print(a + b)


print(demo)

# executes the most recent definition,
# here it calls the second demo as it is the most recent
# demo()

demo = "Manoj"

print(demo)

n = 12  # Same as above, assigning different value to same variable
n = 13
