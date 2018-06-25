def table(n):
    if n>0:
        table(n-1)
        print("12 x",n,"=",12*n)

table(10)

