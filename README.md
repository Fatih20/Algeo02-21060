# Algeo02-21060
Repository Tugas Besar Kedua Mata Kuliah Aljabar Linier dan Geometri

## Table of Contents
* [General Information](#general-information)
* [Languange Used](#languange-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Repository Structure](#repository-structure)
* [Setup](#setup)
* [How to Compile and Run](#how-to-compile-and-run)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contacts](#contacts)

## General Information
Sebuah program untuk pengenalan wajah dengan menggunakan metode eigenface. 
Repository ini dibuat dan mengandung file yang dibutuhkan untuk menyelesaikan Tugas Besar Kedua IF2123 Aljabar Linier dan Geometri.
Contributors: 
- 13521060 Fatih Nararya Rashadyfa I.
- 13521062 Go Dillon Audris
- 13521074 Eugene Yap Jin Quan

## Languange Used
- Python Languange (100%)

## Features
- Training terhadap data set agar komputer dapat melakukan pengenalan wajah
- Pengenalan wajah dengan menggunakan metode eigenface
- Kamera yang dapat mengenali wajah setiap 2 detik

## Screenshots
![image](https://user-images.githubusercontent.com/110383663/203105117-78a4a688-65fe-4f78-95d8-358d636c887c.png)

## Repository Structure
```bash
.
│   README.md
│   
├───doc
│      Algeo02-21060.pdf
│
├───src
│   ├───_pycache_
│   │      eigen_function.cpython-310.pyc
│   │      kivy.cpython-310.pyc
│   │      processing.cpython-310.pyc
│   │
│   └───Images
│          placeHolderImage.png
│          bg.jfif
│          cameraImage.jpg
│          cameraImage.png
│       
│       processing.py
│       eigen_function.py
│       App.py
│       GUI.kv
│
└───test
       trainingSet1
       trainingSet2
       trainingSet3
       trainingSet4
```

## Setup
Pastikan anda telah menginstall beberapa library python yang dibutuhkan yaitu:
1. Kivy     : python -m pip install kivy
2. Numpy    : python -m pip install numpy
3. OpenCV   : python -m pip install opencv-python
4. Plyer    : python -m pip install plyer

## How to Compile and Run
Setelah setup berhasil dilakukan, ikuti langkah dibawah untuk menjalankan program:
1. Masuk ke dalam folder src
2. Masukkan command 'python App.py' untuk menjalankan program

Note: Jika program tiba-tiba berhenti berjalan dan memunculkan pesan error "No such file/directory found: Images/cameraImage.png", cukup reload terminal dan jalankan ulang program.

## Project Status
Proyek ini telah selesai secara utuh (Completed)

## Acknowledgements
- Terima kasih kepada Tuhan yang Maha Esa
- Terima kasih kepada para dosen pengampu: Pak Judhi, Pak Rinaldi, dan Pak Rila
- Terima kasih kepada Tim Asisten Kuliah IF2123

## Contacts
Diciptakan dan diatur oleh Pepsiman
![](https://user-images.githubusercontent.com/110383663/199404321-43752715-8edc-4269-a4fa-8860e846a63b.png)
