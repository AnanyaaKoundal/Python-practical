''' Consider a showroom of electronic products, where there are various salesmen. Each salesman is given a commission of 5%,
depending on the sales made per month. In case the sale done is less than 50000, then the salesman is not given any commission.
Write a function to calculate total sales of a salesman in a month, commission and remarks for the salesman. Sales done by each 
salesman per week is to be provided as input. Use tuples / list to store data of salesmen.
Assign remarks  according to  the following criteria: 
Excellent: Sales  >=80000
Good: Sales>=60000 and <80000 
Average: Sales>=40000 and <60000 
Work  Hard: Sales  <  40000
'''

def total_sales(t):
    sum=0
    for i in t:
        sum+=i
    return sum

def commission(sale):
    if(sale<50000):
        com=0
    else:
        com=sale*(0.05)
    print("Monthly sales: ",sale)
    print("Commission earned: ",com)
    print("Total earning: ", sale+com);
    if(com>=80000):
        print("Remark: Excellent")
    elif(com>=60000):
        print("Remark: Good")
    elif(com>=40000):
        print("Remark: Average")
    else:
        print("Work Hard")

t=tuple()
for i in range(4):
    print("Weelk", i+1, end=", ")
    s=int(input("Enter sale: "))
    t=(*t, s)

sale=total_sales(t)
commission(sale)

