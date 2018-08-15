# ALPR-Project
Project untuk mendeteksi dan membaca nomor plat Indonesia

Plate Number Recognition adalah aplikasi yang di tulis dalam python, opencv, openalpr dan Tesseract. Aplikasi ini dapat menganalisis gambar maupun video yang di dalamnya terdapat gambar plat yang kemudian di identifikasikan dengan output string.

Depedencies :

-	Python (https://www.python.org/downloads/)

-	Tesseract v 4.00 ( https://github.com/tesseract-ocr/tesseract )

-	Openalpr ( https://github.com/openalpr/openalpr )

-	OpenCV v3.4.1 ( https://github.com/opencv/opencv )

-	Project ( https://github.com/luthfitabey/ALPR-Project )

Usage :
1. Mengatur masukan source yang akan dideteksi pada file vid.py
   Line 19-20	: Masukan berupa video stream
   Line 21	: Masukan berupa video maupun gambar
   Line 22	: Masukan berupa video dari webcam PC

2.	Menjalan aplikasi menggunakan terminal(ubuntu)/CMD(windows) di dalam direktori aplikasi command: $ python vid.py

  # Cara untuk menambahkan sampel foto ke train detector ada di link berikut:
   https://github.com/openalpr/train-detector

1. Download repository pada link di atas

2. Crop plat pada foto

3. Hasil crop tersebut diberi nama sesuai dengan nomor plat yang di crop seperti contoh,anda sedang memotong foto untuk plat AB 4413   DW, maka hasil tersebut diberi nama “AB4413DW”,dan harus konsisten memberi format gambar jika JPG maka JPG semua jika PNG maka PNG         semua
4. Kemudian hasil crop di masukan di 1 folder yang sama

5. Kemudian Edit file Prep.py ,kemudian ke Line-31 edit menjadi “BASE_DIT + [Folder tempat menyimpan hasil crop] +’/’ ”

6. Kemudian buka terminal di directory train-detector

7. Jalankan command-command ini:
```
      •	rm ./out/* (Menghapus isi directory ‘out’)
   
      •	./prep.py neg (menyiapkan gambar negatif)
   
      •	./prep.py pos (menyiapkan gambar positif)
   
      •	./prep.py train (mempersiapkan training data)
   
      •	Setelah prep.py dijalankan maka terdapat command yang siap dijalankan kembali,lalu copy-paste command tersebut, sebelum dijalankan command tersebut ubahlah stages menjadi maksimal 11, kemudian ubah nilai numPos ¼ dari total gambar yang ingin di train kemudian enter.
   
      •	Kemudian hasil dari train tersebut bisa di lihat di directory out, kemudian copy cascade.xml ke runtime anda.
```
   
> Kekurangan dari aplikasi ini adalah kurangnya keakuratan dari pendeteksian plat itu, penyebabnya adalah kurangnya sampel foto plat yang saat ini di gunakan baru sekitar 2400 sampel foto yang jika di lihat dari sampel foto negara yang sudah jadi sekitar 8000 sampel foto.
