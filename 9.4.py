class Shape:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l*self.b

class Rectangle(Shape):
    def area(self):
        print("\n
              Area of Rectangle : ",super().area())
        
class Square(Shape):
    def area(self):
        print("Area of Square : ",super().area())

ob4 = Rectangle(20,15)
ob4.area()
ob5 = Square(5,5)
ob5.area()

