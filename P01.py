''' Write a function that takes the lengths of three sides: side1, side2 and side3 of the triangle as the input from th user
using the input function and return the area and perimeter of the triangle as a tuple. Also, assertthat sum of the length of any
two sides is greater then the third side'''

def check(a,b,c):
    return (a+b)>c and (b+c)>a and (a+c)>b

def func1():
    a=int(input("Enter side 1: "))
    b=int(input("Enter side 2: "))
    c=int(input("Enter side 3: "))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**(1/2)
    p=a+b+c
    if(check(a,b,c)):
        print("\nThe sum of length of any two sides is greater than third")
    return (area,p)

t=func1()
print("\nArea: ",t[0])
print("Perimeter: ", t[1])
