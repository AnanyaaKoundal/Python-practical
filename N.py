class Product:
    count=0
    def calc(self):
        if self.material=="Metal":
            return 0.2*self.costPrice
        if self.material=="Plastic":
            return 0.1*self.costPrice
    def __init__(self,name, m1,m2):
        self.name=name
        self.material=m1
        self.costPrice=m2
        assert m2>=25 and m2<=250
        self.discount=Product.calc(self)          
        Product.count+=1
    def avg(self,m1,m2,m3):
        self.avg=(m1+m2+m3)/3
        if(self.avg>Student.average):
            Student.average=self.avg
    def sellingPrice(self):
        p=self.costPrice- self.discount
        print("Selling price is of",self.name,": ",p)
    def display(self):
        print("Name:",self.name)
        print("Material:",self.material)
        print("CostPrice:",self.costPrice)
        print("Discount:",self.discount)
    def __del__(self):
        print("Destructor called successfully for object",self.name)

p1=Product("Plate", "Metal", 170)
print("Value of count is after creating plate:", Product.count)
p2=Product("Spoon","Plastic", 26)
print("Value of count is:", Product.count)
p1.sellingPrice()
p2.sellingPrice()
print("Value of count is:", Product.count)'''
