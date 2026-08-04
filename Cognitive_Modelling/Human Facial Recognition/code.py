# Human Face Recognition System
# Requirements:
# pip install opencv-contrib-python numpy

import cv2
import os
import numpy as np

# -------------------------------
# Load Face Detector
# -------------------------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -------------------------------
# Dataset Path
# Dataset/
#    Person1/
#       img1.jpg
#       img2.jpg
#    Person2/
#       img1.jpg
#       img2.jpg
# -------------------------------
dataset_path = "Dataset"

faces = []
labels = []
label_names = {}
label_id = 0

# -------------------------------
# Read Training Images
# -------------------------------
for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    label_names[label_id] = person

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        img = cv2.imread(image_path)

        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detected = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in detected:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            faces.append(face)
            labels.append(label_id)

    label_id += 1

print("Training Images Loaded")

# -------------------------------
# Train LBPH Recognizer
# -------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

print("Training Completed")

# -------------------------------
# Start Webcam
# -------------------------------
camera = cv2.VideoCapture(0)

threshold = 70

print("Press Q to Quit")

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detected:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label, confidence = recognizer.predict(face)

        if confidence < threshold:
            name = label_names[label]
        else:
            name = "Unknown Person"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            f"{name} ({confidence:.2f})",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,0,0),
            2
        )

    cv2.imshow("Human Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()