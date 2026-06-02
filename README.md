# 🎬 YouTube Video Downloader

An elegant, fast, and user-friendly desktop application built with Python to download YouTube videos effortlessly. It features a modern GUI, real-time progress tracking, and does not require external tools like ffmpeg for basic high-quality downloads.

---

## ✨ Features

* **User-Friendly GUI:** Built using Python's `tkinter` and `ttk` for a clean interface.
* **Smart Downloads:** Uses `yt_dlp` with single-stream format selection (`b`) ensuring seamless audio-video integration without extra dependencies.
* **Real-time Progress Bar:** Visual feedback on download percentage and download speed status.
* **Video Details Extractor:** Displays Video Title, Duration (Length), and File Size before/during download.
* **Custom Save Directory:** Browse and select any folder to save your downloaded videos.
* **Safe Error Handling:** Catch invalid URLs or network issues gracefully without crashing.

---

## 🚀 How to Run the App

### Option 1: Download the Executable (.exe) — *Recommended for Users*
You don't need Python installed! Just head over to the **[Releases](https://github.com/thisum-gamage/YT-Video-Downloader/releases)** section, download the latest `main.exe`, and run it directly on your Windows PC.

### Option 2: Run from Source Code — *For Developers*
If you want to run or modify the code locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/thisum-gamage/YT-Video-Downloader.git](https://github.com/thisum-gamage/YT-Video-Downloader.git)
   cd YT-Video-Downloader
   
2. **Install dependencies:**
Make sure you have Python installed, then run:
   ```bash
   pip install yt-dlp

3. **Run the application:**
   
   ```bash
   python main.py

   
