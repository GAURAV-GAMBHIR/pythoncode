class Expenditure:
    def __init__(self,exp,sav):
        self.exp = exp
        self.sav = sav
    def display(self):
        print("\nExpenditure : ",self.exp)
        print("Savings : ",self.sav)
    def calSalary(self):
        return self.sav + self.exp
    def displaySalary(self):
        print("Total Salary : ",self.calSalary())

ob7 = Expenditure(37000,15000)
ob7.display()
ob7.displaySalary()
