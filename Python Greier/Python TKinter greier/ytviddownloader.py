from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
from pydub import AudioSegment
import os

def download_video():
    audiodownload = choice()
    link = url_entry.get()
    download_folder = download_path.get()
    try:
        getVid = YouTube(link)
        if audiodownload == True:
            stream = getVid.streams.filter(only_audio=True).first()
            stream.download(download_folder)
            video_file = stream.download(download_folder)
            audio = AudioSegment.from_file(video_file)
            audio_path = os.path.splitext(video_file)[0] + ".mp3"
            audio.export(audio_path, format="mp3")
            os.remove(video_file)


            

        else:
            stream = getVid.streams.get_highest_resolution()
            stream.download(download_folder)
        messagebox.showinfo(title="Downloaded", message="Downloaded Successfully!")
    except:
        messagebox.showerror(title="Error", message="Invalid URL/Unsuccessful download")

def browsedestination():
    download_directory = filedialog.askdirectory(initialdir="YOUR PATH", title="save video")
    download_path.set(download_directory)

def choice():
    if (x.get()==0):
        audiodownload = True
    else:
        audiodownload = False
    
    return audiodownload


root = Tk()

download_path = StringVar()

choicelist = ["mp3", "mp4"]

x = IntVar()

root.geometry("800x400")

mainlabel = Label(root,
                  text="Youtube Video Downloader",
                  font=("Arial", 50))

label1 = Label(root,
               text="Enter video URL:",
               font=("italic", 20))

destinationlabel = Label(root, text="Selected path:")

root.destinationtext = Entry(root, width=40, textvariable=download_path, font=("arial"))


url_entry = Entry(root, width=60)


Downloadbutton = Button(root, text="Download", command=download_video)
browsebutton = Button(root, text="browse download location", width=20, command=browsedestination, relief=GROOVE)



mainlabel.pack()
label1.pack()
url_entry.pack(pady=(0, 20))

for index in range(len(choicelist)):
    radiobutton = Radiobutton(root,
                              text=choicelist[index],
                              variable=x,
                              value=index,
                              command=choice)
    radiobutton.pack()

browsebutton.pack(pady=(20, 0))
root.destinationtext.pack()
Downloadbutton.pack(pady=(20, 0))


root.mainloop()