from tkinter import *
import random



def clear():
    label2.config(text=password)


def copy():
    global newpasword
    window.clipboard_clear()
    window.clipboard_append(newpasword)

def submit():
    global newpasword
    global password
    length = 0
    if entry1.get().isdigit():
        length = int(entry1.get())
    if length >= minimumpasslen and length <= maximumpasslen:
        removeall()
        for i in range(0, length):
            password = password + random.choice(randomchars)
        label2.config(text=password)
        newpasword = str(password)
        password = ""
        errorlabel.pack_forget()
    else:
        errorlabel.pack()
    password = ""

def removeall():
    entry1.delete(0, END)

def validate_entry(text):
    return text.isdigit()

window = Tk()
window.title("Random Assword Generator")
window.geometry('820x420')

randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
password = ""
newpasword = ""

minimumpasslen = 6
maximumpasslen = 60


label1 = Label(window,
               text="how many characters should your password be? (" + str(minimumpasslen) +"-"+ str(maximumpasslen) +" characters)",
               font=("arial", 25))


entry1 = Entry(window,
               font=('arial', 20),
               validate="key",
               validatecommand=(window.register(validate_entry), "%S"))



label2 = Label(window,
               text="Random Password will generate here")

errorlabel = Label(window,
               text="Password length requirements not met (" + str(minimumpasslen) +"-"+ str(maximumpasslen) +" characters)",
               fg="red")

submitbutton = Button(window,
                      text="submit",
                      command=submit)

copybutton = Button(window,
                    text="Copy Password",
                    command=copy)

clearpassbutton = Button(window,
                         text="Clear Password",
                         command=clear)

label1.pack(pady=30)
entry1.pack(pady=5)
submitbutton.pack(pady=5)
label2.pack(pady=5)
copybutton.pack(pady=5)
clearpassbutton.pack(pady=5)

window.mainloop()
