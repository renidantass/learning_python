import cv2
import os
import numpy as np


TEST_FOLDER = os.path.join(os.getcwd(), 'test-data')
CASCADES = os.path.join(os.getcwd(), 'opencv-files')


def detect_face(img):
    # Classifier to recognize face
    face_classifier = cv2.CascadeClassifier(os.path.join(CASCADES, 'haarcascade_frontalface_default.xml'))
    # Loading image
    img = cv2.imread(os.path.join(TEST_FOLDER, img))
    # Converting image to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecting faces on image with grayscale
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    # If faces then...
    if faces is not None:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img, '<Rosto da pessoa', (x+w+10, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, .70, (255, 255, 255))
    
    # Show image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_face('test5.jpg')