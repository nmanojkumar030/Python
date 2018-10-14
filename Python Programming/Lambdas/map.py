#Map function maps or transforms each elemnt of an iterable resulting in a new iterable containing the transformed elements

#The number of elements in the output sequence will be equal to the number of elements in the input sequence

#Syntax :map(func,seq)

def f(x): return 2*x

L=[1,6,4,9,7]

M=list(map(f,L))
print(M)