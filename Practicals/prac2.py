def calc_sales(t):
    sales=0
    for i in t:
        sales+=i
    if sales<50000 :
        com=0
    else:
        com=sales*(0.05)
    print("Sales: ",sales)
    print("Commission: ",com)
    print("Total Earning: ",sales+com)
    ch=""
    if sales>=80000:
        ch="Excellent" 
    elif sales>=60000:
        ch="Good"
    elif sales>=40000:
        ch="Average"
    else:
        ch="Work Hard"
    print("Remarks: ",ch)
    t=(*t, sales, com, sales+com, ch)
    return t

t1=tuple()
for i in range(4):
    n=int(input("Enter the sales in week"+str(i+1)))
    t1=(*t1,n)
t1=calc_sales(t1)
print("Employee Record: ", t1)
