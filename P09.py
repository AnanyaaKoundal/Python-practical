''' Use dictionary to store marks of the students in 4 subjects. Write a function to 
find the name of the student securing highest percentage. (Hint: Names of 
students are unique).
'''

n=int(input("Enter the number of student: "))
d={}
for i in range(n):
    print("\n")
    name=input("Enter the name of the student: ")
    m1=int(input("Enter the marks of subject 1: "))
    m2=int(input("Enter the marks of subject 2: "))
    m3=int(input("Enter the marks of subject 3: "))
    m4=int(input("Enter the marks of subject 4: "))
    t=(m1,m2,m3,m4)
    d[name]=t

max=0
s=""
for i in d:
    sum=0
    for j in d[i]:
        sum+=j
    p=sum*100/4
    if(max<p):
        max=p
        s=i

print("Student with highest percentage: ",s)
