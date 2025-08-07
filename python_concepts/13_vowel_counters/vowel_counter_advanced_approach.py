vowels = {"a", "e", "i", "o", "u"}
found = {}
print(type(found))

word = input("Provide a word to search for vowels: ")

found = vowels.intersection(word)

print(type(found))

for letter in found:
    print(letter)
