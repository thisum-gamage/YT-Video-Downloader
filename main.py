# https://youtu.be/9wafxM-vA0E

import tkinter as tk
import yt_dlp
import threading
from tkinter import ttk
from tkinter import filedialog

selected_path = ""

# Functions


def start_download_thread():
    thread = threading.Thread(target=download_video)
    thread.start()


def select_folder():
    global selected_path
    selected_path = filedialog.askdirectory()
    path_label.config(text=selected_path)


def download_video():
    try:
        title_label.config(text="")  # Empty method after 1 cycle
        length_label.config(text="")  # Empty method after 1 cycle
        size_label.config(text="")  # Empty method after 1 cycle

        # if block for when user not select a file path
        if not selected_path:
            save_dir = "."
        else:
            save_dir = selected_path

        # Telling to ydl-dlp about user browsed folder
        ydl_opts = {"outtmpl": f"{save_dir}/%(title)s.%(ext)s"}

        # Assign ttk entry url input to url var
        url = url_input.get()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            down_btn.config(state="disabled")

            info_dict = ydl.extract_info(url, download=False)

            # Getting video details & config
            video_title = info_dict.get("title", None)
            video_duration = info_dict.get("duration", None)
            minutes, seconds = divmod(video_duration, 60)
            bytes_size = (
                info_dict.get("filesize") or info_dict.get("filesize_approx") or 0
            )
            video_size_mb = round(bytes_size / (1024 * 1024), 2)

            # Label printing
            title_label.config(text=f"Title : {video_title}")
            length_label.config(text=f"Video Length : {minutes}:{seconds}")
            size_label.config(text=f"Size : {video_size_mb} MB")
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

# root windows design
diplay_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

width, height = 450, 350
left = int(diplay_width / 2 - width / 2)
top = int(display_height / 2 - height / 2)

root.title("YouTube Video Downloader")
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap("macos_big_sur_download_folder_icon_186042.ico")
root.resizable(False, False)

# labels

label = tk.Label(root, text="Paste your YouTube video URL", font=("Arial", 11))
label.pack(pady=10)

url_input = ttk.Entry(root, width=50)
url_input.pack(pady=5)

browse_btn = ttk.Button(root, text="Browse", command=select_folder)
browse_btn.pack(pady=5)

# ttk config for download button
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

# labels
status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

title_label = tk.Label(root, text="", wraplength=400)
title_label.pack(pady=2)

length_label = tk.Label(root, text="")
length_label.pack(pady=2)

size_label = tk.Label(root, text="")
size_label.pack(pady=2)

path_label = ttk.Label(root, text="No folder selected", font=("Arial", 9, "italic"))
path_label.pack(pady=5)


root.mainloop()
