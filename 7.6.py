t = time.localtime()
t = time.mktime(t)
print(time.strftime("\n%r",time.gmtime(t)))
