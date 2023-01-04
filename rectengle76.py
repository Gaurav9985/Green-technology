class rectengle:
    a=int(input("enter a length :"))
    b=int(input("enter a height :"))
    def area(self):
        area=self.a*self.b
        print(area)
    def perimeter(self):
        p=2*(self.a*self.b)
        print(p)
c=rectengle()
x=c.area()
y=c.perimeter()
 
