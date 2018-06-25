class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        print("\Name : ",self.name)
        print("Roll Number : ",self.roll)

ob2 = Student("Akr",11506836)
ob3 = Student("CKR",11507090)
ob4 = Student("MKR",11503739)

ob2.display()
ob3.display()
ob4.display()
