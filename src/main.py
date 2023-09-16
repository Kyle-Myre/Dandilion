from tkinter import StringVar
from pytube import YouTube 
import customtkinter as ct



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

        self.Download_Button = ct.CTkButton(self , text="Download" , command=lambda:print(self.options.get()))
        self.Download_Button.pack(padx=5 , pady=5)

        self.Progress = "";
        self.ProgressBar = "";

        self.mainloop()

App()