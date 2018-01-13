#!/usr/bin/python3
"""
    This is a test only
"""
import cv2
import os
import numpy as np


subjects = ["", "Barack Obama"]

def detect_face(img):
    # convert image to grayscale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # load OpenCV face detector, I'm using LBP which is fast
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    # let's detect multiscale images(some images may be closer to camera than others)
    # result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # if no faces are detect then return to original img
    if len(faces) == 0:
        return None, None
    # under the assumption that there will be only one face, extract the face area
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]



def prepare_training_data(data_folder_path=""):
    # one dir to each subject
    dirs = os.listdir(data_folder_path)

    # list to hold all subject faces
    faces = []

    # list to hold labels for all subjects
    labels = []
    
    # STEP 2
    """
        Extract label number of subject from dir_name
        format of dir name = slabel
        so removing letter 's' from dir_name will gives us label
    """
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue
        label = int(dir_name.replace('s', ''))
        subject_dir_path = os.path.join(data_folder_path, dir_name)
        subject_images_names = os.listdir(subject_dir_path)

    # STEP 3
    """
        go through each image name, read image,
        detect face and add face to list of faces
    """
    for image_name in subject_images_names:
        if image_name.startswith('.'):
            continue
        # build image path
        image_path = os.path.join(subject_dir_path, image_name)
        image = cv2.imread(image_path)
        cv2.imshow("Training an image", image)
        cv2.waitKey(100)
        face, rect = detect_face(image)

    # STEP 4
    """
        for the purpose of this tutorial
        we will ignore faces that are not detected
    """
    if face is not None:
        faces.append(face)
        labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels


print("Colocando óleo no pulmão e desejando a morte...")
faces,labels = prepare_training_data('training_data')
print("Ops, acho que isso é errado, pera, vou começar a treinar os rostos")

print("Total de rostos detectados:", len(faces))
print("Total de rótulos:", len(labels))


# create our LBPH face recognizer
face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer.train(faces, np.array(labels))

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0,), 2)

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0,), 2)

def predict(test_img):
    img = test_img.copy()
    face, rect = detect_face(img)
    label = face_recognizer.predict(face)
    print(label)
    label_text = subjects[label]
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    return img

print("Detectando rostos...")

# load test images
test_img1 = cv2.imread("test-data/test1.jpg")

# perform a prediction
predicted_img1 = predict(test_img1)
print("Rostos detectados!")

# display both images
cv2.imshow(subjects[0], predicted_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()