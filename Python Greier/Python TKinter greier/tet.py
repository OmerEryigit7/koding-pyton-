from tkinter import *
from pytube import *
 
window = Tk()
window.geometry("500x500")
 
 
def Download():
    YouTubelink = linkEntry.get()
    yt = YouTube(YouTubelink)
    stream = yt.streams.get_highest_resolution()
    stream.download()
 
frame1 = Frame(window)
frame1.pack()
linkLabel = Label(frame1, text="Lenke")
linkLabel.pack(side=LEFT)
linkEntry = Entry(frame1)
linkEntry.pack(side=LEFT)
 
downloadButton= Button(window, text="last ned", command=Download)
 
frame2 = Frame(window)
frame2.pack(pady=10)
downloadLocationLabel = Label(frame2, text="Nedlastningsmål")
downloadLocationLabel.pack(side=LEFT)
downloadLocationEntry = Entry(frame2)
downloadLocationEntry.pack(side=LEFT)
downloadButton.pack()
 
 
window.mainloop()