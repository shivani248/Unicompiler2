import tkinter as tk
from tkinter import*

from pytube import YouTube
from tkinter import filedialog,messagebox
import os

def widgets():
    label_yt = Label(root,text="YouTube URL :" , bg="white")
    label_yt.grid(row=1,column=0,padx=3,pady=3)

    root.text = Entry(root,width=65,textvariable=videolink)
    root.text.grid(row=1,column=1,padx=10,pady=10)

    des_label=Label(root,text="Video Path", bg= "white")
    des_label.grid(row=2,column=0,padx=4,pady=4)

    root.des_text= Entry(root, width=50, textvariable=download)
    root.des_text.grid(row=2,column=1,padx=5,pady=5)

    browsebutton= Button(root , text="browse", command=browse, width=5,bg="white")
    browsebutton.grid(row=2,column=2,padx=4,pady=4)

    downloadbutton=Button(root, text="download video", command= downloadvideo , width=35,bg="white")
    downloadbutton.grid(row=3,column=1,padx=5,pady=5)
    

def browse():
    directory=filedialog.askdirectory(initialdir="Your directory")
    download.set(directory)

def downloadvideo():
    url= videolink.get()
    folder= download.get()
    getvideo = YouTube(url)
    getstream = getvideo.streams.first()
    getstream.download(folder)

    messagebox.showinfo("success","You have downloaded the video " +folder)





root = tk.Tk()
root.geometry('560x170')
root.configure(bg='pink')
root.resizable(False,False)
root.title(" Youtube Downloader")


download=StringVar()
videolink=StringVar()

widgets()

root.mainloop()
