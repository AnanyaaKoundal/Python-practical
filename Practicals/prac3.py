l=[0,1]
def fib(n):
    if n<len(l):
        return l[n-1]
    else:
        l.append(fib(n-1)+fib(n-2))
        return l[n]
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def calc(n):
    s1=fib(n)
    s2=fact(n)
    return [s1,s2]

ch=int(input("Enter the number: "))
l2=calc(ch)
print("Term",ch,"in fibonacci series: ",l2[0])
print("Factorial of",ch,":",l2[1])
    
