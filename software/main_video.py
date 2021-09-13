"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# import modules
import cv2
import mediapipe as mp
import numpy as np
import time

# setting modules
drawModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

cap = cv2.VideoCapture(0)  # To use webcam.
# cap = cv2.VideoCapture("./assets/video/vid-hand1.mp4")  # To use video.

prevTime = 0
with handsModule.Hands(
    max_num_hands=1,
    min_detection_confidence=0.58,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, image = cap.read()
        
        if not ret:
            print("[INFO] The frame does not exist.")
            continue  # for webcam.
            # break  # for video.

        image = cv2.flip(image, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # To improve performance, make any cached arrays read-only.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Get height and width info from image.
        imageHeight, imageWidth, _ = image.shape
        
        black = np.zeros((imageHeight, imageWidth, 3), np.uint8)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                # Draw landmarks for original frame.
                drawModule.draw_landmarks(
                    image,
                    hand_landmarks,
                    handsModule.HAND_CONNECTIONS,
                    drawModule.DrawingSpec(
                        color=(0, 255, 0),
                        thickness=-1,
                        circle_radius=6),
                    drawModule.DrawingSpec(
                        color=(243, 51, 255),
                        thickness=2,
                        circle_radius=2))
                
                # Draw landmarks for extract frame.
                drawModule.draw_landmarks(
                    black,
                    hand_landmarks,
                    handsModule.HAND_CONNECTIONS,
                    drawModule.DrawingSpec(
                        color=(0, 255, 0),
                        thickness=-1,
                        circle_radius=6),
                    drawModule.DrawingSpec(
                        color=(243, 51, 255),
                        thickness=2,
                        circle_radius=2))
                
                idx = 0
                for point in handsModule.HandLandmark:
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordinatesLandmark = drawModule._normalized_to_pixel_coordinates(
                        normalizedLandmark.x,
                        normalizedLandmark.y,
                        imageWidth,
                        imageHeight
                        )
                    
                    # Draw landmark index.
                    image = cv2.putText(image, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (192, 61, 0), 1)
                    black = cv2.putText(black, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1)
                    
                    idx += 1

                # Save each landmark keypoints.
                keypoints = []
                for data_point in hand_landmarks.landmark:
                    keypoints.append({
                         'X': data_point.x,
                         'Y': data_point.y,
                         'Z': data_point.z,
                         'Visibility': data_point.visibility,
                         })
        
        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime
        
        # Draw fps frame.
        cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
        cv2.putText(black, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
        
        cv2.imshow('HAND DETECTION WITH LANDMARK - EXTRACT', black)
        cv2.imshow('HAND DETECTION WITH LANDMARK - ORIGINAL', image)
        
        if cv2.waitKey(5) & 0xFF == 27:  # ESC
            break
        
cap.release()