''' Write a function that takes a sentence as input from the user and calculates 
the frequency of each letter. Use a variable of dictionary type to maintain the 
count.
'''

def frequency(a):
    s={}
    for i in a:
        if i!=" ":
            if i in s.keys():
                s[i]=s[i]+1
            else:
                s[i]=1
    return s

str=input("Enter the sentence: ")
ans=frequency(str)
print(ans)
