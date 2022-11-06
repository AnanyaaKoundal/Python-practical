''' Consider  a  tuple  t1={1,2,5,7,9,2,4,6,8,10}.  Write  a  program  to  perform  following operations:
a)  Print  another  tuple whose values  are  even numbers  in the given tuple.
b)  Concatenate a tuple t2={11,13,15)  with t1.
c)  Return maximum  and minimum  value from  this  tuple.
'''

t1=(1,2,5,7,9,2,4,6,8,10)
t=tuple()
for i in t1:
    if i%2==0:
        t=(*t, i)

print("Tuple with even values: ", t)

t2=(11,13,15)
t1=t1+t2
print("Tuple after concatenation: ", t1)

min=t1[0]
max=t1[0]
for i in t1:
    if i>max:
        max=i
    elif i<min:
        min=i

print("Maximum value: ",max)
print("Minimum value: ",min)
