from csv import reader

shell_freq = dict()
for row in reader(open('folderspath.txt'), delimiter=':'):
    # print(row)
    val = row[-1]
    shell_freq[val] = shell_freq.get(val, 0) + 1

print(shell_freq)
