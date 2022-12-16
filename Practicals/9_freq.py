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
