import pprint
people = {}
people['Ford'] = {'Name':'Ford Perfect', 'Gender':'Male', 'Occupation':'Researcher','Home Planet' : 'Betelgeuse Seven'}

people['Arthur'] = {'Name':'Arthur Dent', 'Gender':'Male', 'Occupation':'Sandwich-maker','Home Planet' : 'Earth'}
#print(people)
pprint.pprint(people)

print(people['Arthur']['Occupation'])
