from tkinter import *

root = Tk()
root.geometry("1600x800")
root.title("Assignment")

def root_exit():
    root.destroy()

def show_text():
    l2 = Label(f1,font = ("Algerian",30), text = "Did you clicked that button")
    l2.grid()

f1 = Frame(root)
f1.pack(side = TOP)

l1 = Label(f1,font = ("Algerian",20), text = "Hello World")
l1.grid()

b1 = Button(f1,font = "Arial", text = "Exit",command = root_exit)
b1.grid()
