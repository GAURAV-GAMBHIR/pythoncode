t = time.localtime()
t = time.mktime(t)
print(time.strftime("\n%m i.e %b",time.gmtime(t)))
