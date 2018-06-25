def delaythread():
    lis = [5,4,8,7,6]
    for x,y in zip(range(6),lis):
        time.sleep(2*x)
        print(y)

print()
t3 = Thread(target = delaythread)
t3.start()
