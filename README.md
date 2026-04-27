Gesture-Controlled Music Player

Overview
    The Gesture-Controlled Music Player is a computer vision-based application that allows users to control music playback using hand gestures captured through a webcam. The system uses real-time hand tracking to interpret gestures and map them to media controls such as play, pause, next, and previous.
    
    This project combines computer vision and audio processing to create a touchless and interactive user experience.

Key Features
1. Real-time hand gesture recognition using a webcam
2. Touchless music control system
3. Supports multiple songs in MP3 format
4. Dynamic gesture detection with visual feedback
5. Displays current gesture, playback state, and song name
6. Lightweight and runs locally without internet dependency

How It Works
1. The webcam captures live video frames using OpenCV.
2. Frames are processed and converted into RGB format.
3. MediaPipe detects hand landmarks from each frame.
4. The system analyzes finger positions to determine gestures.
5. Recognized gestures are mapped to music control commands.
6. Pygame handles audio playback based on detected gestures.

Gesture Mapping
Gesture Description	      |  Action Performed
------------------------------------------------
Thumb raised (Thumbs Up)  |  Play / Pause toggle
Only Index finger raised  |  Next song
Index and Middle fingers  |  Previous song

Project Structure
gesture-music-player/GestureController.py
gesture-music-player/hand_landmarker.task
gesture-music-player/songs/
gesture-music-player/songs/song1.mp3.....

Dependencies
> Install all required dependencies using pip:
    "pip install opencv-python mediapipe pygame numpy"

Library Purpose
1. OpenCV: Handles webcam input and image processing
2. MediaPipe: Detects and tracks hand landmarks
3. Pygame: Plays and controls audio files
4. NumPy: Supports numerical operations

Installation Guide
1. Download or clone the repository:
    "git clone <your-repo-link>
     cd gesture-music-player"
2. Install dependencies:
    "pip install -r requirements.txt"
3. Add your music files:
    Place .mp3 files inside the songs folder.
4. Ensure the model file:
    "hand_landmarker.task" is present in the root directory.

Running the Application
> Execute the following command:
    "python GestureController.py"
> Once started:

1. A webcam window will open.
2. The system begins detecting gestures in real time.
3. Music playback starts automatically.

User Interface
> The application window displays:

1. Detected gesture (top-left corner)
2. Playback status (Playing / Paused)
3. Current song name

Technical Details
> Hand Detection

1. Uses MediaPipe Hand Landmarker model
2. Detects 21 key landmarks per hand
3. Tracks only one hand for simplicity

> Gesture Recognition Logic

1. Based on relative positions of finger landmarks
2. Compares tip and joint coordinates to determine if a finger is raised
3. Applies thresholds to reduce noise and false detection

> Audio Control

1. Managed using Pygame mixer module
2. Supports:
    1. Play
    2. Pause
    3. Resume
    4. Track switching

Limitations
1. Only supports MP3 format
2. Requires a functional webcam
3. Gesture detection may vary under poor lighting conditions
4. No graphical UI beyond OpenCV window
5. Currently supports only one hand

Possible Improvements
1. Add volume control gestures
2. Improve gesture stability using smoothing techniques
3. Support additional file formats (WAV, FLAC)
4. Build a graphical user interface (GUI)
5. Add playlist and shuffle functionality
6. Improve gesture classification using machine learning

Troubleshooting
> No songs detected

1. Ensure the songs folder exists
2. Check that files have .mp3 extension

> Webcam not working

1. Verify camera permissions
2. Check if another application is using the webcam

> Gestures not recognized properly

1. Improve lighting conditions
2. Keep hand clearly visible in frame
3. Avoid background clutter

> Audio not playing

1. Verify Pygame installation
2. Check if audio device is available

Acknowledgment

Thank you for using the Gesture-Controlled Music Player.

Your interest and time in exploring this project are greatly appreciated. This project was developed with the aim of demonstrating how computer vision and human-computer interaction can be combined to create intuitive, touchless control systems.

If you found this project useful or insightful, your feedback, suggestions, or contributions are always welcome. They play an important role in improving and expanding the project further.

Thank you for your support.
