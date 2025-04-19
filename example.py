
"""
Eye Gaze Controlled Media Player with Audio Playback
Author: Abhishek Tyagi
Version: 2.3
"""

import cv2
import time
import os
import pygame
from gaze_tracking import GazeTracking

# Initialize gaze tracker and webcam
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# Initialize pygame mixer
pygame.mixer.init()

# Load songs from media directory
media_folder = "media"
songs = [file for file in os.listdir(media_folder) if file.endswith(".mp3")]
songs.sort()
current_song = 0

def play_song(index):
    song_path = os.path.join(media_folder, songs[index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    print(f"▶️ Playing: {songs[index]}")

if songs:
    play_song(current_song)
else:
    print("⚠️ No .mp3 files found in 'media/' folder.")
    exit()

blink_count = 0
last_blink_time = 0
blink_window = 2  # seconds

paused = False

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
            current_song = (current_song + 1) % len(songs)
            play_song(current_song)
            blink_count = 0

        elif blink_count == 3:
            if paused:
                pygame.mixer.music.unpause()
                print("▶️ Resumed")
            else:
                pygame.mixer.music.pause()
                print("⏸️ Paused")
            paused = not paused
            blink_count = 0

        text = f"Blinking ({blink_count})"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, f"Left pupil:  {left_pupil}", (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, f"Right pupil: {right_pupil}", (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Gaze Media Player", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
