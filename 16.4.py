def change_it():
    text_variable = e1.get()
    l5 = Label(f2,font = ("Helvetica",30),text = text_variable)
    l5.grid()

l4 = Label(f2,font = ("Helvetica",30),text = "Enter Whatever you want : ")
l4.grid(row = 5,column = 0)

e1 = Entry(f2)
e1.grid(row = 5, column = 1)

b5 = Button(f2,text = "See Magic", command = change_it)
b5.grid()

root.mainloop
