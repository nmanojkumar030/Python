from csv import reader


def get_shell_frequency(csv_file):
    shell_freq = dict()
    for row in reader(open(csv_file), delimiter=':'):
        val = row[-1]
        shell_freq[val] = shell_freq.get(val, 0) + 1

    return shell_freq


counts = get_shell_frequency('folderspath.txt')
# print(counts)

for key, value in counts.items():
    print(key, '->', value)
