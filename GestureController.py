import cv2
import mediapipe as mp
import numpy as np
import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load songs
music_folder = "songs"
songs = sorted([os.path.join(music_folder, song) for song in os.listdir(music_folder) if song.endswith(".mp3")])
if not songs:
    raise Exception("No MP3 files found in the 'songs' folder.")

current_song_index = 0

def play_song(index):
    try:
        pygame.mixer.music.load(songs[index])
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(songs[index])}")
    except:
        print("Skipping bad file:", songs[index])
        index = (index + 1) % len(songs)
        play_song(index)

# Initial song play
play_song(current_song_index)

# MediaPipe setup
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

# Webcam
cap = cv2.VideoCapture(0)

# Gesture tracking
last_gesture = None
gesture_cooldown = 3
last_gesture_time = time.time()

print("Gestures: 👍 Play/Pause | ☝️ Next | ✌️ Previous")

gesture_count = 0
stable_gesture = None
STABLE_FRAMES=5

is_playing = True
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # MediaPipe input
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=img_rgb
    )

    results = detector.detect(mp_image)

    gesture = None

    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            lm = hand_landmarks

            # Thumb (different logic)
            thumb_up = lm[4].x - lm[3].x + 0.04
            index_up = lm[8].y < lm[6].y - 0.03
            middle_up = lm[12].y < lm[10].y - 0.03
            ring_up = lm[16].y < lm[14].y - 0.03
            pinky_up = lm[20].y < lm[18].y - 0.03

            # Gesture detection
            # 👍 THUMBS UP (very strict)
            if thumb_up and not index_up and not middle_up and not ring_up and not pinky_up:
                # 👇 extra condition to avoid confusion
                if abs(lm[4].y - lm[8].y) > 0.1:  
                    gesture = "thumbs_up"

            # ☝️ INDEX ONLY
            elif index_up and not middle_up:
                gesture = "next"

            # ✌️ INDEX + MIDDLE
            elif index_up and middle_up:
                gesture = "previous"

            else:
                gesture = None

        current_time = time.time()

    if gesture == stable_gesture:
        gesture_count += 1
    else:
        stable_gesture = gesture
        gesture_count = 1

    if (gesture_count >= STABLE_FRAMES and 
        gesture is not None and 
        current_time - last_gesture_time > gesture_cooldown):

        if gesture == "thumbs_up":
            if is_playing:
                pygame.mixer.music.pause()
                print("Paused")
                is_playing = False
            else:
                pygame.mixer.music.unpause()
                print("Playing")
                is_playing = True

        elif gesture == "next":
            current_song_index = (current_song_index + 1) % len(songs)
            play_song(current_song_index)

        elif gesture == "previous":
            current_song_index = (current_song_index - 1) % len(songs)
            play_song(current_song_index)

        last_gesture_time = current_time
    if gesture is None:
        last_gesture = None
    # Show window
    # Show current gesture
    cv2.putText(img, f"Gesture: {gesture}", (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    # Show play/pause
    cv2.putText(img, "Playing" if is_playing else "Paused",
                (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)

    # Show song name
    cv2.putText(img, f"Song: {os.path.basename(songs[current_song_index])}",
                (10,130), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

    # Show window
    cv2.imshow("Gesture Music Player", img)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop() 
