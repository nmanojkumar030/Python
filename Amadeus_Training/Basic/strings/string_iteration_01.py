s = 'this is a sample string in python'

for temp in s:
    if temp not in 'aeiou ':
        print(temp, ':', ord(temp))  # ascii value
    else:
        print('**')