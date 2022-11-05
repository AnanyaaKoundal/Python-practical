''' Write  a  function  that  takes  a  number  (>=10)  as  an  input  and  return  the  digits  of 
the number as  a set.
'''

def set1(n):
    s=set()
    while(n>0):
        num=n%10
        s.add(num)
        n=n//10
    return s

num=int(input("Enter the number: "))
print("The tuple of its digits are: ", set1(num))
