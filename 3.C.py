import operator
d={"shivam":80,"ashish":75,"sahil":90,"prince":50,"vinay":40}
sorted_d = sorted(d.items(), key=lambda x: x[1])
print(sorted_d)
a="MISSISSIPPI"
b={'M':a.count('M'),'I':a.count('I'),'S':a.count('S'),'p':a.count('P')}
print(b)
