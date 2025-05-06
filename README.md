### 📄 `README.md`

```markdown
# 🖼️ Zoom Any Picture Using Hand Gestures

This Python OpenCV project allows users to zoom in and out of a static image using **real-time hand gestures** via webcam. It uses **MediaPipe** for hand tracking and dynamically adjusts zoom based on the distance between the thumb and index finger.

---

## 📌 Features

- ✅ Real-time hand tracking using MediaPipe
- 🔍 Dynamic zoom based on finger distance
- 🎯 Smooth zoom scaling without pixelation
- 🖥️ Live webcam feed + zoomed image window
- 📏 Visual feedback for scale and distance

---

## 📁 Project Structure

```

zoom-hand-gesture/
│
├── main.py                  # Main driver script
├── hand\_tracker.py          # Handles hand detection using MediaPipe
├── utils.py                 # Utility functions (distance, zoom logic)
├── zoom\_logic.py            # Zoom scale controller
├── assets/
│   └── image.jpg            # Image to zoom (you can change this)
├── requirements.txt         # Installed packages list
└── README.md                # This file

````

---

## 🛠️ Setup Instructions

### 1. 📦 Create Conda Environment

```bash
conda create -n zoom-hand-gesture python=3.10
conda activate zoom-hand-gesture
````

### 2. 🧰 Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

> Make sure you are using **Python 3.10 or 3.11**. MediaPipe does not yet support Python 3.13+.

### 3. ▶️ Run the App

```bash
python main.py
```

Press `Q` to exit the app.

---

## ✋ Hand Gesture Controls

* 👌 **Zoom In/Out**: Move thumb and index finger apart or closer.
* 📐 Distance is used to scale the image dynamically.
* 🖼️ The zoomed image stays center-aligned and resizes smoothly.

---

## 📷 Requirements

* Webcam (built-in or external)
* Compatible OS (Windows/macOS/Linux)
* Python 3.10+

---

## 💡 Future Improvements

* Add GUI with zoom slider
* Save zoomed images
* Support for gesture-based panning

---

## 📸 Demo

> *(Add screenshots or demo GIFs here)*

---

## 🧑‍💻 Author

**Sanket Nitin Shinde**
Zoom Hand Gesture Vision Project — 2025

---

## 📝 License

This project is open source and free to use under the [MIT License](LICENSE).

```
