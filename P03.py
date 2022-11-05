''' Write   a   Python   function   to   find   the   nth   term   of   Fibonacci   sequence   and   its 
factorial. Return the result  as  a list.
'''

l=[0,1]

def fib(n):
    if(n<len(l)):
        return l[n-1]
    else:
        l.append(fib(n-1)+fib(n-2))
        return l[n]

def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
    return fact

def calc(n):
    s1=fib(n)
    s2=fact(n)
    return [s1,s2]

num=int(input("Ebter the number: "))
l=calc(num)
print(l[0], l[1])
