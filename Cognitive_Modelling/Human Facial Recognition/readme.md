# Human Face Recognition System using OpenCV (LBPH)

## Overview

This project implements a **Human Face Recognition System** using **OpenCV**, **NumPy**, and the **Local Binary Patterns Histograms (LBPH)** face recognizer. The system is trained on images stored in a dataset, detects faces using a Haar Cascade classifier, and identifies known individuals through a live webcam feed.

---

## Features

* Detects human faces using Haar Cascade Classifier.
* Trains an LBPH Face Recognizer on multiple individuals.
* Recognizes known faces in real time.
* Labels unknown faces as **"Unknown Person"**.
* Displays confidence score for each prediction.
* Simple folder-based dataset structure.
* Real-time webcam recognition.

---

## Technologies Used

* Python 3.x
* OpenCV (opencv-contrib-python)
* NumPy

---

## Requirements

Install the required libraries:

```bash
pip install opencv-contrib-python numpy
```

---

## Dataset Structure

Create a folder named **Dataset** in the project directory.

```
Dataset/
│
├── Person1/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│
├── Person2/
│   ├── img1.jpg
│   ├── img2.jpg
│
└── Person3/
    ├── img1.jpg
    ├── img2.jpg
```

Each folder name represents the person's identity.

---

## How It Works

### 1. Face Detection

* Loads the Haar Cascade face detector.
* Detects faces from every training image.

### 2. Data Preparation

* Converts images to grayscale.
* Crops detected face regions.
* Resizes each face to **200 × 200 pixels**.
* Assigns a unique label to every person.

### 3. Model Training

* Trains an **LBPH Face Recognizer** using:

  * Face images
  * Corresponding labels

### 4. Real-Time Recognition

* Opens the webcam.
* Detects faces in each frame.
* Predicts the identity of each detected face.
* Displays:

  * Person's name
  * Confidence score

If the confidence value exceeds the threshold, the face is labelled as:

```
Unknown Person
```

---

## Algorithm

1. Load Haar Cascade classifier.
2. Read all images from the dataset.
3. Detect and crop faces.
4. Convert to grayscale.
5. Resize images to 200×200.
6. Assign labels.
7. Train the LBPH recognizer.
8. Start webcam.
9. Detect faces in live video.
10. Predict identity.
11. Display name and confidence.
12. Exit when **Q** is pressed.

---

## Project Structure

```
Human-Face-Recognition/
│
├── Dataset/
│   ├── Person1/
│   ├── Person2/
│   └── ...
│
├── face_recognition.py
└── README.md
```

---

## Sample Output

```
Training Images Loaded
Training Completed
Press Q to Quit
```

Webcam Window:

```
+-----------------------------+
|                             |
|      [ Face Detected ]      |
|                             |
|  Tanisha (42.53)            |
|                             |
+-----------------------------+
```

Unknown person:

```
Unknown Person (89.24)
```

---

## Advantages

* Easy to implement.
* Fast real-time recognition.
* Works with multiple individuals.
* Lightweight and suitable for basic face recognition tasks.
* Requires minimal training data.

---

## Limitations

* Accuracy depends on image quality and lighting.
* Sensitive to pose variations and facial occlusions.
* Haar Cascade may produce false detections in challenging conditions.
* Not suitable for large-scale or highly secure recognition systems.

---

## Future Enhancements

* Add automatic dataset image capture.
* Improve accuracy using deep learning models (FaceNet, ArcFace, Dlib).
* Store trained model for reuse without retraining.
* Support multiple camera inputs.
* Integrate attendance management or access control systems.
* Enhance performance under varying lighting conditions.

---

## Conclusion

This project demonstrates a simple and efficient **real-time human face recognition system** using OpenCV's Haar Cascade for face detection and the **LBPH algorithm** for recognition. It serves as a strong beginner-friendly computer vision project and provides a foundation for more advanced facial recognition applications.
