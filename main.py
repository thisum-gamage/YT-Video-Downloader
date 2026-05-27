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

try:
    url = input("Paste your video url : ")
    yt = YouTube(url)

    print(yt.title)

    minutes, seconds = divmod(yt.length, 60)

    print(f"Video Length: {minutes}:{seconds}")
    print("Downloading...")

    video = yt.streams.get_highest_resolution()
    download = video.download()

    print("Download Completed! 🎉")
except:
    print("Please enter valid url!!!")
