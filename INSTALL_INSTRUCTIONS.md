# 📥 Instruksi Download Dataset

## ✅ Step 1: Dependencies Sudah Terinstall

Semua library Python yang diperlukan sudah terpasang:
- ✅ pandas
- ✅ numpy  
- ✅ matplotlib
- ✅ seaborn
- ✅ jupyter

## 📥 Step 2: Download Dataset

Sekarang Anda perlu download dataset pemain sepak bola. Ada beberapa opsi:

### Opsi A: Kaggle (Recommended)

1. Kunjungi: https://www.kaggle.com/stefanoleone992/fifa-22-complete-player-dataset
2. Klik tombol **Download** (akan mendownload zip file)
3. Ekstrak file zip
4. Cari file CSV (biasanya bernama `players_22.csv` atau similar)
5. **Renamed** file tersebut menjadi: `fifa_players.csv`
6. Pindahkan ke folder proyek: `c:\Users\Kevin\Downloads\FootballDS\`

### Opsi B: Kaggle Alternative

Atau coba dataset lain:
- https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset
- https://www.kaggle.com/datasets/ekapryadef/complete-fifa-player-dataset

### Opsi C: Dataset Minimal untuk Testing

Jika ingin dataset kecil untuk testing dulu, gunakan ini:
- https://www.kaggle.com/datasets/cashncarry/fifa-23-complete-player-dataset
- Download dan ekstrak file CSV

## 📂 Step 3: Pastikan File di Lokasi Benar

Setelah download, struktur folder Anda harus seperti ini:

```
📁 FootballDS/
├── 📄 fifa_players.csv  ← PASTIKAN FILE INI ADA
├── 📄 football_analysis.py
├── 📄 demo_analysis.ipynb
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 INSTALL_INSTRUCTIONS.md
```

## ▶️ Step 4: Jalankan Analisis

Setelah file dataset ada, jalankan salah satu:

### Menggunakan Python Script:
```bash
python football_analysis.py
```

### Menggunakan Jupyter Notebook:
```bash
jupyter notebook demo_analysis.ipynb
```

## 📊 Dataset Kolom yang Dibutuhkan

Script ini otomatis mencari kolom berikut (beradaptasi jika nama berbeda):
- `name` - Nama pemain
- `club` - Klub
- `nationality` - Kewarganegaraan
- `age` - Usia
- `overall` - Overall rating
- `passing` - Kemampuan passing
- `position` - Posisi bermain

## ⚠️ Troubleshooting

**Error: File tidak ditemukan**
```
✗ File fifa_players.csv tidak ditemukan
```
- Pastikan nama file tepat: `fifa_players.csv` (case sensitive)
- Pastikan file ada di folder `FootballDS`
- Cek menggunakan: `dir` (untuk list file)

**Error: Kolom tidak ditemukan**
- Script akan otomatis beradaptasi
- Jika masih error, cek kolom dataset dengan: `df.columns.tolist()`

---

**Selesai! Happy Analyzing! 🎉**

