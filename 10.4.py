import math

def fact():
    print("\nFactorial of 5 : ",math.factorial(5))

t4 = Thread(target = fact)
t4.start()


