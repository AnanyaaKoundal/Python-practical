''' Write  a  menu-driven  program  to  accept  a  list  of  student  names  and  perform 
the  following
a. search an element  using linear  search/ binary search.
b. Sort  the elements  using  bubble  sort/ insertion sort/ selection sort.
'''

def linear_search(l, n):
    for i in range(0,len(l)):
        if l[i]==n:
            print("Element found at index ",i)
            return
    print("Element not found")

def binary_search(l, n):
    start=0
    end=len(l)-1
    insertion_sort(l)
    print("Sorting list to implement binary search")
    while(start<=end):
        mid=(start+end)//2
        if(l[mid]==n):
            print("Element found at index ",mid)
            return
        elif(n<l[mid]):
            end=mid-1
        else:
            start=mid+1
    print("Element not found")

def bubble_sort(l):
    for i in range(0,len(l)-1):
        for j in range(i+1, len(l)):
            if l[i]>l[j]:
                n=l[i]
                l[i]=l[j]
                l[j]=n

def selection_sort(l):
    for i in range(0,len(l)-1):
        temp=i
        for j in range(i+1, len(l)):
            if l[temp]>l[j]:
                temp=j
        t=l[i]
        l[i]=l[temp]
        l[temp]=t


def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
  
n=int(input("Enter your range: "))
l=[]
for i in range(n):
    num=int(input("Enter the number: "))
    l.append(num)

num=int(input("Enter the element to be searched: "))
print("\n1. Linear search")
print("2. Binary Search")
ch=int(input("Select the search type: "))
if(ch==1):
    linear_search(l,num)
else:
    binary_search(l,num)


print("\n1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")
ch=int(input("Select the sort type: "))
if(ch==1):
    bubble_sort(l)
elif(ch==2):
    selection_sort(l)
else:
    insertion_sort(l)
print("Sorted list: ",l)
