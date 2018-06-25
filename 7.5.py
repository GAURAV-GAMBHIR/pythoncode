t = time.localtime()
t = time.mktime(t)
print(time.strftime("\nToday is : %d",time.gmtime(t)))
