Gesture-Controlled Music Player

This project is a computer vision-based application that enables users to control music playback using hand gestures captured through a webcam. It uses real-time hand tracking to interpret gestures and map them to actions such as play, pause, next, and previous. The system combines computer vision and audio processing to provide a touchless and interactive experience.

Project Overview

The application captures live video using a webcam and processes each frame to detect hand landmarks. Based on finger positions, it identifies specific gestures and translates them into music control commands. Audio playback is handled locally, allowing the system to function without an internet connection.

Key Features

Real-time hand gesture recognition using a webcam
Touchless music control system
Support for multiple songs in MP3 format
Dynamic gesture detection with visual feedback
Display of current gesture, playback state, and song name
Lightweight system that runs locally without internet dependency

How the System Works

Step 1
The webcam captures live video frames using OpenCV.

Step 2
Frames are processed and converted into RGB format.

Step 3
MediaPipe detects hand landmarks from each frame.

Step 4
The system analyzes finger positions to determine gestures.

Step 5
Recognized gestures are mapped to music control commands.

Step 6
Pygame handles audio playback based on detected gestures.

Gesture Mapping

Thumb raised (Thumbs Up)
Action: Play or Pause toggle

Only Index finger raised
Action: Next song

Index and Middle fingers raised
Action: Previous song

Project Structure

gesture-music-player/ (GestureController.py, hand_landmarker.task, songs/song1.mp3)

Dependencies

Install all required dependencies using pip:

pip install opencv-python mediapipe pygame numpy

Library Purpose

OpenCV handles webcam input and image processing
MediaPipe detects and tracks hand landmarks
Pygame plays and controls audio files
NumPy supports numerical operations

Installation and Setup

Step 1
Download or clone the repository:

git clone <your-repo-link>
cd gesture-music-player

Step 2
Install dependencies:

pip install -r requirements.txt

Step 3
Add your music files by placing MP3 files inside the songs folder

Step 4
Ensure that the file hand_landmarker.task is present in the root directory

Running the Application

Execute the following command:

python GestureController.py

Once started:

A webcam window will open
The system begins detecting gestures in real time
Music playback starts automatically

User Interface

The application window displays:

Detected gesture in the top-left corner
Playback status such as Playing or Paused
Current song name

Technical Details

Hand Detection

Uses MediaPipe Hand Landmarker model
Detects 21 key landmarks per hand
Tracks one hand for simplicity

Gesture Recognition Logic

Based on relative positions of finger landmarks
Compares tip and joint coordinates to determine if a finger is raised
Applies thresholds to reduce noise and false detection

Audio Control

Managed using Pygame mixer module
Supports play, pause, resume, and track switching

Limitations

Only supports MP3 format
Requires a functional webcam
Gesture detection may vary under poor lighting conditions
No graphical user interface beyond the OpenCV window
Currently supports only one hand

Future Improvements

Add volume control gestures
Improve gesture stability using smoothing techniques
Support additional file formats such as WAV and FLAC
Build a graphical user interface
Add playlist and shuffle functionality
Improve gesture classification using machine learning

Troubleshooting

No songs detected

Ensure the songs folder exists
Check that files have MP3 extension

Webcam not working

Verify camera permissions
Check if another application is using the webcam

Gestures not recognized properly

Improve lighting conditions
Keep the hand clearly visible in the frame
Avoid background clutter

Audio not playing

Verify Pygame installation
Check if the audio device is available
