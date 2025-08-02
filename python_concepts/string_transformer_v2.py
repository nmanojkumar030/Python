phrase = "Don't Panic!"
plist = list(phrase)

print(phrase)
print(plist)

plist.pop(0)
plist.remove("'")
plist.remove(" ")
plist.remove("!")

new_phrase = "".join(plist[:3])
new_phrase = new_phrase + "".join([plist[4], plist[3]])
print(new_phrase)
