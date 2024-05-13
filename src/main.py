# imports
try:
    import pytube.request
    import tkinter as tk
    from threading import Thread
    from pytube import YouTube
    from os import path, rename
    from datetime import datetime
    from rich.console import Console
    from tkinter import StringVar
    from tkinter import ttk

except (ImportError, ImportWarning) as err:
    print(f"Missing Library Error : {err}")

pytube.request.default_range_size = 10000  # 10 GB
console = Console()

App = tk.Tk()

icon_relative_path = ""

icon_relative_path = path.join(path.dirname(__file__), 'assets', 'public', 'Icon.ico')

App.iconbitmap(icon_relative_path)

theme_relative_path = path.join(path.dirname(__file__), 'assets', 'themes', 'forest-dark.tcl')
App.tk.call('source', theme_relative_path)
ttk.Style().theme_use('forest-dark')

def Download(link: str):
    FinishLabel.configure(text="Fetching . . .", foreground="#FFFF00")

    if link == "":
        FinishLabel.configure(text="Empty Link")
        FinishLabel.configure(text="")

        return None

    Y_obj = YouTube(link, use_oauth=False, allow_oauth_cache=True)
    Y_obj.register_on_progress_callback(on_progress)

    if options.get() == "MP4":
        try:
            video = Y_obj.streams.get_highest_resolution()
            VideoTitle.configure(text=video.title)

            FinishLabel.configure(text="Video founded")

            video.download("./output")

            FinishLabel.configure(text="Finished", foreground="green")
            FinishLabel.configure(text="")

        except Exception as error:
            FinishLabel.configure(text=error, foreground="red")

    elif options.get() == "MP3":
        try:
            video = Y_obj.streams.filter(only_audio=True).first()

            FinishLabel.configure(text="Video founded")

            VideoTitle.configure(text=video.title)
            output_file = video.download("./output")

            name, _ = path.splitext(output_file)
            new_file = name + ".mp3"

            rename(output_file, new_file)

            FinishLabel.configure(text="Finished", foreground="green")
            FinishLabel.configure(text="")

        except Exception as error:
            FinishLabel.configure(text=error, foreground="red")

def on_progress(stream, _, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100

    Progress['value'] = pct_completed
    Progress_Label.configure(text=f"{int(pct_completed)}%")

# UI
__Types = ["", "MP3", "MP4"]
options = StringVar(App)

options.set('Select An Option')

value = StringVar()

App.geometry("480x320")
App.resizable(False, False)

App.title("Dandilion")

Entry_Label = ttk.Label(App, text="Put a Video Link")
Entry_Label.pack(padx=5, pady=5)

Entry = ttk.Entry(App, width=370, textvariable=value)
Entry.pack(padx=10, pady=10)

Type = ttk.OptionMenu(App, options, *__Types)
Type.pack(padx=5, pady=5)

FinishLabel = ttk.Label(App, text="")
FinishLabel.pack()

Download_Button = ttk.Button(App, text="Download", style='Accent.TButton', command=lambda: Thread(
    target=Download, args=(value.get(), )).start())
Download_Button.pack(padx=5, pady=5)

VideoTitle = ttk.Label(App, text="")
VideoTitle.pack()

Progress = ttk.Progressbar(App, orient="horizontal", length=300, mode="determinate")
Progress.pack(padx=5, pady=5)

Progress_Label = ttk.Label(App, text="")
Progress_Label.pack()

def main():
    console.print(f"[blue]Dandilion[/] Has Started at {datetime.now()}")

    console.print("[yellow]{}[/] Loaded".format(icon_relative_path))
    console.print("[yellow]{}[/] Loaded".format(theme_relative_path))

    App.mainloop()

main()
