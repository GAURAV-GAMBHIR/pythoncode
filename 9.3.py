class Cop:
    def __init__(self,name,age,wexp):
        self.name = name
        self.age = age
        self.wexp = wexp
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Work Experience : ",self.wexp)
    def update(self):
        self.name = input("Update Name : ")
        self.age = int(input("Update Age : "))
        self.wexp = int(input("Update Work Experience : "))

class Mission(Cop):
    def addMissionDetails(self):
        print("One Cop is now available for Mission\n\nDetails of the Cop is given below")
        self.display()
        print("\nUpdate details of Cop on Mission")
        self.update()
        print("Cop ready for Mission with details")
        self.display()

ob3 = Mission("Akr",21,4)
ob3.addMissionDetails()
