M=(lambda x:x**2)(4)
print(M)

square=lambda x:x**2
print(square(4))


#cONVERT ALL CHARACTERS of strings ina list to uppercase
L=['HELLO','WORLD']
M=list(map(lambda x:x.upper(),L))
print(M)


#Add corresponding elements of 3 lists

L1=[1,2,3]
L2=[4,5,6]
L3=[7,8,9]
M=list(map(lambda a,b,c:a+b+c,L1,L2,L3))
print(M)


#Multiply all elements in a List

from functools import reduce
L=[1,6,4,9,7]
product=reduce(lambda x,y:x*y,L)
print(product)
