import cv2
import numpy as np
import mediapipe as mp

# Initialize mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Colors
colors = [
    (0, 0, 255),    # Red
    (0, 255, 0),    # Green
    (255, 0, 0),    # Blue
    (0, 255, 255),  # Yellow
    (255, 0, 255)   # Purple
]
eraser_color = (0, 0, 0)
draw_color = colors[0]
color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Eraser"]

# Canvas setup
xp, yp = 0, 0
canvas = None
brush_thickness = 10
eraser_thickness = 50

# Webcam
cap = cv2.VideoCapture(0)

def fingers_up(lm_list):
    fingers = []
    if lm_list[4][1] > lm_list[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    for id in [8, 12, 16, 20]:
        fingers.append(1 if lm_list[id][2] < lm_list[id - 2][2] else 0)
    return fingers

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if canvas is None:
        canvas = np.zeros_like(img)

    results = hands.process(img_rgb)
    lm_list = []
    hand_present = False

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        for id, lm in enumerate(hand_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((id, cx, cy))

        hand_present = True

        if lm_list:
            x1, y1 = lm_list[8][1], lm_list[8][2]
            fingers = fingers_up(lm_list)

            # Select mode - two fingers up
            if fingers[1] and fingers[2]:
                xp, yp = 0, 0
                if y1 < 60:
                    if 0 < x1 < 100:
                        draw_color = colors[0]
                    elif 100 < x1 < 200:
                        draw_color = colors[1]
                    elif 200 < x1 < 300:
                        draw_color = colors[2]
                    elif 300 < x1 < 400:
                        draw_color = colors[3]
                    elif 400 < x1 < 500:
                        draw_color = colors[4]
                    elif 500 < x1 < 600:
                        draw_color = eraser_color
                cv2.rectangle(img, (x1 - 20, y1 - 20), (x1 + 20, y1 + 20), draw_color, cv2.FILLED)

            # Drawing mode - index finger only
            elif fingers[1] and not fingers[2]:
                cv2.circle(img, (x1, y1), 10, draw_color, cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                if draw_color == eraser_color:
                    cv2.line(img, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                    cv2.line(canvas, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                else:
                    cv2.line(img, (xp, yp), (x1, y1), draw_color, brush_thickness)
                    cv2.line(canvas, (xp, yp), (x1, y1), draw_color, brush_thickness)
                xp, yp = x1, y1
            else:
                xp, yp = 0, 0  # reset if not in draw mode
    else:
        xp, yp = 0, 0  # hand not detected — reset so next draw is fresh

    # Merge canvas and webcam feed
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv_canvas = cv2.threshold(gray_canvas, 50, 255, cv2.THRESH_BINARY_INV)
    inv_canvas = cv2.cvtColor(inv_canvas, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, inv_canvas)
    img = cv2.bitwise_or(img, canvas)

    # Draw color bar
    for i, color in enumerate(colors):
        cv2.rectangle(img, (i * 100, 0), ((i + 1) * 100, 60), color, -1)
        cv2.putText(img, color_names[i], (i * 100 + 10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.rectangle(img, (500, 0), (600, 60), (50, 50, 50), -1)
    cv2.putText(img, "Eraser", (510, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Show image
    cv2.imshow("Virtual Paint", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
