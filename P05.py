''' Write   a   function   that   finds   the   sum   of   the   n   terms   of   the   following   series. 
Import  the factorial function created in question 4.
1 –  x  2 /2!  +  x4  /4!  –  x  6  /6!  +  … xn /n!
'''

def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact+=i
    return fact

def calc(n):
    sum=1.0
    c,x=1,1
    for i in range(2,n+1, 2):
        if(c==1):
            sum-=(float((x**i))/fact(i))
            c+=1
        else:
            sum+=(float((x**i))/fact(i))
            c+=1
    return sum

num=int(input("Enter the number: "))
print(calc(num))
