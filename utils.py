import math
import cv2

def calculate_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def zoom_image(image, scale):
    height, width = image.shape[:2]
    center_x, center_y = width // 2, height // 2

    new_width = int(width * scale)
    new_height = int(height * scale)

    resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    x1 = max(0, center_x - width // 2)
    y1 = max(0, center_y - height // 2)
    x2 = x1 + width
    y2 = y1 + height

    cropped = resized[y1:y2, x1:x2]
    return cropped
