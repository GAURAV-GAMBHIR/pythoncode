def fact(n):
    if n == 0 or n == 1:
        return 1
    if n>0:
        return n*fact(n-1)

dicfac = {x:fact(x) for x in range(11)}
print("\nDictionary with numbers and their factorial : \n",dicfac)
