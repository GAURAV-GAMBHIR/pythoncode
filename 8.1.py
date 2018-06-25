class Circle:
    def __init__(self,rad):
        self.rad = rad
    def getArea(self):
        return 3.14*self.rad**2
    def getCircumference(self):
        return 2*3.14*self.rad

ob1 = Circle(10)
print("get Area : ",ob1.getArea())
print("get Circumference : %.2f"%ob1.getCircumference())
