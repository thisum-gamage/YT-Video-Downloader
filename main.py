# https://youtu.be/9wafxM-vA0E

import tkinter as tk
import yt_dlp
import threading
from tkinter import ttk
from tkinter import filedialog

selected_path = ""

# ====================================Functions==============================================


def start_download_thread():
    thread = threading.Thread(target=download_video)
    thread.start()


def progress_hook(d):
    if d["status"] == "downloading":
        total_bytes = d.get("total_bytes") or d.get("total_bytes_approx", 1)
        downloaded_bytes = d.get("downloaded_bytes", 0)

        percentage = (downloaded_bytes / total_bytes) * 100

        progress["value"] = percentage
        root.update_idletasks()


def select_folder():
    global selected_path
    selected_path = filedialog.askdirectory()
    path_label.config(text=selected_path)


def download_video():
    try:
        # --Empty method after 1 cycle--
        title_label.config(text="")
        length_label.config(text="")
        size_label.config(text="")
        progress["value"] = 0

        # if block for when user not select a file path
        if not selected_path:
            save_dir = "."
        else:
            save_dir = selected_path

        # quality selection
        selected_quality = quality_box.get()

        if selected_quality == "720p":
            video_format = "bestvideo[height<=720]+bestaudio/best"
        elif selected_quality == "480p":
            video_format = "bestvideo[height<=480]+bestaudio/best"
        elif selected_quality == "360p":
            video_format = "bestvideo[height<=360]+bestaudio/best"
        elif selected_quality == "144p":
            video_format = "bestvideo[height<=144]+bestaudio/best"
        else:
            video_format = "best"

        # Telling to ydl-dlp about user browsed folder etc
        ydl_opts = {
            "outtmpl": f"{save_dir}/%(title)s.%(ext)s",
            "progress_hooks": [progress_hook],
            "format": video_format,
        }

        # Assign ttk entry url input to url var
        url = url_input.get()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            down_btn.config(state="disabled")

            info_dict = ydl.extract_info(url, download=False)

            # --------------------Getting video details & config-------------------------
            video_title = info_dict.get("title", None)
            video_duration = info_dict.get("duration", None)
            minutes, seconds = divmod(video_duration, 60)
            bytes_size = (
                info_dict.get("filesize") or info_dict.get("filesize_approx") or 0
            )
            video_size_mb = round(bytes_size / (1024 * 1024), 2)

            # ---------------------Label printing---------------------------
            title_label.config(text=f"Title : {video_title}")
            length_label.config(text=f"Video Length : {minutes}:{seconds}")
            size_label.config(text=f"Size : {video_size_mb} MB")
            status_label.config(text="Downloading...", fg="blue")

            root.update_idletasks()
            ydl.download([url])

            progress["value"] = 100

            status_label.config(text="Download Completed!", fg="green")

            url_input.delete(0, tk.END)
            down_btn.config(state="enabled")
    except Exception as e:
        print(e)
        status_label.config(text="Please enter valid url!!!", fg="red")
        url_input.delete(0, tk.END)
        down_btn.config(state="enabled")


# =====================================GUI Design=========================================
# --------------------------------root windows design--------------------------------------
root = tk.Tk()

diplay_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

width, height = 500, 500
left = int(diplay_width / 2 - width / 2)
top = int(display_height / 2 - height / 2)

root.title("YouTube Video Downloader")
root.geometry(f"{width}x{height}+{left}+{top}")
root.iconbitmap("macos_big_sur_download_folder_icon_186042.ico")
root.resizable(False, False)

# ------------------------------------labels_1---------------------------------------

label = tk.Label(root, text="Paste your YouTube video URL", font=("Arial", 11))
label.pack(pady=8)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

url_input = ttk.Entry(input_frame, width=50)
url_input.pack(side="left", padx=5)

browse_btn = ttk.Button(input_frame, text="Browse", command=select_folder)
browse_btn.pack(side="left", padx=5)

quality_label = tk.Label(root, text="Select Quality:")
quality_label.pack(pady=2)

quality_box = ttk.Combobox(
    root, values=["Best", "720p", "480p", "360p", "144p"], state="readonly"
)
quality_box.set("Best")
quality_box.pack(pady=5)

# ----------------------ttk config for download button-------------------------
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

# -------------------------------labels_2----------------------------------
status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

title_label = tk.Label(root, text="", wraplength=400)
title_label.pack(pady=2)

length_label = tk.Label(root, text="")
length_label.pack(pady=2)

size_label = tk.Label(root, text="")
size_label.pack(pady=2)

# ----------------------ttk config for progress bar-------------------------
style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#ffffff",
    background="#2ecc71",
    bordercolor="#2c3e50",
    lightcolor="#2ecc71",
    darkcolor="#2ecc71",
)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate",
    style="Custom.Horizontal.TProgressbar",
)
progress.pack(pady=10)

# ------------------------------------labels_3----------------------------------------
path_label = ttk.Label(root, text="No folder selected", font=("Arial", 9, "italic"))
path_label.pack(pady=5)


root.mainloop()
