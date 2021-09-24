<h1 align="center">🤖 AI Robot Hand with Raspberry Pi</h1>

<h3 align="center"><strong>A robotics hand that mimics human hands using Computer Vision</strong></h1>

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

<a href='https://kimdonghee.dev/categories/robot/'>
<img src='https://img.shields.io/badge/BLOG%20POST-blue?style=for-the-badge'>
</a>

<a href='https://portfolio.kimdonghee.dev/projects/'>
<img src='https://img.shields.io/badge/PORTFOLIO-yellow?style=for-the-badge'>
</a>

<a href='https://colab.research.google.com/drive/1w7I8yGAaeVIxXkxoTj6KdLO33mSbWkmY'>
<img src='https://img.shields.io/badge/Open%20in-Google Colab-blue?logo=Google-Colab&style=for-the-badge'>
</a>
  
</div>

---

> This project is currently under development and is always being updated.

```markdown
# TODO
Update development environment
Update project documents
```

## 📎 Table of Contents
  * [Project Documents](#-project-documents)
  * [Folder Structure](#-folder-structure)
  * [Development Environment](#-development-environment)
  * [Licensing](#-licensing)

## 📑 Project Documents

<a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>
<img src='https://img.shields.io/badge/DOCUMENT-orange?style=for-the-badge'>
</a>

-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>Introduction</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/getting-started'>Getting Started</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>1. Map out</a>
-   <a href='https://ai-robot-hand-with-raspberry-pi.kimdonghee.dev/'>2. Electronic Control Research</a>

<a href='https://kimdonghee.dev/categories/robot/'>
<img src='https://img.shields.io/badge/BLOG%20POST-blue?style=for-the-badge'>
</a>

-   <a href='https://kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-1-구상/'>Robot / AI Robot Hand with Raspberry Pi - 1. 구상</a>
-   <a href='https://kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-2-전자제어-연구/'>Robot / AI Robot Hand with Raspberry Pi - 2. 전자제어 연구</a>
-   <a href='https://kimdonghee.dev/posts/Projects_Robot_AI-Robot-Hand-with-Raspberry-Pi-3-하드웨어-연구/'>Robot / AI Robot Hand with Raspberry Pi - 3. 하드웨어 연구</a>

## 🗂 Folder Structure

    .
    ├── hardware
    │   └── circuit diagram
    │       ├── AI Robot Hand with Raspberry Pi Circuit Diagram.fzz
    │       └── AI Robot Hand with Raspberry Pi Circuit Diagram.png
    ├── resource
    │   ├── environment
    │   │   └── Miniconda3-latest-Linux-aarch64.sh
    │   └── library
    │       └── mediapipe-0.8.4-cp38-cp38-linux_aarch64.sh
    ├── software
    │   ├── hand-recongition
    │   │   ├── assets
    │   │   │   ├── image
    │   │   │   │   ├── img-hand1.jpg
    │   │   │   │   ├── img-hand2.jpg
    │   │   │   │   └── img-hand3.jpg
    │   │   │   └── video
    │   │   │       ├── vid-hand1.mp4
    │   │   │       ├── vid-hand2.mp4
    │   │   │       └── vid-hand3.mp4
    │   │   └── main_handRecognition.py
    │   ├── mask-recognition
    │   │   ├── assets
    │   │   │   ├── image
    │   │   │   │   ├── mask_1.png
    │   │   │   │   ├── mask_2.png
    │   │   │   │   ├── no_mask_1.png
    │   │   │   │   └── no_mask_2.png
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
    │   │   ├── main_maskRecongition_image.py
    │   │   ├── main_maskRecongition_video.py
    │   │   ├── main_maskRecongition.ipynb
    │   │   ├── maskRecognizer.model
    │   │   └── train_maskRecongition.py
    │   └── text-recognition
    │       ├── assets
    │       │   ├── image
    │       │   │   └── test.png
    │       │   └── temp
    │       │       └── .keep
    │       ├── result
    │       │   └── tts
    │       │       ├── string.txt
    │       │       └── tts.mp3
    │       └── main_textRecognition.py
    ├── .gitattributes
    ├── .gitginore
    ├── LICENSE
    └── README.md

## 👨🏻‍💻 Development Environment

### Devices

- Raspberry Pi 4 Model B 4GB

### System

- macOS Monterey 12.0 Beta (21A5506) ARM
- Windows 11 Pro 21H2
- Ubuntu 20.04.3 LTS 64-bit ARM (ARMv8/AArch64)

### Tools

- PyCharm Professional
- Visual Studio Code

## ⭐️ Licensing

The MIT License 2021 KIM DONGHEE

<a href="https://github.com/DEVHEE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=KIM%20DONGHEE&color=000000"></a>