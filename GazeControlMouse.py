# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

############ Version 1.0
############## Left click only

# import cv2
# import mediapipe as mp
# import pyautogui

# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)
# screen_w, screen_h = pyautogui.size()

# while True: 
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
#     # print(landmark_points)
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             # print(len(landmarks[474:478]))
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             # print(x,y)
#             cv2.circle(frame, (x,  y), 3, (0, 255, 0))
#             if id == 1:
#                 screen_x = 1.2 * screen_w/frame_w * x
#                 screen_y = 1.2 * screen_h /frame_h * y

#                 # pyautogui.moveTo(x, y)
#                 pyautogui.moveTo(screen_x, screen_y)
                
#         left = [landmarks[145],landmarks[159]]
#         for landmark in left :
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             # print(x,y)
#             cv2.circle(frame, (x,  y), 3, (0, 255, 255))
#         # print(left[0].y, left[1],y)
#         print(left[0].y - left[1].y)
#         if (left[0].y - left[1].y) < 0.009:
#             # print('click')
#             pyautogui.click()
#             pyautogui.sleep(1)
                
#     cv2.imshow('eye mouse', frame)
#     cv2.waitKey(1)




################# Version 1.1
################ Left and Right click only

# import cv2
# import mediapipe as mp
# import pyautogui

# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()

# while True: 
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
    
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 0))
#             if id == 1:
#                 screen_x = 1.2 * screen_w / frame_w * x
#                 screen_y = 1.2 * screen_h / frame_h * y
#                 pyautogui.moveTo(screen_x, screen_y)
        
#         # Left eye landmarks
#         left = [landmarks[145], landmarks[159]]
#         for landmark in left:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
#         # Right eye landmarks
#         right = [landmarks[374], landmarks[386]]
#         for landmark in right:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (255, 0, 255))
        
#         # Check for left eye blink
#         if (left[0].y - left[1].y) < 0.009:
#             pyautogui.click()
#             pyautogui.sleep(1)
        
#         # Check for right eye blink
#         if (right[0].y - right[1].y) < 0.009:
#             pyautogui.rightClick()
#             pyautogui.sleep(1)
                
#     cv2.imshow('eye mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()


################# Version 1.2
################ Left and Right click and Gaze Pattern
# import cv2
# import mediapipe as mp
# import pyautogui
# import numpy as np

# # Initialize camera and face mesh
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()

# def get_gaze_ratio(eye_points, landmarks):
#     # Get the average position of the landmarks
#     left_point = np.array([landmarks[eye_points[0]].x, landmarks[eye_points[0]].y])
#     right_point = np.array([landmarks[eye_points[1]].x, landmarks[eye_points[1]].y])
#     center_top = np.array([landmarks[eye_points[2]].x, landmarks[eye_points[2]].y])
#     center_bottom = np.array([landmarks[eye_points[3]].x, landmarks[eye_points[3]].y])
    
#     # Horizontal gaze ratio
#     hor_line = np.linalg.norm(right_point - left_point)
#     ver_line = np.linalg.norm(center_top - center_bottom)
    
#     gaze_ratio = hor_line / ver_line
#     return gaze_ratio

# while True: 
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
    
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
        
#         # Define landmarks for left and right eyes
#         left_eye_indices = [33, 133, 159, 145]
#         right_eye_indices = [362, 263, 386, 374]
        
#         # Calculate gaze ratios
#         left_gaze_ratio = get_gaze_ratio(left_eye_indices, landmarks)
#         right_gaze_ratio = get_gaze_ratio(right_eye_indices, landmarks)
        
#         # Use average of both eyes' gaze ratios
#         gaze_ratio = (left_gaze_ratio + right_gaze_ratio) / 2
        
#         # Map gaze ratio to screen coordinates
#         screen_x = int(screen_w * (1 - gaze_ratio))  # Flip the ratio for natural movement
#         screen_y = int(screen_h * gaze_ratio)
        
#         pyautogui.moveTo(screen_x, screen_y)
        
#         # Visualize gaze direction on the frame
#         for eye in [left_eye_indices, right_eye_indices]:
#             for idx in eye:
#                 x = int(landmarks[idx].x * frame_w)
#                 y = int(landmarks[idx].y * frame_h)
#                 cv2.circle(frame, (x, y), 3, (0, 255, 0))
                
#         cv2.line(frame, (screen_x - 10, screen_y), (screen_x + 10, screen_y), (0, 255, 0), 2)
#         cv2.line(frame, (screen_x, screen_y - 10), (screen_x, screen_y + 10), (0, 255, 0), 2)
        
#         # Left eye landmarks for blink detection
#         left_blink = [landmarks[145], landmarks[159]]
#         for landmark in left_blink:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
#         # Right eye landmarks for blink detection
#         right_blink = [landmarks[374], landmarks[386]]
#         for landmark in right_blink:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (255, 0, 255))
        
#         # Check for left eye blink
#         if (left_blink[0].y - left_blink[1].y) < 0.009:
#             pyautogui.click()
#             pyautogui.sleep(1)
        
#         # Check for right eye blink
#         if (right_blink[0].y - right_blink[1].y) < 0.009:
#             pyautogui.rightClick()
#             pyautogui.sleep(1)
                
#     cv2.imshow('eye mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()





# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# # Initialize camera and face mesh
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()

# # Define margin to prevent cursor from reaching the edges of the screen
# margin = 50

