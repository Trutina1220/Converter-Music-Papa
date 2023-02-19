from tkinter import *
from tkinter.ttk import Label, Style
import tkinter.messagebox as messagebox
import os 
import shutil


import yt_dlp
from yt_dlp.postprocessor.common import PostProcessor


#Global variable to use once
lastMusic =""
source = os.getcwd()
destination = "E:"  # E drive for the destination


# Youtube download options
class MyCustomPP(PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info

ydl_opts ={
    'format': 'bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'forcefilename': 'True',

    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
        
    }],
}







#Developing GUI for the converter using Tkinter

master = Tk()
master.title("Converter Youtube Papa")
w = 800 # width for the Tk master
h = 600 # height for the Tk master

# get screen width and height
ws = master.winfo_screenwidth() # width of the screen
hs = master.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk master window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
Label(master, text="Youtube Link",font=("Arial",20)).grid(row=0, pady=50)

#Entry field for youtube link 
e1= Entry(master,  width=50, font=("Arial",12))
e1.grid(row=1, column = 0)

Label(master, text="Music Yang Udah Masuk", font=("Arial",20)).grid(row=2, pady=10)


# Music list box to show how many music downloaded
musicListBox = Listbox(master, width=50, font=("Arial",15))
musicListBox.grid(row =3 , column=0)

# Setting up the vertical scroll bar
y_scrollbar = Scrollbar(master)
y_scrollbar.grid(row=3, column=1, sticky=N+S)

#Setting up the horizontal scroll bar 
x_scrollbar = Scrollbar(master, orient=HORIZONTAL)
x_scrollbar.grid(row=4, sticky = E+W)



musicListBox.config(yscrollcommand= y_scrollbar.set, xscrollcommand= x_scrollbar.set )

y_scrollbar.config(command= musicListBox.yview)
x_scrollbar.config(command=musicListBox.xview)


# Button function to download 
def download():
    global lastMusic, source, destination
    #Check if the link is empty or not 
    if e1.get() != "":
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: #loading up the youtube downloader library
            ydl.add_post_processor(MyCustomPP())
            try:
                info = ydl.extract_info(e1.get(), download = True) #Download music 
                e1.delete(0,'end') #Emptying youtube link entry

                #Preparing the file name
                lastMusic = ydl.prepare_filename(info)
                lastMusic = lastMusic.rsplit('.',1)
                lastMusic = lastMusic[0] +".mp3"
                #Displaying the file name in the downloaded music
                musicListBox.insert(0, lastMusic)

                #Copy the file to the flash disk
                movedFile = shutil.copy(os.path.join(source,lastMusic), destination+lastMusic)
                messagebox.showinfo(title='Info',message="Music sudah masuk usb")
            

            except Exception as e:
                print(e)
                messagebox.showerror(title='Error',message="Link biru youtube salah, masukin link biru youtube lagi")
    
    else: 
        messagebox.showerror(title='Error',message="Masukan link biru biru youtube yang udah di ctrl + c")
        
b1 = Button(master, text="Download", font=("Arial",14), activebackground="grey", border=10, foreground= "grey", command=download)
b1.grid(row=1, column=1, padx=1, pady=20)
mainloop()
