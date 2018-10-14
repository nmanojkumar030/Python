from csv import reader
from collections import Counter


def get_shell_frequency(csv_file):
    user_shell = list()
    for row in reader(open(csv_file), delimiter=':'):
        user_shell.append(row[-1])

    return Counter(user_shell)


counts = get_shell_frequency('folderspath.txt')
# print(counts)

for key, value in counts.items():
    print(key, '->', value)
