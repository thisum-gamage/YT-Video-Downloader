import tkinter as tk

root = tk.Tk()
root.title("Youtube Video Downloader")
root.geometry("400x300")

label = tk.Label(root, text="Enter YouTube URL :-")
label.pack(pady=10)

url_input = tk.Entry(root, width=40)
url_input.pack(pady=5)

down_btn = tk.Button(root, text=("Download"), command=download_video)
down_btn.pack(pady=10)

root.mainloop()