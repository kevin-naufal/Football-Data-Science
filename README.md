# ⚽ Football Data Science - Pencarian & Analisis Statistik Pemain Sepak Bola

Proyek data science untuk mencari dan menganalisis statistik pemain sepak bola menggunakan dataset FIFA 22 dengan **19,000+ pemain**.

## 📋 Deskripsi

Proyek ini menyediakan sistem pencarian interaktif dan analisis data pemain sepak bola dengan fitur:

### 🎯 Fitur Pencarian Interaktif
- ✅ **Pencarian berdasarkan nama pemain** - dengan normalisasi karakter khusus (è, é, ü, dll)
- ✅ **Pencarian berdasarkan klub** - pilih liga, lalu klub
- ✅ **Pencarian berdasarkan negara** - dengan daftar negara lengkap
- ✅ **Pencarian berdasarkan potensi (range)** - Wo顯示range min/max
- ✅ **Pencarian berdasarkan umur (range)** - Wo顯示range min/max
- ✅ **Pencarian berdasarkan posisi** - dengan daftar posisi lengkap
- 🔍 **Filter lanjutan** - tambahkan multiple filter untuk hasil lebih spesifik
- 🎛️ **Menu dinamis** - filter yang sudah digunakan tidak muncul lagi

### 📊 Analisis Data
- ✅ **Top 10 pemain dengan passing terbaik**
- ✅ **Top 10 pemain dengan potensi tertinggi**
- ✅ **Top 10 pemain muda (U-20) dengan potensi tertinggi**
- ✅ **Top 10 defender muda (U-18) dengan potensi tertinggi**

## 🚀 Cara Menggunakan

### 1. Instalasi Dependencies

Buka terminal di folder proyek dan jalankan:

```bash
pip install -r requirements.txt
```

### 2. Persiapan Dataset

Pastikan file `csv_files/fifa_players.csv` sudah tersedia.

**Download Manual:** [Kaggle - FIFA 22 Complete Player Dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

### 3. Menjalankan Pencarian Interaktif ⭐

Program utama untuk mencari pemain:

```bash
python py_files/search_players.py
```

**Fitur Pencarian:**
1. **Pilih opsi pencarian** (1-6):
   - Nama pemain
   - Klub (dengan pilihan liga)
   - Negara (dengan daftar negara)
   - Potensi range (dengan min/max)
   - Umur range (dengan min/max)
   - Posisi (dengan daftar posisi)
   
2. **Tampilkan hasil** (10 pemain pertama)

3. **Tambah filter lanjutan** (opsional):
   - Filter klub, negara, potensi, umur, atau posisi
   - Opsi yang sudah digunakan tidak muncul lagi
   - Bisa melihat hasil kapan saja (Opsi 6)
   
4. **Tampilkan hasil akhir**

**Contoh Alur:**
```
Menu → Pilih 2 (Klub) → Pilih Liga → Pilih Klub → Tampilkan 10 hasil
→ Tambah filter? (y/n) → Jika ya → Menu filter → Pilih 4 (Umur)
→ Lihat range min/max → Masukkan range → Tampilkan hasil
```

### 4. Analisis Data (Opsional)

Semua hasil analisis akan tersimpan di:
- `csv_files/` - Data CSV
- `png_files/` - Visualisasi gambar

#### Jupyter Notebook
```bash
jupyter notebook demo_analysis.ipynb
```

## 📊 Fitur Pencarian

### Pencarian Fleksibel
- **Nama**: Cari dengan atau tanpa accent (Messi, Mbappé, Müller)
- **Klub**: Pilih dari 50+ liga, lalu pilih klub
- **Negara**: Pilih dari 150+ negara
- **Potensi**: Masukkan range dengan melihat min/max
- **Umur**: Masukkan range dengan melihat min/max
- **Posisi**: Pilih dari posisi yang tersedia

### Filter Lanjutan
- Gunakan multiple filter untuk hasil lebih spesifik
- Setiap filter mengurangi hasil pencarian
- Dapat melihat range min/mức pada tiap filter
- Opsi filter yang sudah digunakan tersembunyi

### Penanganan Karakter Khusus
- Otomatis menghandle karakter seperti é, ü, ç, ñ
- Tampilan di Windows console aman
- Pencarian tetap bekerja meskipun mengetik tanpa accent

## 📁 Struktur File

```
FootballDS/
├── 📁 py_files/              # Script Python
│   └── search_players.py            # ⭐ PROGRAM UTAMA - Pencarian interaktif
│
├── 📁 csv_files/             # Dataset & Hasil Analisis
│   └── fifa_players.csv             # ⭐ DATASET UTAMA (harus di-download manual)
│
├── 📁 png_files/             # Visualisasi Grafik (opsional)
│
├── 📄 demo_analysis.ipynb    # Jupyter Notebook untuk eksplorasi
├── 📄 requirements.txt        # Dependencies
├── 📄 README.md              # Dokumentasi proyek
└── 📄 .gitignore              # Git ignore rules
```

**Note:** File `fifa_players.csv` (~109 MB) **harus di-download manual** dan diletakkan di folder `csv_files/`.

## 📦 Dependencies

- **pandas** - Manipulasi dan analisis data
- **numpy** - Operasi matematika
- **matplotlib** - Visualisasi data dasar
- **seaborn** - Visualisasi data lanjutan
- **jupyter** - Notebook interaktif

## 🔍 Contoh Penggunaan

### Pencarian Nama Pemain
```
Menu → 1 (Nama) → mbappe
✓ Found 1 player: Kylian Mbappe

Apakah Anda ingin menambahkan filter? (y/n): n
```

### Pencarian Klub dengan Filter
```
Menu → 2 (Klub) → Pilih Liga 18 (English Premier League)
→ Pilih Klub 61 (Manchester City)
✓ Found 25 players

Tambah filter? (y/n): y
Filter Menu → 4 (Umur) → Range: 20-30
✓ Filter applied: 15 pemain remaining

Lihat hasil sekarang? → 6
```

### Pencarian Potensi dengan Range
```
Menu → 4 (Potensi)
Potensi: [Paling rendah: 46] [Paling tinggi: 95]

Masukkan potensi minimum: 90
Masukkan potensi maksimum: 95
✓ Found 50 players with potential 90-95
```

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

