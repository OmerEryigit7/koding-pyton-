from tkinter import *
from PIL import Image, ImageTk 

def submit():
    username = entry.get()
    print("Hello, Mr. " + username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

def display():
    if(x.get()==1):
        print("balls")
    else:
        print("No balls")

window = Tk()
window.title("Eating a burger with no honey mustard")
window.geometry("420x420")

x = IntVar()

img = Image.open("Images/ydH2c6IcxRc7MSFEq7b5-x7Zr9KZrbgX720xrjSMoSk.gif")
resized_image= img.resize((150,150))
pic1 = ImageTk.PhotoImage(resized_image)

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black") 

enter_button = Button(window,
                      text="Enter",
                      command=submit)

delete_button = Button(window,
                      text="Delete",
                      command=delete)

backspace_button = Button(window,
                      text="Backspace",
                      command=backspace)

check_button = Checkbutton(window,
                           text="I agree that I am severely addicted to fentanyl and cocaine",
                           font=("Arial", 15),
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           image=pic1,
                           compound="bottom")




enter_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)
entry.pack(side=LEFT)
check_button.pack(side=RIGHT)

window.mainloop()
