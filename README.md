# Zoom Hand Gesture

This project allows users to zoom in and out of an image using real-time hand gestures. The implementation uses Python, OpenCV, and MediaPipe for hand tracking and zoom functionality.

## Features
- **Hand Gesture Tracking**: Real-time hand tracking using MediaPipe or equivalent.
- **Zoom In/Out Functionality**: Zooms based on the distance between thumb and index finger.
- **Smooth Zoom Scaling**: Ensures zooming without pixelation or distortion.
- **Visual Feedback**: Shows distance between thumb and index finger and zoom scale.

## Folder Structure

```

zoom-hand-gesture/
├── assets/
│   └── image.jpg          # Image used for zooming
├── hand\_tracker.py        # Hand tracking module using MediaPipe
├── main.py                # Main script to run the program
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
├── utils.py               # Utility functions like distance calculation and zooming
└── zoom\_logic.py          # Logic to handle zoom in and out

```

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.x (preferably 3.8 or above)
- OpenCV
- MediaPipe
- Numpy

You can install the necessary packages using `pip`:

```

pip install -r requirements.txt

```

Alternatively, install dependencies manually:

```

pip install opencv-python mediapipe numpy

```

## How to Use

1. Clone the repository or download the project files.
2. Install the required dependencies listed above.
3. Place your desired image in the `assets/` folder and name it `image.jpg`.
4. Run the main program:

```

python main.py

```

5. Open your webcam, and the program will track your hand gestures to zoom in and out of the image.

## Explanation of Files

- **`main.py`**: The main script where the webcam feed is processed and zoom functionality is applied.
- **`hand_tracker.py`**: Contains the `HandTracker` class, which uses MediaPipe to track hand landmarks in real-time.
- **`zoom_logic.py`**: Contains the `ZoomController` class, which calculates zoom scale based on the distance between thumb and index finger.
- **`utils.py`**: Contains utility functions such as calculating the distance between fingers and zooming the image.
- **`assets/`**: A folder where the image to be zoomed (image.jpg) is stored.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Instructions to create the `README.md`:

1. Create a file named `README.md` in the root directory of your project.
2. Copy and paste the above content into the file.

### Additional Information

* If you have a `requirements.txt` file, you can include the following dependencies:

```
opencv-python
mediapipe
numpy
```
