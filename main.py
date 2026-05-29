# https://youtu.be/9wafxM-vA0E

import tkinter as tk
import yt_dlp
import threading


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
    except Exception as e:
        print(e)
        status_label.config(text="Please enter valid url!!!", fg="red")


# GUI Design

root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry("450x350")

label = tk.Label(root, text="Paste your YouTube video URL :-", font=("Arial", 11))
label.pack(pady=10)

url_input = tk.Entry(root, width=50)
url_input.pack(pady=5)

down_btn = tk.Button(
    root,
    text="Download",
    command=start_download_thread,
    bg="red",
    fg="white",
    font=("Arial", 10, "bold"),
)
down_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

title_label = tk.Label(root, text="", wraplength=400)
title_label.pack(pady=2)

length_label = tk.Label(root, text="")
length_label.pack(pady=2)

root.mainloop()
