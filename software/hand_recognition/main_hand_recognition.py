"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
import time
import cv2
import mediapipe as mp
import numpy as np

# Import custom modules.
import modules.pca9685 as pca9685
import modules.utils as utils

# Setting modules.
drawModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

cap = cv2.VideoCapture(0)  # To use webcam.
# cap = cv2.VideoCapture("./assets/video/vid_hand-1.mp4")  # To use video.

# Initialize lambda coordinates of saved fingers.
saved_fin0_L01 = None
saved_fin0_L12 = None
saved_fin0_L23 = None
saved_fin0_W = None

saved_fin1_L01 = None
saved_fin1_L12 = None
saved_fin1_L23 = None
saved_fin1_W = None

saved_fin2_L01 = None
saved_fin2_L12 = None
saved_fin2_L23 = None
saved_fin2_W = None

saved_fin3_L01 = None
saved_fin3_L12 = None
saved_fin3_L23 = None
saved_fin3_W = None

saved_fin4_L01 = None
saved_fin4_L12 = None
saved_fin4_L23 = None
saved_fin4_W = None

# Initialize motor run status.
run = 0

# Recognition start.
prevTime = 0
with handsModule.Hands(max_num_hands=1,
                       min_detection_confidence=0.58,
                       min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, image = cap.read()

        if not ret:
            print("The frame does not exist.")
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
                        circle_radius=3),
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
                        circle_radius=3),
                    drawModule.DrawingSpec(
                        color=(243, 51, 255),
                        thickness=2,
                        circle_radius=2))

                idx = 0
                topPoint_list = []
                secondPoint_list = []
                thirdPoint_list = []
                bottomPoint_list = []
                wristPoint_list = []
                for point in handsModule.HandLandmark:
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordinatesLandmark = drawModule._normalized_to_pixel_coordinates(
                        normalizedLandmark.x,
                        normalizedLandmark.y,
                        imageWidth,
                        imageHeight
                        )

                    # Save top points coordinate.
                    if idx == 4 or idx == 8 or idx == 12 or idx == 16 or idx == 20:
                        if pixelCoordinatesLandmark is None:
                            topPoint_list.append((0, 0))
                        else:
                            topPoint_list.append(pixelCoordinatesLandmark)

                    # Save second points coordinate.
                    if idx == 3 or idx == 7 or idx == 11 or idx == 15 or idx == 19:
                        if pixelCoordinatesLandmark is None:
                            secondPoint_list.append((0, 0))
                        else:
                            secondPoint_list.append(pixelCoordinatesLandmark)

                    # Save third points coordinate.
                    if idx == 2 or idx == 6 or idx == 10 or idx == 14 or idx == 18:
                        if pixelCoordinatesLandmark is None:
                            thirdPoint_list.append((0, 0))
                        else:
                            thirdPoint_list.append(pixelCoordinatesLandmark)

                    # Save top points coordinate.
                    if idx == 1 or idx == 5 or idx == 9 or idx == 13 or idx == 17:
                        if pixelCoordinatesLandmark is None:
                            bottomPoint_list.append((0, 0))
                        else:
                            bottomPoint_list.append(pixelCoordinatesLandmark)

                    # Save wrist coordinate.
                    if idx == 0:
                        if pixelCoordinatesLandmark is None:
                            wristPoint_list.append((0, 0))
                        else:
                            wristPoint_list.append(pixelCoordinatesLandmark)

                    # Draw landmark index.
                    image = cv2.putText(image, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (192, 61, 0), 1)
                    black = cv2.putText(black, f'IDX: {int(idx)}', pixelCoordinatesLandmark, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1)

                    idx += 1

                # Save points of each finger.
                level_list = []
                for i in range(5):
                    lvl0 = [topPoint_list[i]]
                    lvl1 = [secondPoint_list[i]]
                    lvl2 = [thirdPoint_list[i]]
                    lvl3 = [bottomPoint_list[i]]

                    level_list.append([lvl0, lvl1, lvl2, lvl3])

                # level_list
                # [
                # [[#0 finger top], [#0 finger second], [#0 finger third], [#0 finger bottom]],
                # [[#1 finger top], [#1 finger second], [#1 finger third], [#1 finger bottom]],
                # [[#2 finger top], [#2 finger second], [#2 finger third], [#2 finger bottom]],
                # [[#3 finger top], [#3 finger second], [#3 finger third], [#3 finger bottom]],
                # [[#4 finger top], [#4 finger second], [#4 finger third], [#4 finger bottom]]
                # ]

                # Assign level of each finger point.
                fin0_lvl0 = level_list[0][0]
                fin0_lvl1 = level_list[0][1]
                fin0_lvl2 = level_list[0][2]
                fin0_lvl3 = level_list[0][3]

                fin1_lvl0 = level_list[1][0]
                fin1_lvl1 = level_list[1][1]
                fin1_lvl2 = level_list[1][2]
                fin1_lvl3 = level_list[1][3]

                fin2_lvl0 = level_list[2][0]
                fin2_lvl1 = level_list[2][1]
                fin2_lvl2 = level_list[2][2]
                fin2_lvl3 = level_list[2][3]

                fin3_lvl0 = level_list[3][0]
                fin3_lvl1 = level_list[3][1]
                fin3_lvl2 = level_list[3][2]
                fin3_lvl3 = level_list[3][3]

                fin4_lvl0 = level_list[4][0]
                fin4_lvl1 = level_list[4][1]
                fin4_lvl2 = level_list[4][2]
                fin4_lvl3 = level_list[4][3]

                wrist_lvl = wristPoint_list[0]

                # Calculate the joints distance of fingers.
                result_fin0_L01 = utils.calcJoint(fin0_lvl0, fin0_lvl1)
                result_fin0_L12 = utils.calcJoint(fin0_lvl1, fin0_lvl2)
                result_fin0_L23 = utils.calcJoint(fin0_lvl2, fin0_lvl3)
                result_fin0_W = utils.calcJoint(fin0_lvl3, [wrist_lvl])

                result_fin1_L01 = utils.calcJoint(fin1_lvl0, fin1_lvl1)
                result_fin1_L12 = utils.calcJoint(fin1_lvl1, fin1_lvl2)
                result_fin1_L23 = utils.calcJoint(fin1_lvl2, fin1_lvl3)
                result_fin1_W = utils.calcJoint(fin1_lvl3, [wrist_lvl])

                result_fin2_L01 = utils.calcJoint(fin2_lvl0, fin2_lvl1)
                result_fin2_L12 = utils.calcJoint(fin2_lvl1, fin2_lvl2)
                result_fin2_L23 = utils.calcJoint(fin2_lvl2, fin2_lvl3)
                result_fin2_W = utils.calcJoint(fin2_lvl3, [wrist_lvl])

                result_fin3_L01 = utils.calcJoint(fin3_lvl0, fin3_lvl1)
                result_fin3_L12 = utils.calcJoint(fin3_lvl1, fin3_lvl2)
                result_fin3_L23 = utils.calcJoint(fin3_lvl2, fin3_lvl3)
                result_fin3_W = utils.calcJoint(fin3_lvl3, [wrist_lvl])

                result_fin4_L01 = utils.calcJoint(fin4_lvl0, fin4_lvl1)
                result_fin4_L12 = utils.calcJoint(fin4_lvl1, fin4_lvl2)
                result_fin4_L23 = utils.calcJoint(fin4_lvl2, fin4_lvl3)
                result_fin4_W = utils.calcJoint(fin4_lvl3, [wrist_lvl])

                # Make lists of intervals between joints.
                result_fin0_list = [result_fin0_L01, result_fin0_L12, result_fin0_L23, result_fin0_W]
                saved_fin0_list = [saved_fin0_L01, saved_fin0_L12, saved_fin0_L23, saved_fin0_W]

                result_fin1_list = [result_fin1_L01, result_fin1_L12, result_fin1_L23, result_fin1_W]
                saved_fin1_list = [saved_fin1_L01, saved_fin1_L12, saved_fin1_L23, saved_fin1_W]

                result_fin2_list = [result_fin2_L01, result_fin2_L12, result_fin2_L23, result_fin2_W]
                saved_fin2_list = [saved_fin2_L01, saved_fin2_L12, saved_fin2_L23, saved_fin2_W]

                result_fin3_list = [result_fin3_L01, result_fin3_L12, result_fin3_L23, result_fin3_W]
                saved_fin3_list = [saved_fin3_L01, saved_fin3_L12, saved_fin3_L23, saved_fin3_W]

                result_fin4_list = [result_fin4_L01, result_fin4_L12, result_fin4_L23, result_fin4_W]
                saved_fin4_list = [saved_fin4_L01, saved_fin4_L12, saved_fin4_L23, saved_fin4_W]

                # Process of control fingers.
                if run == 1:  # If run status.
                    # Control servo motor by case when coordinates saved.
                    if saved_fin0_list[3] and saved_fin1_list[3] and saved_fin2_list[3] and saved_fin3_list[3] and saved_fin4_list[3] is not None:  # If fingers coordinates are saved.
                        pca9685.ctrlFin1(result_fin1_list, saved_fin1_list)  # Control the finger 1 servo motors.
                    else:
                        print("Please save the fingers coordinates.")

                # Save each landmark keypoints.
                keypoints = []
                for data_point in hand_landmarks.landmark:
                    keypoints.append({
                         'X': data_point.x,
                         'Y': data_point.y,
                         'Z': data_point.z,
                         'Visibility': data_point.visibility,
                         })

                for i in range (4):
                    cv2.circle(image, level_list[0][i][0], 5, (73, 73, 255), 2)
                    cv2.circle(image, level_list[1][i][0], 5, (56, 182, 255), 2)
                    cv2.circle(image, level_list[2][i][0], 5, (38, 255, 255), 2)
                    cv2.circle(image, level_list[3][i][0], 5, (60, 214, 0), 2)
                    cv2.circle(image, level_list[4][i][0], 5, (244, 255, 96), 2)
                    cv2.circle(image, wrist_lvl, 5, (255, 255, 255), 2)
                    cv2.circle(black, level_list[0][i][0], 5, (73, 73, 255), 2)
                    cv2.circle(black, level_list[1][i][0], 5, (56, 182, 255), 2)
                    cv2.circle(black, level_list[2][i][0], 5, (38, 255, 255), 2)
                    cv2.circle(black, level_list[3][i][0], 5, (60, 214, 0), 2)
                    cv2.circle(black, level_list[4][i][0], 5, (244, 255, 96), 2)
                    cv2.circle(black, wrist_lvl, 5, (255, 255, 255), 2)

        currTime = time.time()
        fps = 1 / (currTime - prevTime)
        prevTime = currTime

        # Draw fps frame.
        cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)
        cv2.putText(black, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

        # Draw hand safe rectangle.
        cv2.rectangle(image, (imageWidth//2 - 150, imageHeight//2 - 150), (imageWidth//2 + 150, imageHeight//2 + 150), (255, 255, 255), 2)
        cv2.rectangle(black, (imageWidth//2 - 150, imageHeight//2 - 150), (imageWidth//2 + 150, imageHeight//2 + 150), (255, 255, 255), 2)

        cv2.imshow('HAND DETECTION WITH LANDMARK - EXTRACT', black)
        cv2.imshow('HAND DETECTION WITH LANDMARK - ORIGINAL', image)

        key = cv2.waitKey(5) & 0xFF

        if key == ord("a"):  # Key press A.
            run = 0

        elif key == ord("d"):  # Key press D.
            run = 1

        elif key == ord("s"):  # Key press S.
            run = 0

            saved_fin0_L01 = result_fin0_L01
            saved_fin0_L12 = result_fin0_L12
            saved_fin0_L23 = result_fin0_L23
            saved_fin0_W = result_fin0_W

            saved_fin1_L01 = result_fin1_L01
            saved_fin1_L12 = result_fin1_L12
            saved_fin1_L23 = result_fin1_L23
            saved_fin1_W = result_fin1_W

            saved_fin2_L01 = result_fin2_L01
            saved_fin2_L12 = result_fin2_L12
            saved_fin2_L23 = result_fin2_L23
            saved_fin2_W = result_fin2_W

            saved_fin3_L01 = result_fin3_L01
            saved_fin3_L12 = result_fin3_L12
            saved_fin3_L23 = result_fin3_L23
            saved_fin3_W = result_fin3_W

            saved_fin4_L01 = result_fin4_L01
            saved_fin4_L12 = result_fin4_L12
            saved_fin4_L23 = result_fin4_L23
            saved_fin4_W = result_fin4_W

            print("\n-----------------------------------------------------------")
            print("Fingers coordinates saved.")
            print(f"[Finger 0] IDX 8-7: ({saved_fin0_L01}) / IDX 7-6: ({saved_fin0_L12}) / IDX 6-5: ({saved_fin0_L23})")
            print(f"[Finger 1] IDX 8-7: ({saved_fin1_L01}) / IDX 7-6: ({saved_fin1_L12}) / IDX 6-5: ({saved_fin1_L23})")
            print(f"[Finger 2] IDX 8-7: ({saved_fin2_L01}) / IDX 7-6: ({saved_fin2_L12}) / IDX 6-5: ({saved_fin2_L23})")
            print(f"[Finger 3] IDX 8-7: ({saved_fin3_L01}) / IDX 7-6: ({saved_fin3_L12}) / IDX 6-5: ({saved_fin3_L23})")
            print(f"[Finger 4] IDX 8-7: ({saved_fin4_L01}) / IDX 7-6: ({saved_fin4_L12}) / IDX 6-5: ({saved_fin4_L23})")
            print("-----------------------------------------------------------")

        elif key == ord('q') or key == 27:  # Key press Q or ESC.
            cv2.destroyAllWindows()
            break

cap.release()
