import tkinter as tk
from tkinter import *
from youtube_dl import YoutubeDL
import os, glob,sys
import sys

window=tk.Tk()
window.title("Download .mp3 youtube")
window.geometry('490x180')
Label(window, text = "Tải file youtube",
          background = 'red', foreground ="white",
          font = ("Times New Roman BOLD", 15)).grid(column= 2, row = 1)
          
Label(window, text = "18004135 - Nguyễn Mạnh Tiến", foreground ="black",
          font = ("Times New Roman BOLD", 10)).grid(column= 2, row = 2)

Label(window, text = "Đường link:",
          font = ("Times New Roman", 10)).grid(column=1, row =3)
link_per = Entry(window, width = 50)
link_per.grid(column = 2, row = 3)
dl = YoutubeDL()

def my_hook(d):
    if d['status'] == 'finished':
        print('--- DOWNLOAD --- Quá trình tải xuống đã hoàn thành')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '171'
    }],
    'noplaylist' : True,
    'progress_hooks': [my_hook]
}


def download():
    try:
        link = link_per.get()
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            return NONE
    except:
        print("--- DOWNLOAD --- LỘN ĐƯỜNG DẪN RỒI KÌA")

def renamem4u():
    folder = 'M:\Music\youtube'
    try:
        for filename in os.listdir(folder):
            infilename = os.path.join(folder,filename)
            if not os.path.isfile(infilename):
                continue
            oldbase = os.path.splitext(filename)
            newname = infilename.replace(".m4a", ".webm")
            output = os.rename(infilename, newname)
    except PostProcessingError as e: 
        print("--- RENAME --- HMMM ! ! !")

def rename():
    folder = 'M:\Music\youtube'
    count = 0
    try:
        renamem4u()
        for filename in os.listdir(folder):
            infilename = os.path.join(folder,filename)
            if not os.path.isfile(infilename):
                continue
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.webm', '.mp3')
            count= count + 1
            output = os.rename(infilename, newname)
        count = count - 1
        dem = str(count)
        print("--- RENAME --- Đã đổi đuôi file(s) .webm thành .mp3. Hiện tại có "+dem+" files .mp3")
    except PostProcessingError as e: 
        print("--- RENAME --- HÌNH NHƯ ĐÃ CÓ LỖI GÌ Ở HÀM (RENAME) RỒI ! ! !")

def openfolder():
    path = os.getcwd()
    path = os.path.realpath(path)
    os.startfile(path)

openfolder = Button(window, text="Mở thư mục", command = openfolder, width = 10).grid(column =3, row=3)
Button(window, text="tải", command=download, width = 40).grid(column = 2, row = 6)
remp3 = Button(window, text="đổi tên", command=rename, width = 40)
remp3.grid(column = 2, row = 8)
window.mainloop()

