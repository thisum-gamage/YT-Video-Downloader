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


from pytube import YouTube
import tkinter as tk


def download_video():
    try:
        url = url_input.get()
        yt = YouTube(url)

        print(yt.title)

        minutes, seconds = divmod(yt.length, 60)

        print(f"Video Length: {minutes}:{seconds}")
        status_label.config(text="Downloading...")

        video = yt.streams.get_highest_resolution()
        download = video.download()

        print("Download Completed! 🎉")
    except:
        print("Please enter valid url!!!")


# GUI Design

root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry("400x300")

label = tk.Label(root, text="Paste your YouTube video URL :-")
label.pack(pady=10)

url_input = tk.Entry(root, width=40)
url_input.pack(pady=5)

down_btn = tk.Button(root, text=("Download"), command=download_video)
down_btn.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

status_title = tk.label(
    root,
)
root.mainloop()
