i = 1

while i <= 10:
    if i == 1:
        print("one")
    elif i == 2:
        print("ii")
    elif i == 4:
        i += 1  # without this line, the loop will stuck in a infinite loop
        continue
    else:
        print(i)
    i += 1
else:
    print("loop completed")
