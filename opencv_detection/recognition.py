from glos import *
import os
import cv2
import numpy as np


def training_set_data():
	dirs = os.listdir(PEOPLE)
	faces = []
	labels = []
	print(dirs)
	for d in dirs:
		if not d.startswith('s'):
			continue
		label = int(d.replace('s', ''))




def recognize():
	recognizer = cv2.createLBPHFaceRegonizer()


training_set_data()