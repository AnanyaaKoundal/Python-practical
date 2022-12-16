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
  
n=int(input("Enter the size of list: "))
l=[]
for i in range(n):
    num=input("Enter the name: ")
    l.append(num)

while True:
    print("\n\t    Operations\n\t1. Linear search")
    print("\t2. Binary Search")
    print("\t3. Bubble Sort")
    print("\t4. Selection Sort")
    print("\t5. Insertion Sort")
    print("\t6. Exit")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        num=input("Enter the element to be searched: ")
        linear_search(l,num)
    elif(ch==2):
        num=input("Enter the element to be searched: ")
        binary_search(l,num)
    elif(ch==3):
        bubble_sort(l)
        print("Sorted list: ",l)
    elif(ch==4):
        selection_sort(l)
        print("Sorted list: ",l)
    elif(ch==5):
        insertion_sort(l)
        print("Sorted list: ",l)
    elif(ch==6):
        break;
    else:
        print("Invalid choice!")
