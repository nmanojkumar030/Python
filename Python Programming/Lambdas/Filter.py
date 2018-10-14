#Filter function filters a sequence -It's elements are passed through a filtering function and only those elements that pass a criteria are allowed to pass through while the rest are blocked

#Each element in the sequence is sent to the function func as an argument and if the function return TRue ,it will be sent to the output sequence

#Syntax : filter(func,sequence)

L=[1,6,4,9,7]

def f(x): return x%2==0

M=list(filter(f,L))
print(M)