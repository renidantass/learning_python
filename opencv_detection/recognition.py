"""
	My own test with OpenCV :d
"""
import os
import cv2
import numpy as np


TEST_FOLDER = os.path.join(os.getcwd(), 'test-data')
CASCADES = os.path.join(os.getcwd(), 'opencv-files')
PEOPLE = os.path.join(os.getcwd(), 'training-data')



def detect_face(img):
	"""
		This function fetch ONE FACE in image and return this in gray
	"""
	face_classifier = cv2.CascadeClassifier(os.path.join(CASCADES, 'haarcascade_frontalface_default.xml'))
	image = cv2.imread(img)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(image, 1.3, 5)
	if len(faces) == 0:
		return None, None
	else:
		(x,y,w,h) = faces[0]
		return gray[y:y+h, x:x+w]

def training_set_data(path):
	dirs = os.listdir(path)
	faces = []
	labels = []

def recognize():
	recognizer = cv2.createLBPHFaceRegonizer()