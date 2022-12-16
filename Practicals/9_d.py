d=dict()
def inp():
    n=input("Enter the name: ")
    m1=int(input("Enter the marks in subject 1:"))
    m2=int(input("Enter the marks in subject 2:"))
    m3=int(input("Enter the marks in subject 3:"))
    m4=int(input("Enter the marks in subject 4:"))
    d[n]=(m1,m2,m3,m4)

def perc(d):
    max=0
    ans=""
    for i in d.keys():
        sum=0
        for j in d[i]:
            sum+=j
        per=(sum*100)/4
        if per>max:
            max=per
            ans=i
    return ans

n=int(input("Enter the number of students: "))
for i in range(n):
    print("\tStudent",i+1)
    inp()

print("Student with highest percentage is: ",perc(d))
