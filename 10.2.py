def numthread():
    for x in range(1,11):
        time.sleep(1)
        print(x)

print()
t2 = Thread(target = numthread)
t2.start()
