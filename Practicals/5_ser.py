#factorial.py
def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
    return fact

#calc.py
from factorial import *
def calc(n, x):
    sum=1
    c=2
    i=2
    while(c<=n):
        if(i%2==0):
            sum-=(float((x**c))/fact(c))
            i+=1
        else:
            sum+=(float((x**c))/fact(c))
            i+=1
        c+=2
    return sum
num=int(input("Enter n: "))
x=int(input("Enter x: "))
print("Sum: ",calc(num, x))
