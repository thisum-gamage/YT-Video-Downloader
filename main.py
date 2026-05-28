# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog


# def download_video(url, save_path):
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive=True, file_extension="mp4")
#         highest_res_stream = streams.get_highest_resolution()
#         highest_res_stream.download(output_path=save_path)
#         print("Video Downloaded Successfully!!!")
#     except Exception as e:
#         print(e)

# https://youtu.be/9wafxM-vA0E

from pytube import YouTube
import tkinter as tk


def download_video():
    try:
        url = url_input.get()

        title_label.config(text="")
        length_label.config(text="")
        
        yt = YouTube(url)
        title_label.config(text=f"Title: {yt.title}")

        minutes, seconds = divmod(yt.length, 60)
        length_label.config(text=f"Video Length: {minutes}:{seconds}")

        status_label.config(text="Downloading...", fg="blue")
        root.update_idletasks()

        video = yt.streams.get_highest_resolution()
        video.download()

        status_label.config(text="Download Completed! 🎉", fg="green")
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
    command=download_video,
    bg="red",
    fg="white",
    font=("Arial", 10, "bold"),
)
down_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

title_label = tk.Label(root, text="", wraplength=400)
title_label.pack(pady=10)

length_label = tk.Label(root, text="")
length_label.pack(pady=10)

root.mainloop()
