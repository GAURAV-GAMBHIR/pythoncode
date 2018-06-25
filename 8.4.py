class MovieDetails:
    def __init__(self,mname,aname,yr,rt):
        self.mname = mname
        self.aname = aname
        self.yr = yr
        self.rt = rt
    def display(self):
        print("\nMovie Name : ",self.mname)
        print("Artist Name : ",self.aname)
        print("Year of release : ",self.yr)
        print("Rating : ",self.rt)
    def update(self):
        print("Update Details")
        self.mname = input("Update Movie Name : ")
        self.aname = input("Update Artist Name : ")
        self.yr = input("Update year of release : ")
        self.rt = input("Update rating : ")
        
ob6 = MovieDetails("Sanju","Ranbir","2018,"10")
ob6.display()
ob6.update()
ob6.display()
