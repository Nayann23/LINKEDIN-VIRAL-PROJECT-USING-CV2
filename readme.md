# 🖱️ Virtual Mouse & Air Paint using OpenCV + MediaPipe

This project contains two exciting gesture-based applications using Python, OpenCV, MediaPipe, and PyAutoGUI:

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
- Move cursor with your **index finger**
- **Single click**: Pinch (index + thumb)
- **Double click**: Pinch + middle finger
- Smooth mouse movement with adjustable sensitivity
- Works full-screen with webcam tracking

### ✅ CV2 Paint (`cv2_paint.py`)
- Draw with your finger in air
- Select between 4–5 preset **colors**
- Use **eraser gesture**
- Smart detection to avoid continuous tracking from last point
- Color selection and brush gesture support

---

## ✋ Hand Gestures

| Gesture                       | Action                  |
|------------------------------|--------------------------|
| ☝️ Index finger only         | Move cursor              |
| 🤏 Index + Thumb             | Single click             |
| 🤏 + ✌️ Middle finger        | Double click             |
| ✋ All fingers together      | Eraser (in Paint mode)   |

---

## 📸 Screenshots (Optional)
_Add screenshots or a screen recording GIF to show how it works visually._

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/virtual-mouse-opencv.git
cd virtual-mouse-opencv
