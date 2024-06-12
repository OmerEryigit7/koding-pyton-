from tkinter import *
from tkinter import colorchooser

def add():
    listybox.insert(listybox.size(), entry1.get())
    listybox.config(height=listybox.size())


def delete():
    for index in reversed(listybox.curselection()):
        listybox.config(height=listybox.size() - 1)
        listybox.delete(index)

def colorchange():
    window.config(bg=colorchooser.askcolor()[1])




    listybox.config(height=listybox.size())

window = Tk()

listybox = Listbox(window,
                   font=("Constantia", 35),
                   width=12,
                   bg="gray",
                   selectmode=MULTIPLE)

addbutton = Button(window,
                      font=("Impact", 30),
                      text="add",
                      command=add)

removebutton = Button(window,
                      font=("Impact", 30),
                      text="remove",
                      command=delete)

colorbutton = Button(window,
                      font=("Impact", 30),
                      text="Color Theme",
                      command=colorchange)

entry1 = Entry(window)

listybox.pack(pady=75)
entry1.pack()
addbutton.pack(pady=2)
removebutton.pack(pady=2)
colorbutton.pack(pady=2)

listybox.insert(1, "Your own house")
listybox.insert(4, "Bosnia")
listybox.insert(5, "Saturn")

listybox.config(height=listybox.size())

window.mainloop()