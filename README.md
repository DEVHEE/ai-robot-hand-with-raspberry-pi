<h1 align="center">🤖 AI Robot Hand with Raspberry Pi</h1>

<h3 align="center"><strong>A robotics hand that mimics human hands using Computer Vision</strong></h3>

![preview-crop](https://user-images.githubusercontent.com/46535278/132984747-09d74565-d2ef-4d48-a31e-11a7b0df6df0.jpeg)

---

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-in%20progress-yellow.svg)]()
[![Python 3.8.10](https://img.shields.io/badge/python-3.8.10-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![made-with-opencv](http://img.shields.io/badge/OpenCV-5c3ee8?style=square&logo=OpenCV&logoColor=white)](https://opencv.org/)
[![Raspberry Pi](http://img.shields.io/badge/Raspberry%20Pi-c51a4a?style=square&logo=Raspberry-Pi&logoColor=white)](https://www.raspberrypi.org/)

</div>

---

<div align='center'>

### Quick Links

<a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>
<img src='https://img.shields.io/badge/DOCUMENT-orange?style=for-the-badge'>
</a>

<a href='https://blog.kimdonghee.dev/categories/robot/'>
<img src='https://img.shields.io/badge/BLOG%20POST-blue?style=for-the-badge'>
</a>

<a href='https://portfolio.kimdonghee.dev/projects/'>
<img src='https://img.shields.io/badge/PORTFOLIO-yellow?style=for-the-badge'>
</a>

<a href='https://colab.research.google.com/drive/1lIUMgEGuxMQnUnG-7kwvn2p90z00Xy_m'>
<img src='https://img.shields.io/badge/Open%20in-Google Colab-blue?logo=Google-Colab&style=for-the-badge'>
</a>
  
</div>

---

> This project is currently under development and is always being updated.

```markdown
# TODO
-
```

## 📎 Table of Contents
  * [Project Documents](#-project-documents)
  * [Folder Structure](#-folder-structure)
  * [Licensing](#-licensing)

## 📑 Project Documents

<a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>
<img src='https://img.shields.io/badge/DOCUMENT-orange?style=for-the-badge'>
</a>

-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>Introduction</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/getting-started'>Getting Started</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/document/1-map-out'>1. Map out</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/document/2-electronic-control-research'>2. Electronic Control Research</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/document/3-hardware-research'>3. Hardware Research</a>

<a href='https://blog.kimdonghee.dev/categories/robot/'>
<img src='https://img.shields.io/badge/BLOG%20POST-blue?style=for-the-badge'>
</a>

-   <a href='https://blog.kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-1-구상/'>Robot / AI Robot Hand with Raspberry Pi - 1. 구상</a>
-   <a href='https://blog.kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-2-전자제어-연구/'>Robot / AI Robot Hand with Raspberry Pi - 2. 전자제어 연구</a>
-   <a href='https://blog.kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-3-하드웨어-연구/'>Robot / AI Robot Hand with Raspberry Pi - 3. 하드웨어 연구</a>

## 🗂 Folder Structure

    .
    ├── hardware
    │   └── circuit-diagram
    │       ├── AI_Robot_Hand_with_Raspberry_Pi_Circuit_Diagram.fzz
    │       └── AI_Robot_Hand_with_Raspberry_Pi_Circuit_Diagram.png
    ├── resource
    │   ├── 3d_model
    │   │   └── robot_hand
    │   │       ├── finger
    │   │       │   ├── fin_L01_1.STL
    │   │       │   ├── fin_L01_2.STL
    │   │       │   ├── fin_L01_3.STL
    │   │       │   ├── fin_L12_1.STL
    │   │       │   ├── fin_L12_2.STL
    │   │       │   ├── fin_L12_3.STL
    │   │       │   ├── fin_L23_1.STL
    │   │       │   ├── fin_L23_2.STL
    │   │       │   ├── fin_L23_3.STL
    │   │       │   └── servo_gear.STL
    │   │       └── LICENSE.txt
    │   ├── environment
    │   │   └── Miniconda3_latest_Linux_aarch64.sh
    │   ├── library
    │   │   ├── Adafruit_Python_PCA9685
    │   │   │   └── ...
    │   │   ├── watson-streaming-stt
    │   │   │   └── ...
    │   │   └── mediapipe_0.8.4_cp38_cp38_linux_aarch64.whl
    │   └── testing
    │       ├── alpha_prototype_v0.1T
    │       │   ├── alpha_prototype_v0.1T_1.MOV
    │       │   ├── alpha_prototype_v0.1T_2.MOV
    │       │   └── alpha_prototype_v0.1T_3.MOV
    │       └── alpha_prototype_v0.2T
    │           └── alpha_prototype_v0.2T.mp4
    ├── software
    │   ├── embedded_saved
    │   │   ├── pwm_on_8051
    │   │   │   ├── example.c
    │   │   │   └── example.s
    │   │   ├── led_dimmer.c
    │   │   └── test_pwm.c
    │   ├── hand_recongition
    │   │   ├── assets
    │   │   │   ├── image
    │   │   │   │   ├── img_hand-1.jpg
    │   │   │   │   ├── img_hand-2.jpg
    │   │   │   │   └── img_hand-3.jpg
    │   │   │   └── video
    │   │   │       ├── vid_hand-1.mp4
    │   │   │       ├── vid_hand-2.mp4
    │   │   │       └── vid_hand-3.mp4
    │   │   ├── modules
    │   │   │   ├── pca9685
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── pwm_control.py
    │   │   │   │   ├── pwm_init.py
    │   │   │   │   └── pwm_settings.py
    │   │   │   ├── utils
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── calculate_joint.py
    │   │   │   └── __init__.py
    │   │   └── main_hand_recognition.py
    │   ├── mask_recognition
    │   │   ├── assets
    │   │   │   ├── image
    │   │   │   │   ├── mask-1.png
    │   │   │   │   ├── mask-2.png
    │   │   │   │   ├── no_mask-1.png
    │   │   │   │   └── no_mask-2.png
    │   │   │   └── video
    │   │   │       ├── CDC_mask_480.mp4
    │   │   │       ├── CDC_mask_720.mp4
    │   │   │       └── video_source.txt
    │   │   ├── dataset
    │   │   │   ├── with_mask
    │   │   │   │   └── ...
    │   │   │   └── without_mask
    │   │   │       └── ...
    │   │   ├── face_recognizer
    │   │   │   ├── deploy.prototxt
    │   │   │   └── res10_300x300_ssd_iter_140000.caffemodel
    │   │   ├── loss_acc_plot.png
    │   │   ├── main_mask_recongition_image.py
    │   │   ├── main_mask_recongition_video.py
    │   │   ├── main_mask_recongition.ipynb
    │   │   ├── mask_recognizer.model
    │   │   └── train_mask_recongition.py
    │   ├── pwm_test
    │   │   ├── gpio_test.py
    │   │   └── pca9685_test.py
    │   ├── speech_recognition
    │   │   ├── modules
    │   │   │   ├── pca9685
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── pwm_control.py
    │   │   │   │   ├── pwm_init.py
    │   │   │   │   └── pwm_settings.py
    │   │   │   └── __init__.py
    │   │   ├── main_speech_movement.py
    │   │   ├── main_speech_recognition.py
    │   │   ├── setup.py
    │   │   ├── speech.cfg
    │   │   └── text_output.txt
    │   └── text_recognition
    │       ├── assets
    │       │   ├── image
    │       │   │   └── test.png
    │       │   └── temp
    │       │       └── .keep
    │       ├── result
    │       │   └── tts
    │       │       ├── string.txt
    │       │       └── tts.mp3
    │       └── main_text_recognition.py
    ├── .gitattributes
    ├── .gitginore
    ├── LICENSE
    └── README.md

## ⭐️ Licensing

The MIT License 2021 KIM DONGHEE

<a href="https://github.com/DEVHEE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=KIM%20DONGHEE&color=000000"></a>  
