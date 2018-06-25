def perfect(n):
    summ = 0
    for x in range(1,int(n/2)+1):
        if n%x == 0:
            summ+=x
    if summ == n:
        return "a Perfect Number"
    else:
        return "Not a Perfect number"

result = print(perfect(int(input("\nEnter a number : "))))

print("\nPerfect Numbers between 1 and 100 are : ")
for y in range(1,1000):
    result = perfect(y)
    if result == True:

        print(y)
