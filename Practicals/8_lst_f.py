def largest(l):
    ans=l[0]
    for i in l:
        if i>ans:
            ans=i
    return ans

def reverse(l):
    l=l[::-1]
    print("\nReversed list: ",l)

def search(l,n):
    for i in range(0, len(l)):
        if l[i]==n:
            print("Element found at index ",i)
            return True
    print("Element not found")
    return False

def common(l1,l2):
    l=[]
    for i in l1:
        if i in l2:
            l.append(i)
    return l

n=int(input("Enter your range: "))
l=[]
for i in range(n):
    num=input("Enter the number: ")
    l.append(num)

print("\nList Entered: ",l)

check1=all(i.isdigit() for i in l)
check2=all(i.isalpha() for i in l)

if (check1):
    print("\nList contain all digits!!")
    c=0
    for i in l:
        if int(i)%2!=0:
            c+=1
    print("\nNumber of odd values: ",c)

elif(check2):
    print("\nList contain all strings!!")
    print("\nLargest string is: ",largest(l))

reverse(l)

num2=input("\nEnter element to be searched: ")
search(l,num2)

num2=input("\nEnter element to be removed: ")
if(search(l,num2)==True):
    l.remove(num2)
    print("Element removed successfully!!")
else:
    print("Element nor found in the list.")

print()
n=int(input("\nEnter range for second list: "))
l2=[]
for i in range(n):
    num=input("Enter the element: ")
    l2.append(num)

print("\nList Entered: ",l2)
ans=common(l,l2)
print("\nCommom elements are: ",end="")
for i in ans:
    print(i, end=" ")
