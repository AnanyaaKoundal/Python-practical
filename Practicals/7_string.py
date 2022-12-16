def menu():
    print("\n\n1. Find the length of  string.")
    print("2. Return maximum  of  three strings.")
    print("3. Accept  a string and replace all vowels  with “#”")
    print("4. Find number  of  words  in the given string.")
    print("5. Check  whether  the string  is  a palindrome or  not.")
    print("6. Exit")

def length(s):
    c=0
    for i in s:
        c=c+1
    print("Length of the string is: ",c)

def max_of_three(s1,s2,s3):
    if(s1>s2 and s1>s3):
        print("Maximum: ",s1)
    elif(s2>s1 and s2>s3):
        print("Maximum: ",s2)
    else:
        print("Maximum: ",s3)

def replace_vowels(s):
    l=['A','E','I','O','U','a','e','i','o','u']
    s1=""
    for i in s:
        if i in l:
            s1=s1+"#"
        else:
            s1=s1+i
    s=s1
    print("String after replacing: ",s)

def number_of_words(s):
    c=1
    for i in s:
        if i==" ":
            c=c+1
    print("Number of words: ",c)

def palindrome(s):
    i=0
    j=len(s)-1
    while(i<=j):
        if s[i]!=s[j]:
            print("The word is not a palindrome.")
            return
        i+=1
        j-=1
    print("The word is palindrome.")
    
menu()
ch=int(input("Enter your choice: "))
while(ch!=6):
    if(ch==1):
        s=input("Enter the string: ")
        length(s)
    elif ch==2:
        s1=input("Enter the string 1: ")
        s2=input("Enter the string 2: ")
        s3=input("Enter the string 3: ")
        max_of_three(s1,s2,s3)
    elif ch==3:
        s=input("Enter the string: ")
        replace_vowels(s)
    elif ch==4:
        s=input("Enter the string: ")
        number_of_words(s)
    elif ch==5:
        s=input("Enter the word: ")
        palindrome(s)
    menu()
    ch=int(input("Enter your choice: "))
