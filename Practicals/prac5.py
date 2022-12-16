try:
    myfile=open("file1.txt",'r')
except:
    print("Error while opening current file")
    exit()
f2=open("file2.txt",'w')

print("Content of file1: ")
str1=" "
while str1:
    str1=myfile.readline()
    print(str1)
    f2.write(str1)
    str1=myfile.readline()
    print(str1)
myfile.close()
f2.close()

f1=open("file2.txt",'r')
print("Content of file2 after copying..")
str1=" "
while str1:
    str1=f1.readline()
    print(str1)
