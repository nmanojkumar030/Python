vowels = ["a", "e", "i", "o", "u"]
found = {}
# word = input("Provide a word to search for vowels: ")
word = "Milliways"

print(type(found))

for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 1
        else:
            found[letter] += 1

for K, V in sorted(found.items()):
    print(K, "was found", V, "times")

    
