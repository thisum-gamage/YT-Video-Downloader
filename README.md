![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-Open%20Source-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
# 🎬 YouTube Video Downloader

A modern, fast, and user-friendly desktop application built with Python for downloading YouTube videos effortlessly. Featuring a clean graphical interface, real-time download tracking, and high-quality video downloads without requiring additional tools such as FFmpeg.

---

## ✨ Features

* 🎨 **Modern GUI** — Built with Python's `tkinter` and `ttk` for a simple and intuitive user experience.
* ⚡ **Fast Downloads** — Powered by `yt-dlp` for reliable and efficient video downloading.
* 🎥 **High-Quality Video Support** — Downloads videos using single-stream formats with integrated audio and video.
* 📊 **Real-Time Progress Tracking** — Live progress bar with download percentage updates.
* ℹ️ **Video Information Preview** — Displays video title, duration, and file size before downloading.
* 📁 **Custom Download Location** — Choose any folder to save your videos.
* 🛡️ **Error Handling** — Gracefully handles invalid URLs, network errors, and download failures.
* 💻 **Standalone Executable** — Run the application without installing Python.

---

## 🚀 Getting Started

### Option 1 — Download the Executable (Recommended)

No Python installation is required.

Download the latest release from the GitHub Releases page and run the executable directly:

```text
Releases → main.exe
```

---

### Option 2 — Run from Source

#### 1. Clone the Repository

```bash
git clone https://github.com/thisum-gamage/YT-Video-Downloader.git
cd YT-Video-Downloader
```

#### 2. Install Dependencies

```bash
pip install yt-dlp
```

#### 3. Run the Application

```bash
python main.py
```

---

## 🛠️ Building the Executable

To create your own standalone executable using PyInstaller:

```bash
pip install pyinstaller

pyinstaller --onefile --windowed \
--icon=macos_big_sur_download_folder_icon_186042.ico \
main.py
```

The generated executable will be available inside the:

```text
dist/
```

folder.

---

## 📂 Project Structure

```text
YT-Video-Downloader/
│
├── main.py
├── .gitignore
├── README.md
└── macos_big_sur_download_folder_icon_186042.ico
```

---

## 🧰 Built With

* Python
* Tkinter
* ttk
* yt-dlp
* PyInstaller

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, create a new branch, and submit a pull request.

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub. It helps support future improvements and new projects.

---

## 📜 License

This project is open-source and available for educational and personal use.
