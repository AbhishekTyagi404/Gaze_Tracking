# 👁️ Eye Gaze Controlled Media Player (Hands-Free Interaction)

A real-time Python-based system that uses facial landmarks and blink detection to control media playback without touching your keyboard. This project allows you to skip songs or pause/play videos using just your **eye blinks and gaze** — powered by webcam, OpenCV, and Dlib.

---

## 👨‍💻 Author

**Abhishek Tyagi**  
Roll No: 42370211217  
Delhi Institute of Tool Engineering  
Project for CS50x AI (Harvard)  
🎓 [Certificate](https://cs50.harvard.edu/certificates/cdea1963-1535-4aef-be8e-d285f8a4f2e4)

---

## 🎥 Demo Preview

<details>
<summary>▶️ Click to Watch the WebM Demo</summary>

<br>

<video src="https://github.com/AbhishekTyagi404/Gaze_Tracking/blob/main/Final_Demo.webm?raw=true" controls width="100%" style="border-radius: 12px;">
  Your browser does not support the video tag.
</video>

</details>

🖼️ [Click here to view GIF Demo](https://kritrimintelligence.com/wp-content/uploads/2025/03/EyeGazing_GIF.gif)

---

## 📦 Features

- 👁️ Real-time gaze tracking (center, left, right)
- 👀 Blink detection using Eye Aspect Ratio (EAR)
- 🖱️ 2 sequential blinks → Next track (⏭️)
- ⏸️ 3 sequential blinks → Pause / Play toggle
- 🧠 26 FPS pipeline using OpenCV threading and grayscale optimization
- 🖥️ Works on standard webcam

---

## 🚀 How to Run

### 1. Clone this repository

```bash
git clone https://github.com/AbhishekTyagi404/Gaze_Media_Player.git
cd Gaze_Media_Player
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-python dlib numpy pyautogui pygame imutils
```

> ⚠️ Note: `dlib` requires `cmake`, `boost`, and `XQuartz` (macOS). Refer to this [guide](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) for full setup help.

### 3. Download the facial landmark model

Download the pre-trained **shape predictor model**:

🔗 [shape_predictor_68_face_landmarks.dat](https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat)

Place it in your project root or inside `gaze_tracking/trained_models/`.

---

## 🧪 Run the App

```bash
python blink_control_vlc_youtube.py
# OR
python blink_control_mp3_player.py
```

It will open your webcam and start live gaze tracking with on-screen annotations.

---

## 🧠 Controls

| Action           | Method                                |
|------------------|----------------------------------------|
| ⏭️ Next Track     | 2 rapid blinks (within 2 seconds)      |
| ⏯️ Pause / Play   | 3 rapid blinks (within 2 seconds)      |
| 👁️ Gaze Detection | Direction shown on-screen              |

> Works seamlessly with most media players (YouTube, VLC, Spotify if window focused)

---

## 🔧 File Structure

```bash
📁 Gaze_Media_Player/
│
├── blink_control_mp3_player.py     # Embedded MP3 player
├── blink_control_vlc_youtube.py    # VLC / YouTube control via keyboard
├── gaze_tracking/                  # Gaze tracking module
│   ├── calibration.py
│   ├── eye.py
│   ├── gaze_tracking.py
│   ├── pupil.py
│   └── __init__.py
├── requirements.txt
├── README.md
└── Final_Demo.webm
```

---

## 📈 Tech Stack

- Python 3.x
- OpenCV
- Dlib (Kazemi & Sullivan’s 68-point landmark model)
- NumPy
- Pygame (for embedded MP3 playback)
- PyAutoGUI (for external app key simulation)
- EAR-based blink detection (Soukupová and Čech)

---

## 📚 References

- [OpenCV](https://opencv.org/)
- [Dlib](http://dlib.net/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pygame](https://www.pygame.org/docs/ref/mixer.html)
- Soukupová, T. and Čech, J. (2016). *Real-Time Eye Blink Detection Using Facial Landmarks*.
- CS50 AI: https://cs50.harvard.edu/ai/

---

## 🧠 Future Work

- Add gesture-based volume control
- Screen-based UI selector using gaze zones
- Integrate voice commands
- Model-based gaze regression (ML-driven)

---

## © 2025 Abhishek Tyagi
