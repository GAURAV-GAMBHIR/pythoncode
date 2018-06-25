class Animal:
    def animal_attribute(self):
        print("In class Animal")

class Tiger(Animal):
    def __init__(self):
        print("In class Tiger")
        self.animal_attribute()
        print("Again in class Tiger")

ob1 = Tiger()
