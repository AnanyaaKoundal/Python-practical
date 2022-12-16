class Student:
    average=0
    def __init__(self, n, m1, m2,m3):
        self.name=n
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
        self.avg=(m1+m2+m3)/3
        Student.update(self)
    def update(self):
        if(Student.average<self.avg):
            Student.average=self.avg
    def __del__(self):
        del self.name
        del self.marks1
        del self.marks2
        del self.marks3
        print("Desctructor called successfully")
    def __str__(self):
        s="\nName: "+self.name+"\nMarks 1: "+str(self.marks1)+"\nMarks2: "+str(self.marks2)+"\nMarks 3: "+str(self.marks3)
        s+="\nAverage: "+str(self.avg)
        return s
l=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    print("\tStudent",i+1)
    n=input("Enter the name: ")
    m1=int(input("Enter the marks of subject 1:"))
    m2=int(input("Enter the marks of subject 2:"))
    m3=int(input("Enter the marks of subject 3:"))
    s=Student(n,m1,m2,m3)
    l.append(s)

for i in l:
    print(i)

print("\nMaximum Average of the class: ",Student.average)
