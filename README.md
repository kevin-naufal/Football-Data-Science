# ⚽ Football Data Science - Analisis Statistik Pemain Sepak Bola

Proyek data science untuk menganalisis statistik pemain sepak bola menggunakan dataset FIFA 22 dengan 19,000+ pemain.

## 📋 Deskripsi

Proyek ini melakukan berbagai analisis data pemain sepak bola dengan fokus pada:
- ✅ **Top 10 pemain dengan passing terbaik**
- ✅ **Top 10 pemain dengan potensi tertinggi**
- ✅ **Top 10 pemain muda (U-20) dengan potensi tertinggi**
- ✅ **Top 10 defender muda (U-18) dengan potensi tertinggi**
- 📊 **Visualisasi data interaktif**

## 🚀 Cara Menggunakan

### 1. Instalasi Dependencies

Buka terminal di folder proyek dan jalankan:

```bash
pip install -r requirements.txt
```

### 2. Persiapan Dataset

Download dataset otomatis menggunakan script Python:

```bash
cd py_files
python download_dataset.py
```

Script ini akan mengunduh dataset FIFA 22 dari Kaggle dan menempatkannya di folder `csv_files/`.

**Alternatif:** Download manual dari [Kaggle - FIFA 22 Complete Player Dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

### 3. Menjalankan Analisis

#### Top 10 Passers
```bash
python py_files/top_passers.py
```

#### Top 10 Potential
```bash
python py_files/top_potential.py
```

#### Top 10 Potential U-20
```bash
python py_files/top_potential_u20.py
```

#### Top 10 Defenders U-18
```bash
python py_files/top_defenders_u18.py
```

#### Jupyter Notebook
```bash
jupyter notebook demo_analysis.ipynb
```

Semua hasil analisis akan tersimpan di:
- `csv_files/` - Data CSV
- `png_files/` - Visualisasi gambar

## 📊 Analisis yang Dilakukan

### 1. Pemain dengan Passing Paling Akurat
Mencari 10 pemain teratas berdasarkan kemampuan passing mereka.

### 2. Korelasi Usia vs Overall Rating
Menganalisis hubungan antara usia pemain dengan rating keseluruhan mereka.

### 3. Top Klub dan Negara
Menemukan klub dan negara dengan rata-rata rating tertinggi.

### 4. Analisis Posisi
Membandingkan distribusi rating berdasarkan posisi pemain.

## 📁 Struktur File

```
FootballDS/
├── football_analysis.py      # Script Python utama
├── demo_analysis.ipynb        # Jupyter Notebook
├── requirements.txt            # Dependencies
├── README.md                   # Dokumentasi
└── fifa_players.csv           # Dataset (harus di-download sendiri)
```

## 📦 Dependencies

- **pandas** - Manipulasi dan analisis data
- **numpy** - Operasi matematika
- **matplotlib** - Visualisasi data dasar
- **seaborn** - Visualisasi data lanjutan
- **jupyter** - Notebook interaktif

## 🔍 Contoh Output

Script akan menghasilkan beberapa visualisasi:

1. **age_vs_rating.png** - Scatter plot korelasi usia vs rating
2. **top_clubs.png** - Bar chart top 10 klub
3. **top_nations.png** - Bar chart top 10 negara
4. **position_analysis.png** - Box plot distribusi rating per posisi

## 📝 Catatan

- Pastikan nama kolom dalam dataset sesuai dengan nama yang digunakan dalam script
- Script akan otomatis mengadaptasi kolom yang tersedia dalam dataset
- Beberapa kolom yang dicari: `name`, `club`, `nationality`, `age`, `overall`, `passing`, `position`

## 🛠️ Troubleshooting

### Error: File tidak ditemukan
- Pastikan file `fifa_players.csv` ada di folder yang sama
- Periksa nama file harus tepat: `fifa_players.csv`

### Error: Kolom tidak ditemukan
- Script akan otomatis mencoba kolom alternatif
- Cek kolom dataset Anda dan sesuaikan jika diperlukan

### Visualisasi tidak muncul
- Pastikan matplotlib backend terinstall dengan benar
- Gunakan: `pip install --upgrade matplotlib`

## 📚 Referensi Dataset

Dataset bisa didapatkan dari:
- [Kaggle](https://www.kaggle.com/datasets) - Cari "FIFA" atau "Football Players"
- [Data Science website](https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset)

## 👨‍💻 Author

Dibuat untuk analisis data science pembelajaran.

---

**Happy Analyzing! 🎉**

