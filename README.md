# Algeo02-21060
Repository Tugas Besar Kedua Mata Kuliah Aljabar Linier dan Geometri

## Table of Contents
1. [ General Information. ] (#genInfo)
2. [ Languange Used. ] (#langUsed)
3. [ Features. ] (#feat)
4. [ Screenshots. ] (#ss)
5. [ Repository Structure] (#repoStruct)
6. [ Setup. ] (#setup)
7. [ How to Compile and Run. ] (#howTo)
8. [ Project Status. ] (#status)
9. [ Acknowledgements. ] (#acc)
10. [ Contacts. ] (#contacts)

<a name ="genInfo"></a>
## General Information
Sebuah program untuk pengenalan wajah dengan menggunakan metode eigenface. 
Repository ini dibuat dan mengandung file yang dibutuhkan untuk menyelesaikan Tugas Besar Kedua IF2123 Aljabar Linier dan Geometri.
Contributors: 
- 13521060 Fatih Nararya Rashadyfa I.
- 13521062 Go Dillon Audris
- 13521074 Eugene Yap Jin Quan

<a name ="langUsed"></a>
## Languange Used
- Python Languange (100%)

<a name ="feat"></a>
## Features
- Training terhadap data set agar komputer dapat melakukan pengenalan wajah
- Pengenalan wajah dengan menggunakan metode eigenface
- Kamera yang dapat mengenali wajah setiap 2 detik

<a name ="ss"></a>
## Screenshots

<a name ="repoStruct"></a>
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
<a name ="setup"></a>
## Setup
Pastikan anda telah menginstall beberapa library python yang dibutuhkan yaitu:
1. Kivy     : python -m pip install kivy
2. Numpy    : python -m pip install numpy
3. OpenCV   : python -m pip install opencv-python
4. Plyer    : python -m pip install plyer

<a name ="howTo"></a>
## How to Compile and Run
Setelah setup berhasil dilakukan, ikuti langkah dibawah untuk menjalankan program:
1. Masuk ke dalam folder src
2. Masukkan command 'python App.py' untuk menjalankan program

Note: Jika program tiba-tiba berhenti berjalan dan memunculkan pesan error "No such file/directory found: Images/cameraImage.png", cukup reload terminal dan jalankan ulang program.

<a name ="status"></a>
## Project Status
Proyek ini telah selesai secara utuh (Completed)

<a name ="acc"></a>
## Acknowledgements
- Terima kasih kepada Tuhan yang Maha Esa
- Terima kasih kepada para dosen pengampu: Pak Judhi, Pak Rinaldi, dan Pak Rila
- Terima kasih kepada Tim Asisten Kuliah IF2123

<a name ="contacts"></a>
## Contacts
Diciptakan dan diatur oleh Pepsiman
![](https://user-images.githubusercontent.com/110383663/199404321-43752715-8edc-4269-a4fa-8860e846a63b.png)
