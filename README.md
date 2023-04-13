# Object Detection Python Application
A python application to detect and provide the names of the objects overviewed by a webcam

## Table of Contents

- [About](#about)
- [Installing](#installing)
- [Usage](#usage)
- [Contributing](#contributing)

## About
This small python code uses the MobileNetV2 model from TensorFlow's Keras application,
opens the user's computer web camera using OpenCV, and continuously captures frames from the camera.
For each frame, it resizes it to the required input size of the MobileNetV2 model, 
converts it to an array, preprocesses it, and feeds it to the model to predict the object in the frame.
It then displays the predicted object name on the frame and shows the frame in a window titled "Image Detection."
The program will be running until the user presses the 'q' key,
where it will close the camera and close all the windows.

## Installing
while creating i used the following:
- Python version 3.10
- TensorFlow (Installed as python package by "pip install tensorflow" or "pip3 install tensorflow")
- OpenCv (installed as python package by "pip install opencv-python" or "pip3 install opencv-python")

## Usage
- You can run code directly from your editor or
- Within the same directory containing python file run the command "python image_detector.py".
- Press 'q' key to quit the Webcam window and stop the application.
- For better perfomance connect computer to network (Internet).

## Contributing
Thanks to my friends.
Also online stuffs eg. StackOverflow and ChatGpt

## Remarks
I have decided to use this approach inorder to reduce time and hussle required to build and train models for them to perform. thats why the idea of using TensorFlow came.
