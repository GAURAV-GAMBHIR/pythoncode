print("\n\n")
list4 = [input("Enter element : ") for x in range(10)]
x = input("\nEnter element to be deleted : ")

for y in range(len(list4)):
    if x==list4[y] :
        del list4[y]
        break;
print("After deletion : ",list4)
