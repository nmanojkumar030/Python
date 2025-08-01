from csv import reader
from collections import Counter


def get_shell_frequency(csv_file):
    user_shell = [row[-1] for row in reader(open(csv_file), delimiter=':')]  # list comprehension
    return Counter(user_shell)


counts = get_shell_frequency('folderspath.txt')

for key, value in counts.items():
    print(key, '->', value)
