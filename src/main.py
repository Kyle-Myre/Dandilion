from tkinter import StringVar , PhotoImage
import customtkinter as ctk
from pytube import YouTube
import pytube.request
import os

pytube.request.default_range_size = 9437184 #MB

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

App = ctk.CTk()

full_image_path = os.path.join(os.getcwd() , "assets" , "Icon.ico")

App.iconbitmap(full_image_path)

def Download(link:str):

    if options.get() == "MP4":
        try:

            FinishLabel.configure(text="" , fg_color="transparent")
            Y_obj = YouTube(link , use_oauth=False , allow_oauth_cache=True)
            Y_obj.register_on_progress_callback(on_progress)

            video = Y_obj.streams.get_highest_resolution()

            VideoTitle.configure(text=video.title)
            video.download("./output")
            
            FinishLabel.configure(text="Finished", fg_color="transparent")

        except Exception as error:

            FinishLabel.configure(text=error , fg_color="red")
    
    elif options.get() == "MP3":
        try:
            FinishLabel.configure(text="" , fg_color="transparent")
            Y_obj = YouTube(link , use_oauth=False , allow_oauth_cache=True)
            Y_obj.register_on_progress_callback(on_progress)

            video = Y_obj.streams.filter(only_audio=True).first()
            
            VideoTitle.configure(text=video.title)
            output_file = video.download("./output")

            name , ext = os.path.splitext(output_file)
            new_file = name + ".mp3"

            os.rename(output_file , new_file)
            
            FinishLabel.configure(text="Finished", fg_color="transparent")

        except Exception as error:

            FinishLabel.configure(text=error , fg_color="red")


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    
    Progress.configure(text=f"{str(pct_completed)}%")
    Progress.update()

    ProgressBar.set(float(pct_completed) / 100)


# UI
__Types = ['MP3' , 'MP4']
options = StringVar(value=__Types[0])
value = StringVar()

App.geometry("480x320")
App.resizable(False , False)

App.title("Dandilion")

Entry_Label = ctk.CTkLabel(App , text="Put a Video Link")
Entry_Label.pack(padx=5 , pady=5)

Entry = ctk.CTkEntry(App , width=370 , height=25 , textvariable=value)
Entry.pack(padx=5 , pady=5)

Type = ctk.CTkOptionMenu(App , variable=options , values=__Types)
Type.pack(padx=5 , pady=5)

FinishLabel = ctk.CTkLabel(App,text="")
FinishLabel.pack()

Download_Button = ctk.CTkButton(App , text="Download" , command=lambda:Download(value.get()))
Download_Button.pack(padx=5 , pady=5)

VideoTitle = ctk.CTkLabel(App , text="")
VideoTitle.pack()

Progress = ctk.CTkLabel(App,text="0%")
Progress.pack()

ProgressBar = ctk.CTkProgressBar(App , width=350)
ProgressBar.set(0)

ProgressBar.pack()


App.mainloop()