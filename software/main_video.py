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
                topPoint_list = []
                secondPoint_list = []
                thirdPoint_list = []
                bottomPoint_list = []
                for point in handsModule.HandLandmark:
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordinatesLandmark = drawModule._normalized_to_pixel_coordinates(
                        normalizedLandmark.x,
                        normalizedLandmark.y,
                        imageWidth,
                        imageHeight
                        )
                    
                    # Save top points coordinate.
                    if (idx == 4 or idx == 8 or idx == 12 or idx == 16 or idx == 20):
                        if (pixelCoordinatesLandmark == None):
                            topPoint_list.append((0, 0))
                        else:
                            topPoint_list.append(pixelCoordinatesLandmark)
                    
                    # Save second points coordinate.
                    if (idx == 3 or idx == 7 or idx == 11 or idx == 15 or idx == 19):
                        if (pixelCoordinatesLandmark == None):
                            secondPoint_list.append((0, 0))
                        else:
                            secondPoint_list.append(pixelCoordinatesLandmark)
                            
                    # Save third points coordinate.
                    if (idx == 2 or idx == 6 or idx == 10 or idx == 14 or idx == 18):
                        if (pixelCoordinatesLandmark == None):
                            thirdPoint_list.append((0, 0))
                        else:
                            thirdPoint_list.append(pixelCoordinatesLandmark)
                    
                    # Save top points coordinate.
                    if (idx == 1 or idx == 5 or idx == 9 or idx == 13 or idx == 17):
                        if (pixelCoordinatesLandmark == None):
                            bottomPoint_list.append((0, 0))
                        else:
                            bottomPoint_list.append(pixelCoordinatesLandmark)
                    
                    # Draw landmark index.
                    image = cv2.putText(image, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (192, 61, 0), 1)
                    black = cv2.putText(black, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1)
                    
                    idx += 1
                
                # Draw lines between the top points of landmarks.
                for p in range(0, len(topPoint_list)-1):
                    cv2.line(image, topPoint_list[p], topPoint_list[p+1], (0, 255, 255), 2)
                    cv2.line(black, topPoint_list[p], topPoint_list[p+1], (0, 255, 255), 2)
                
                # Save points of each finger.
                points_list = []
                for i in range (1, 5):
                    pos_1 = [topPoint_list[i]]
                    pos_2 = [secondPoint_list[i]]
                    pos_3 = [thirdPoint_list[i]]
                    pos_4 = [bottomPoint_list[i]]
                    
                    points_list.append([pos_1, pos_2, pos_3, pos_4])
                
                # points_list
                # [
                # [[#1 finger top], [#1 finger second], [#1 finger third], [#1 finger bottom]],
                # [[#2 finger top], [#2 finger second], [#2 finger third], [#2 finger bottom]],
                # [[#3 finger top], [#3 finger second], [#3 finger third], [#3 finger bottom]],
                # [[#4 finger top], [#4 finger second], [#4 finger third], [#4 finger bottom]]
                # ]
                
                # Assign points of each finger.
                pos_1_top = points_list[0][0]
                pos_1_second = points_list[0][1]
                pos_1_third = points_list[0][2]
                
                pos_2_top = points_list[1][0]
                pos_2_second = points_list[1][1]
                pos_2_third = points_list[1][2]
                
                pos_3_top = points_list[2][0]
                pos_3_second = points_list[2][1]
                pos_3_third = points_list[2][2]
                
                pos_4_top = points_list[3][0]
                pos_4_second = points_list[3][1]
                pos_4_third = points_list[3][2]

                # Calculate each finger bended.
                pos_1_TS= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_1_top, pos_1_second)
                result_pos_1_TS = [tuple(i) for i in pos_1_TS][0][1]
                pos_1_ST= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_1_second, pos_1_third)
                result_pos_1_ST = [tuple(i) for i in pos_1_ST][0][1]
                
                pos_2_TS= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_2_top, pos_2_second)
                result_pos_2_TS = [tuple(i) for i in pos_2_TS][0][1]
                pos_2_ST= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_2_second, pos_2_third)
                result_pos_2_ST = [tuple(i) for i in pos_2_ST][0][1]
                
                pos_3_TS= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_3_top, pos_3_second)
                result_pos_3_TS = [tuple(i) for i in pos_3_TS][0][1]
                pos_3_ST= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_3_second, pos_3_third)
                result_pos_3_ST = [tuple(i) for i in pos_3_ST][0][1]
                
                pos_4_TS= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_4_top, pos_4_second)
                result_pos_4_TS = [tuple(i) for i in pos_4_TS][0][1]
                pos_4_ST= map(lambda x, y: map(lambda i, j: i-j, x, y), pos_4_second, pos_4_third)
                result_pos_4_ST = [tuple(i) for i in pos_4_ST][0][1]
                
                # Print bended finger
                if (result_pos_1_TS > 0 and result_pos_1_ST > 0):
                    changed_pos_1 = "o"
                else:
                    changed_pos_1 = "I"
                    
                if (result_pos_2_TS > 0 and result_pos_2_ST > 0):
                    changed_pos_2 = "o"
                else:
                    changed_pos_2 = "I"
                    
                if (result_pos_3_TS > 0 and result_pos_3_ST > 0):
                    changed_pos_3 = "o"
                else:
                    changed_pos_3 = "I"
                    
                if (result_pos_4_TS > 0 and result_pos_4_ST > 0):
                    changed_pos_4 = "o"
                else:
                    changed_pos_4 = "I"
                    
                print(changed_pos_1 + changed_pos_2 + changed_pos_3 + changed_pos_4)

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