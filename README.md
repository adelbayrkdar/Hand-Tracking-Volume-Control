# Hand-Tracking-Volume-Control
Hand gesture-based volume control using Python and OpenCV. Tracks thumb-index finger distance to adjust audio levels, with a lock feature for stable volume. Innovative, touch-free, and user-friendly.

The `HandTrackingMin.py` file contains the minimal code necessary to run the hand tracking model. It utilizes the MediaPipe library to detect and track the hand landmarks in real-time using the webcam. The script captures video frames, processes them to detect hands, and then draws landmarks and connections between them, displaying the result in a live video feed.

In `HandTrackingModule.py`, the hand tracking functionality is encapsulated into a Python class named `HandDetector`. This module abstracts the hand tracking setup and processing, allowing for easy integration and reuse in other projects. It provides functions to find hands in an image and to retrieve the positions of hand landmarks.

The `VolumeHandControl.py` file is the main application script that combines hand tracking with volume control. Using the `HandTrackingModule`, it detects hand gestures to adjust the system's volume level. The volume is controlled through the distance between the thumb and index finger, with a locking feature to maintain the desired volume level until a specific gesture is performed to unlock it.

In addition to the code files, the project includes a comprehensive documentation PDF titled "Hand-Tracking Volume Control." This document serves as a detailed guide to the entire process, from the conceptualization to the execution of the hand tracking volume control system. It offers insights into the design decisions, explains the code structure, and discusses the integration of different modules. By reviewing this documentation, one can gain a deeper understanding of the project's workings, the technology stack used, and the practical applications of hand gesture recognition in controlling system functionalities. It is an essential resource for anyone looking to explore the nuances of this project or to replicate and build upon the work done.

Each of these components plays a crucial role in the hand tracking volume control project, showcasing the integration of computer vision and system control through Python programming.
