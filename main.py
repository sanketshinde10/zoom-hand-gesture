import cv2
from hand_tracker import HandTracker
from utils import calculate_distance, zoom_image
from zoom_logic import ZoomController

# Load and resize image
original_img = cv2.imread("assets/image.jpg")

if original_img is None:
    print("❌ Error: Could not load image. Check the path: assets/image.jpg")
    exit()

# Resize the image to a smaller size (e.g., 640x480)
original_img = cv2.resize(original_img, (640, 480))

# Initialize modules
tracker = HandTracker()
zoom = ZoomController()
scale = 1.0

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Failed to read from webcam.")
        break

    frame = cv2.flip(frame, 1)
    frame, landmarks = tracker.find_hand(frame)

    if landmarks:
        # Thumb tip = id 4, Index tip = id 8
        thumb = landmarks[4][1:]
        index = landmarks[8][1:]
        distance = calculate_distance(thumb, index)
        scale = zoom.get_zoom_scale(distance)

        # Draw visual feedback
        cv2.line(frame, thumb, index, (0, 255, 0), 2)
        cv2.putText(frame, f'Scale: {scale:.2f}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    zoomed_img = zoom_image(original_img, scale)
    cv2.imshow("Zoomed Image", zoomed_img)
    cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
