from tkinter import StringVar
from pytube import YouTube 
import customtkinter as ct
from threading import Thread
from time import sleep


class App(ct.CTk):

    _SETTINGS = {
        # pass
    }

    ct.set_appearance_mode("System")
    ct.set_default_color_theme("green")

    def __init__(self):
        super().__init__()

        self.geometry("480x480")

        self.Entry_Label = ct.CTkLabel(self , text="Put a Video Link")
        self.Entry_Label.pack(padx=5 , pady=5)

        self.value = StringVar()

        self.Entry = ct.CTkEntry(self , width=370 , height=25 , textvariable=self.value)
        self.Entry.pack(padx=5 , pady=5)

        self.__Types = ['MP3' , 'MP4']
        self.options = StringVar(value=self.__Types[0])

        self.Type = ct.CTkOptionMenu(self , variable=self.options , values=self.__Types)
        self.Type.pack(padx=5 , pady=5)

        self.FinishLabel = ct.CTkLabel(self,text="")
        self.FinishLabel.pack()

        print(self.FinishLabel._fg_color)

        self.Download_Button = ct.CTkButton(self , text="Download" , command=lambda:self.Download(self.value.get()))
        self.Download_Button.pack(padx=5 , pady=5)

        self.Progress = ct.CTkLabel(self,text="0%")
        self.Progress.pack()

        self.ProgressBar = ct.CTkProgressBar(self , width=350)
        self.ProgressBar.pack()

        self.mainloop()

    def Download(self , link:str):
        try:
            
            self.FinishLabel.configure(text="" , fg_color="transparent")
            Y_obj = YouTube(link , use_oauth=False , allow_oauth_cache=True)

            video = Y_obj.streams.get_highest_resolution()
            video.download("./output")
            
            self.FinishLabel.configure(text="Finished", fg_color="transparent")

        except Exception as error:
            self.FinishLabel.configure(text=error , fg_color="red")

App()