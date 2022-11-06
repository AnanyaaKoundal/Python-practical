''' Write a Python program  to  perform  the following using list:
a)  Check  if  all elements  in list  are numbers  or  not.
b)  If  it  is  a numeric list,  then count  number of  odd values  in it.
c)  If  list  contains  all Strings,  then display largest  String in the list.
d)  Display list  in reverse form.
e)  Find a specified element  in list.
'''

def reverse(l):
    l=l[::-1]
    print("Reversed list: ",l)

def search(l,n):
    for i in range(0, len(l)):
        if l[i]==n:
            print("Element found at index ",i)
            return
    print("Element not found")
    
n=int(input("Enter your range: "))
l=[]
for i in range(n):
    num=input("Enter the number: ")
    l.append(num)

print("List Entered: ",l)

check1=all(i.isdigit() for i in l)
check2=all(i.isalpha() for i in l)

if (check1):
    print("List contain all digits!!")
    c=0
    for i in l:
        if int(i)%2!=0:
            c+=1
    print("Number of odd values: ",c)

elif(check2):
    print("List contain all strings!!")
    max=len(l[0])
    ans=l[0]
    for i in l:
        if(len(i)>max):
            max=len(i)
            ans=i
    print("Largest string is: ",ans)

reverse(l)

num2=input("Enter element to be searched: ")
search(l,num2)

