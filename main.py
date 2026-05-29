# https://youtu.be/9wafxM-vA0E

import tkinter as tk
import yt_dlp
import threading
from tkinter import ttk

# from tkinter import filedialog

# selected_path = filedialog.askdirectory()


def start_download_thread():
    thread = threading.Thread(target=download_video)
    thread.start()


def download_video():
    try:
        title_label.config(text="")
        length_label.config(text="")

        ydl_opts = {}

        url = url_input.get()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            down_btn.config(state="disabled")

            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get("title", None)
            video_duration = info_dict.get("duration", None)

            title_label.config(text=f"Title : {video_title}")

            minutes, seconds = divmod(video_duration, 60)
            length_label.config(text=f"Video Length : {minutes}:{seconds}")

            status_label.config(text="Downloading...", fg="blue")
            root.update_idletasks()
            ydl.download([url])

            status_label.config(text="Download Completed!", fg="green")

            url_input.delete(0, tk.END)
            down_btn.config(state="enabled")
    except Exception as e:
        print(e)
        status_label.config(text="Please enter valid url!!!", fg="red")
        url_input.delete(0, tk.END)
        down_btn.config(state="enabled")


# GUI Design

root = tk.Tk()

diplay_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

width, height = 450, 350
left = int(diplay_width / 2 - width / 2)
top = int(display_height / 2 - height / 2)

root.title("Youtube Video Downloader")
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap("macos_big_sur_download_folder_icon_186042.ico")
root.resizable(False, False)


label = tk.Label(root, text="Paste your YouTube video URL :-", font=("Arial", 11))
label.pack(pady=10)

url_input = ttk.Entry(root, width=50)
url_input.pack(pady=5)

style = ttk.Style()
style.theme_use("alt")
style.configure(
    "Custom.TButton",
    background="#1ef4ff",
    foreground="black",
    font=("Arial", 10, "bold"),
)

down_btn = ttk.Button(
    root,
    text="Download",
    command=start_download_thread,
    style="Custom.TButton",
)
down_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

title_label = tk.Label(root, text="", wraplength=400)
title_label.pack(pady=2)

length_label = tk.Label(root, text="")
length_label.pack(pady=2)

root.mainloop()
