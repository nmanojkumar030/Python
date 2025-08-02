vowels = ["a", "e", "i", "o", "u"]
found = []
word = input("Provide a word to search for vowels: ")
# word = "Milliways"

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for letter in found:
    print(letter)
