try:
    myfile=open("current.txt",'r')
except:
    print("Error while opening current file")
    exit()
f2=open("new.txt",'w')

print("Current file: ")
str1=" "
while str1:
    str1=myfile.readline()
    print(str1)
    f2.write(str1)
    str1=myfile.readline()
    print(str1)
myfile.close()
f2.close()

f1=open("new.txt",'r')
print("File after copy..")
str1=" "
while str1:
    str1=f1.readline()
    print(str1)
