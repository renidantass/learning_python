from glos import *
import cv2
import os
import numpy as np



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
    
def detect_license_plate(img):
    from PIL import Image
    import pytesseract
    # Only russians
    plate_classifier = cv2.CascadeClassifier(os.path.join(CASCADES, 'haarcascade_licence_plate_rus_16stages.xml'))
    img = cv2.imread(os.path.join(TEST_FOLDER, img))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    licenses = plate_classifier.detectMultiScale(gray, 1.05, 5)
    if licenses is not None:
        for (x,y,w,h) in licenses:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    plate = img[y: y+h, x:x+w]
    cv2.imwrite("plate.jpg", plate)
    number_plate = pytesseract.image_to_string(Image.open("plate.jpg"))
    cv2.putText(img, str(number_plate), (x, (y+h)+55), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 8)
    cv2.imshow('license plate', img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()