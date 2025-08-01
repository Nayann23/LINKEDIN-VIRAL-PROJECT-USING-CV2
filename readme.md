# 🖱️ Virtual Mouse & Air Paint using OpenCV + MediaPipe

This project contains two exciting gesture-based applications built using Python, OpenCV, MediaPipe, and PyAutoGUI:

1. 🎯 **Virtual Mouse**: Control your system mouse using just hand gestures!
2. 🎨 **CV2 Paint**: Draw in the air using your finger like a digital paintbrush.

---

## 📁 Files Included

| File                          | Description                                  |
|-------------------------------|----------------------------------------------|
| `Virtual_Mouse_Using_CV2.py` | Gesture-controlled mouse with click support  |
| `cv2_paint.py`               | Air-drawing app using hand tracking          |
| `requirements.txt`           | Required libraries to run the projects       |

---

## 🛠️ Features

### ✅ Virtual Mouse (`Virtual_Mouse_Using_CV2.py`)
- Move the cursor using your **index finger**
- **Single click**: Pinch gesture (index + thumb)
- **Double click**: Pinch with **middle finger** extended
- Smooth mouse movement with adjustable sensitivity
- Works in full-screen mode using webcam tracking

### ✅ CV2 Paint (`cv2_paint.py`)
- Draw with your finger in the air
- Choose from 4–5 preset **colors**
- Use the **eraser gesture** to remove parts of the drawing
- Smart detection to avoid continuous drawing from the last point
- Supports color selection and brush gestures

---

## ✋ Hand Gestures

| Gesture                        | Action                   |
|-------------------------------|--------------------------|
| ☝️ Index finger only          | Move cursor              |
| 🤏 Index + Thumb              | Single click             |
| 🤏 + ✌️ Middle finger         | Double click             |
| ✋ All fingers extended        | Eraser (in Paint mode)   |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Nayann23/LINKEDIN-VIRAL-PROJECT-USING-CV2.git
cd linkedIn-viral-project-using-cv2
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ **Note**: If `mediapipe` fails to install due to Python version compatibility, use Python **3.9** for best results.

### 3. Run the Applications
```bash
# For Virtual Mouse
python Virtual_Mouse_Using_CV2.py

# For Paint App
python cv2_paint.py
```

---

## 📦 `requirements.txt`
```txt
opencv-python
mediapipe
pyautogui
numpy
```

---

## 🧠 Future Improvements

- Add right-click or scroll gestures  
- Voice assistant feedback (like "Click done, sir")  
- Hand drag & drop support  
- Record drawings or export as images  

---

## 👨‍💻 Author

**Nayan**
