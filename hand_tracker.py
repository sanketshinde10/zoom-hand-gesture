import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_conf=0.7, max_hands=1):
        self.hands_module = mp.solutions.hands
        self.hands = self.hands_module.Hands(static_image_mode=False,
                                             max_num_hands=max_hands,
                                             min_detection_confidence=detection_conf)
        self.draw = mp.solutions.drawing_utils

    def find_hand(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)
        landmarks = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmarks.append((id, cx, cy))
                self.draw.draw_landmarks(frame, hand_landmarks, self.hands_module.HAND_CONNECTIONS)

        return frame, landmarks
