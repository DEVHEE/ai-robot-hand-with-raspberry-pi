"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

'''
USAGE
python main_maskRecongition_image.py --image asstes/image/mask_1.png
'''

# Import modules.
import os
import argparse
import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# Parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="the path of input image")
ap.add_argument("-f", "--face", type=str,
    default="face_recognizer",
    help="the path of face recognizer model directory")
ap.add_argument("-m", "--model", type=str,
    default="mask_recognizer.model",
    help="the path of trained face mask recognizer model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
    help="minimum probability to filter weak recognitions")
args = vars(ap.parse_args())

# Load our serialized face recognizer model from disk.
print("Loading face recognizer model...")
prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
    "res10_300x300_ssd_iter_140000.caffemodel"])
net = cv2.dnn.readNet(prototxtPath, weightsPath)

# Load the face mask recognizer model from disk.
print("Loading face mask recognizer model...")
model = load_model(args["model"])

# Load the input image from disk, clone it, and grab the image spatial dimensions.
image = cv2.imread(args["image"])
orig = image.copy()
(h, w) = image.shape[:2]

# Construct a blob from the image.
blob = cv2.dnn.blobFromImage(
    image,
    1.0,
    (300, 300),
    (104.0, 177.0, 123.0))

# Pass the blob through the network and obtain the face recognitions.
print("Computing face recognitions...")
net.setInput(blob)
recognitions = net.forward()

# Loop over the recognitions.
for i in range(0, recognitions.shape[2]):
    # Extract the confidence (i.e., probability) associated with the recognition.
    confidence = recognitions[0, 0, i, 2]

    # Filter out weak recognitions by ensuring the confidence is greater than the minimum confidence.
    if confidence > args["confidence"]:
        # Compute the (x, y)-coordinates of the bounding box for the object.
        box = recognitions[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # Ensure the bounding boxes fall within the dimensions of the frame.
        (startX, startY) = (max(0, startX), max(0, startY))
        (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

        # Extract the face ROI, convert it from BGR to RGB channel ordering, resize it to 224x224, and preprocess it.
        face = image[startY:endY, startX:endX]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)
        face = np.expand_dims(face, axis=0)

        # Pass the face through the model to determine if the face has a mask or not.
        (mask, withoutMask) = model.predict(face)[0]

        # Determine the class label and color we'll use to draw the bounding box and text.
        label = "MASK" if mask > withoutMask else "NO MASK"
        color = (0, 255, 0) if label == "MASK" else (0, 0, 255)

        # Include the probability in the label.
        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        # Display the label and bounding box rectangle on the output frame.
        cv2.putText(image, label, (startX, startY - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)

# Show the output image.
cv2.imshow("MASK RECOGNITION RESULT", image)
cv2.waitKey(0)