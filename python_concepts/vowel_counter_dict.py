vowels = ["a", "e", "i", "o", "u"]
found = {}
word = input("Provide a word to search for vowels: ")
# word = "Milliways"

found["a"] = 0
found["e"] = 0
found["i"] = 0
found["o"] = 0
found["u"] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for K, V in sorted(found.items()):
    print(K, "was found", V, "times")
