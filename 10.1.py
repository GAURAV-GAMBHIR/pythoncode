from threading import *
import time

def thread():
    time.sleep(5)
    print("This is "+str(current_thread().getName()))

t1 = Thread(target = thread)
t1.start()
