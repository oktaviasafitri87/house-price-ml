#Prediksi Harga Rumah Menggunakan Linear Regression

##Deskripsi Proyek
Proyek ini merupakan tugas Ujian Akhir Semester (UAS) pada mata kuliah Machine Learning.  
Tujuan dari proyek ini adalah membangun sistem prediksi harga rumah menggunakan algoritma Linear Regression, kemudian mengimplementasikannya dalam bentuk API menggunakan FastAPI dan antarmuka web sederhana (HTML).

Sistem ini memungkinkan pengguna memasukkan beberapa atribut rumah dan mendapatkan hasil prediksi harga rumah.

##
- Nama: Oktavia Safitri Ramadani  
- NPM : 2441055
- Mata Kuliah: Machine Learning  
- Jenis Tugas: Project UAS  

##Dataset
- Nama Dataset: House Price Dataset  
- Sumber: Kaggle  
- Format: CSV  

Dataset digunakan untuk melatih model machine learning dalam memprediksi harga rumah berdasarkan beberapa fitur.
Catatan: Dataset bersifat simulasi sehingga hasil prediksi tidak merepresentasikan harga rumah riil.

##Algoritma yang Digunakan
- Linear Regression
- StandardScaler
- Train-Test Split

##Alur Sistem
1. Dataset dibaca dari file CSV
2. Data dilakukan preprocessing dan normalisasi
3. Model Linear Regression dilatih
4. Model disimpan dalam file .pkl
5. Model dimuat ke FastAPI
6. Frontend HTML mengirim data ke API
7. API mengembalikan hasil prediksi harga rumah

##Struktur Folder
house-price-ml/
├── train.py
├── main.py
├── index.html
├── house_price.csv
├── model_house_price.pkl
└── readme.md

##Cara Menjalankan Proyek
### 1. Install Library
### 2. Training Model
### 3. Menjalankan FastAPI
### 4. Menjalankan Web
- Buka file index.html di browser
- Masukkan data rumah
- Klik tombol Prediksi Harga
- Hasil akan ditampilkan dalam format Rupiah

##Kesimpulan
Proyek ini berhasil mengimplementasikan:
- Machine Learning menggunakan Linear Regression
- REST API dengan FastAPI
- Frontend web sederhana
- Integrasi end-to-end dari dataset hingga prediksi
Proyek ini dibuat untuk keperluan akademik dan pembelajaran.

