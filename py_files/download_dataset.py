"""
Script untuk download dataset FIFA menggunakan Kaggle Hub API
"""

import kagglehub
import os

def download_fifa_dataset():
    """
    Download dataset FIFA menggunakan Kaggle Hub API
    """
    print("="*60)
    print("DOWNLOAD DATASET FIFA PLAYERS")
    print("="*60)
    
    try:
        # Download dataset
        print("\n[INFO] Sedang mengunduh dataset dari Kaggle...")
        path = kagglehub.dataset_download("stefanoleone992/fifa-22-complete-player-dataset")
        print(f"[OK] Dataset berhasil diunduh!")
        print(f"[OK] Path: {path}")
        
        # List file yang didownload
        print("\n[INFO] File yang tersedia:")
        if os.path.exists(path):
            files = os.listdir(path)
            for file in files:
                print(f"  - {file}")
        
        # Cari file CSV
        csv_files = [f for f in files if f.endswith('.csv')]
        
        if csv_files:
            print(f"\n[OK] File CSV ditemukan: {csv_files[0]}")
            
            # Copy file ke folder proyek
            import shutil
            source_file = os.path.join(path, csv_files[0])
            destination_file = "fifa_players.csv"
            
            if os.path.exists(destination_file):
                print(f"[WARNING] File 'fifa_players.csv' sudah ada")
                response = input("Apakah ingin mengganti? (y/n): ")
                if response.lower() != 'y':
                    print("Download dibatalkan")
                    return
            
            print(f"[INFO] Menyalin file ke: {destination_file}")
            shutil.copy2(source_file, destination_file)
            print("[OK] Dataset siap digunakan!")
            print("\n" + "="*60)
            print("ANALISIS SIAP DILAKUKAN!")
            print("="*60)
            print("\nJalankan salah satu:")
            print("1. python football_analysis.py")
            print("2. jupyter notebook demo_analysis.ipynb")
            print("="*60)
        else:
            print("\n[ERROR] File CSV tidak ditemukan dalam dataset")
            print("   Mohon cek path dan file secara manual")
            
    except Exception as e:
        print(f"\n[ERROR] Error saat download: {e}")
        print("\nPastikan:")
        print("1. kagglehub sudah terinstall: pip install kagglehub")
        print("2. Internet tersambung")
        print("3. Coba jalankan script lagi")

if __name__ == "__main__":
    download_fifa_dataset()

