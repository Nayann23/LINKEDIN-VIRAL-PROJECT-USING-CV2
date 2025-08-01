import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

screen_width, screen_height = pyautogui.size()
cap = cv2.VideoCapture(0)
sensitivity = 2.0  # Increase for faster cursor movement
prev_click_time = 0

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_height, image_width, _ = image.shape

       
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

               
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

               
                x = int(index_tip.x * image_width)
                y = int(index_tip.y * image_height)

                
                dx = (index_tip.x - 0.5) * sensitivity + 0.5
                dy = (index_tip.y - 0.5) * sensitivity + 0.5
                dx = min(max(dx, 0.0), 1.0)
                dy = min(max(dy, 0.0), 1.0)

                screen_x = int(dx * screen_width)
                screen_y = int(dy * screen_height)

                
                pyautogui.moveTo(screen_x, screen_y)

                
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

               
                thumb_x = int(thumb_tip.x * image_width)
                thumb_y = int(thumb_tip.y * image_height)
                index_x = int(index_tip.x * image_width)
                index_y = int(index_tip.y * image_height)
                middle_x = int(middle_tip.x * image_width)
                middle_y = int(middle_tip.y * image_height)

                
                dist_index_thumb = np.hypot(thumb_x - index_x, thumb_y - index_y)
                dist_middle_thumb = np.hypot(thumb_x - middle_x, thumb_y - middle_y)

                current_time = time.time()

                
                if dist_index_thumb < 30 and dist_middle_thumb > 40:
                    if current_time - prev_click_time > 1:
                        pyautogui.click()
                        prev_click_time = current_time

                
                elif dist_index_thumb < 30 and dist_middle_thumb < 30:
                    if current_time - prev_click_time > 1.5:
                        pyautogui.doubleClick()
                        prev_click_time = current_time

              
                cv2.circle(image, (x, y), 10, (0, 255, 255), -1)

      
        cv2.imshow("Virtual Mouse (with Clicks)", image)

        
        if cv2.waitKey(5) & 0xFF == 27:
            break


cap.release()
cv2.destroyAllWindows()
