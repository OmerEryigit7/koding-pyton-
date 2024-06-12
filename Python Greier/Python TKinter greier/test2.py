from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="What the fuck?",
                       #message="Why'd you click it?")
    
    if messagebox.askyesno(title='Question',
                              message="Are you retarded?"):
        print("fr? me too")
    else:
        print("ok")


window = Tk()

button = Button(window,
                command=click,
                text="Don't. Click. This. Button. pls")


button.pack()

window.mainloop()