phrase = "Don't Panic!"
plist = list(phrase)

print(phrase)
print(plist)

plist.pop(0)
plist.remove("'")
plist.remove(" ")

plist.pop()
plist.pop()
plist.pop()
plist.pop()

plist.insert(3, plist.pop())

new_phrase=''.join(plist)
print(plist)
print(new_phrase)