# # Variables to help with timing to avoid accidental clicks
# left_click_time = 0
# right_click_time = 0
# click_delay = 1  # seconds

# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
    
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
        
#         # Get coordinates for the center of the left and right eyes
#         left_center_x = int((landmarks[362].x + landmarks[263].x) / 2 * frame_w)
#         left_center_y = int((landmarks[362].y + landmarks[263].y) / 2 * frame_h)
        
#         right_center_x = int((landmarks[33].x + landmarks[133].x) / 2 * frame_w)
#         right_center_y = int((landmarks[33].y + landmarks[133].y) / 2 * frame_h)
        
#         # Calculate average center position
#         avg_center_x = (left_center_x + right_center_x) / 2
#         avg_center_y = (left_center_y + right_center_y) / 2
        
#         # Map the average center position to screen coordinates
#         screen_x = int((avg_center_x / frame_w) * screen_w)
#         screen_y = int((avg_center_y / frame_h) * screen_h)
        
#         # Constrain the cursor within screen bounds and margins
#         screen_x = max(margin, min(screen_w - margin, screen_x))
#         screen_y = max(margin, min(screen_h - margin, screen_y))
        
#         pyautogui.moveTo(screen_x, screen_y)
        
#         # Visualize gaze direction on the frame
#         cv2.circle(frame, (left_center_x, left_center_y), 5, (0, 255, 0), -1)
#         cv2.circle(frame, (right_center_x, right_center_y), 5, (0, 255, 0), -1)
        
#         # Left eye landmarks for blink detection
#         left_blink = [landmarks[145], landmarks[159]]
#         for landmark in left_blink:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
#         # Right eye landmarks for blink detection
#         right_blink = [landmarks[374], landmarks[386]]
#         for landmark in right_blink:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (255, 0, 255))
        
#         # Check for left eye blink
#         if (left_blink[0].y - left_blink[1].y) < 0.009 and time.time() - left_click_time > click_delay:
#             pyautogui.click()
#             left_click_time = time.time()
        
#         # Check for right eye blink
#         if (right_blink[0].y - right_blink[1].y) < 0.009 and time.time() - right_click_time > click_delay:
#             pyautogui.rightClick()
#             right_click_time = time.time()
                
#     cv2.imshow('eye mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cam.release()
# cv2.destroyAllWindows()



import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize camera and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Define margin to prevent cursor from reaching the edges of the screen
margin = 10

# Variables to help with timing to avoid accidental clicks
left_click_time = 0
right_click_time = 0
click_delay = 1  # seconds

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        
        # Get coordinates for the center of the left and right iris
        left_iris_x = int(landmarks[474].x * frame_w)
        left_iris_y = int(landmarks[474].y * frame_h)
        
        right_iris_x = int(landmarks[469].x * frame_w)
        right_iris_y = int(landmarks[469].y * frame_h)
        
        # Get coordinates for the center of the left and right eyes
        left_eye_center_x = int(landmarks[473].x * frame_w)
        left_eye_center_y = int(landmarks[473].y * frame_h)
        
        right_eye_center_x = int(landmarks[468].x * frame_w)
        right_eye_center_y = int(landmarks[468].y * frame_h)
        
        # Calculate average iris position
        avg_iris_x = (left_iris_x + right_iris_x) / 2
        avg_iris_y = (left_iris_y + right_iris_y) / 2
        
        # Map the average iris position to screen coordinates
        screen_x = int((avg_iris_x / frame_w) * screen_w)
        screen_y = int((avg_iris_y / frame_h) * screen_h)
        
        # Constrain the cursor within screen bounds and margins
        screen_x = max(margin, min(screen_w - margin, screen_x))
        screen_y = max(margin, min(screen_h - margin, screen_y))
        
        pyautogui.moveTo(screen_x, screen_y)
        
        # Visualize iris centers and pupil tracking on the frame
        cv2.circle(frame, (left_iris_x, left_iris_y), 5, (0, 255, 0), -1)
        cv2.circle(frame, (right_iris_x, right_iris_y), 5, (0, 255, 0), -1)
        
        # Draw arrows for left and right eyes
        cv2.arrowedLine(frame, (left_eye_center_x, left_eye_center_y), (left_iris_x, left_iris_y), (255, 0, 0), 2)
        cv2.arrowedLine(frame, (right_eye_center_x, right_eye_center_y), (right_iris_x, right_iris_y), (255, 0, 0), 2)
        
        # Left eye landmarks for blink detection
        left_blink = [landmarks[145], landmarks[159]]
        for landmark in left_blink:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
        # Right eye landmarks for blink detection
        right_blink = [landmarks[374], landmarks[386]]
        for landmark in right_blink:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (255, 0, 255))
        
        # Check for left eye blink
        if (left_blink[0].y - left_blink[1].y) < 0.009 and time.time() - left_click_time > click_delay:
            pyautogui.click()
            left_click_time = time.time()
        
        # Check for right eye blink
        if (right_blink[0].y - right_blink[1].y) < 0.009 and time.time() - right_click_time > click_delay:
            pyautogui.rightClick()
            right_click_time = time.time()
                
    cv2.imshow('eye mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()



# distance = 200
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)   # move right
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)   # move down
#     pyautogui.drag(-distance, 0, duration=0.5)  # move left
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)  # move up





    
    
    
    
    
    