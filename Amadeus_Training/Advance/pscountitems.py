from collections import Counter

s = """  Generators are a simple and powerful tool for creating iterators. They are written 
like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it,
 the generator resumes where it left off (it remembers all the data values and which statement was last executed). 
 An example shows that generators can be trivially easy to create: """

c = Counter(s.split())
# print(c)

for word in sorted(c, key=lambda w: c[w]):
    print('{:>22} : {}'.format(word, c[word]))

print('--' * 22)
for word in sorted(c, key=lambda w: c[w], reverse=True):
    print('{:>22} : {}'.format(word, c[word]))