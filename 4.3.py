first=int(input("Enter  age of 1st person:"))
second=int(input("Enter age of 2nd person"))
third=int(input("Enter age of 3rd person"))
if first<second and first<third:
    print("First person is younger")
elif second<first and second<third:
    
    print("2nd person is younger")
elif third<first and third<second:
    
    print("Third person is younger")
elif first==second or second==third or first==third:
    print("All are of same age")
else:
    print("cant tell")
