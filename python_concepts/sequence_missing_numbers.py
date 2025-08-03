input_set = {1, 2, 3, 4, 5, 6, 9, 10 }
full_set = set(range(sorted(input_set).pop(0),sorted(input_set).pop()))

print(full_set.difference(input_set))
