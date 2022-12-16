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
