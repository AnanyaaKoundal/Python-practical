import matplotlib.pyplot as plt
import numpy as np

l=eval(input("Enter the list(with [])"))
plt.style.use('ggplot')
plt.title("Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.hist(l, bins=[i for i in range(10,55,10)],width=10, edgecolor="k")
plt.show(block=False)

'''
import matplotlib.pyplot as plt
n=int(input("Enter a size of list: "))
l=[]
for i in range(n):
    d=int(input("Enter the element: "))
    l.append(d)
    
print("Processing Histogram")
plt.style.use('ggplot')
plt.title("Histogram")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.hist(l,bins=[10,20,30,40,50], width=10, edgecolor="black")
plt.show()

'''
