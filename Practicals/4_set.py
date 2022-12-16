def set1(n):
    s=set()
    while(n>0):
        num=n%10
        s.add(num)
        n=n//10
    return s

num=int(input("Enter the number: "))
assert num>=10
print("The tuple of its digits are: ", set1(num))
