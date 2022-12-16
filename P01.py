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

'''
def func1(s1,s2,s3):
    assert s1+s2>s3 and s1+s3>s2 and s2+s3>s1, "The sum of two sides must be greater than 3rd side"
    s=(s1+s2+s3)/2
    area=(s*(s-s1)*(s-2)*(s-3))**(1/2)
    p=s1+s2+s3
    return (area,p)

a=int(input("Enter side1: "))
b=int(input("Enter side2: "))
c=int(input("Enter side3: "))
t=func1(a,b,c)
print("Area of triangle is: ",t[0])
print("Permiter of triangle is: ", t[1])
'''
