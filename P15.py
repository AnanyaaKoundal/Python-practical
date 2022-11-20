class Student:
    average=0
    def __init__(self,name, m1,m2,m3):
        self.name=name
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
        Student.avg(self,self.marks1,self.marks2,self.marks3)
    def avg(self,m1,m2,m3):
        self.avg=(m1+m2+m3)/3
        if(self.avg>Student.average):
            Student.average=self.avg
    def __del__(self):
        print("Destructor called successfully for object",self.name)

a=Student("a",2,3,4)
print(Student.average)
b=Student("b",2,5,6)
print(Student.average)
del a
