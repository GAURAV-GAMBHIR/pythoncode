f2 = Frame(root)
f2.pack()

flag = 0

def change_text():
    global flag
    if flag == 0:
        l3.config(text = "Now You Don't")
        flag = 1
    else:
        l3.config(text = "Now You See Me")
        flag = 0
    

l3 = Label(f2,font = ("Helvetica",20),text = "Now You See Me")
l3.grid()

b3 = Button(f2,text = "Don't click", command = change_text)
b3.grid()
b4 = Button(f2, text = "End your life", command = root_exit)
b4.grid()
