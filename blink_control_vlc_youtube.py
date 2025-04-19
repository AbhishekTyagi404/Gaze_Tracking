""" 
Blink-Controlled Media Player Interface (External Apps: VLC, YouTube)
Author: Abhishek Tyagi
Version: 2.3
"""

import cv2
import time
import pyautogui
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

blink_count = 0
last_blink_time = 0
blink_window = 2  # seconds to detect sequential blinks

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()

    text = ""

    if gaze.is_blinking():
        now = time.time()
        if now - last_blink_time < blink_window:
            blink_count += 1
        else:
            blink_count = 1
        last_blink_time = now

        if blink_count == 2:
            pyautogui.press('right')
            print("[KEYBOARD] Right arrow pressed (Next Track)")
            blink_count = 0
        elif blink_count == 3:
            pyautogui.press('space')
            print("[KEYBOARD] Spacebar pressed (Pause/Play)")
            blink_count = 0

        text = f"Blinking ({blink_count})"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.imshow("External Media Control", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()