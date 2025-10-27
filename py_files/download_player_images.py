"""
Script untuk Download Gambar Muka Pemain dari URL
"""

import pandas as pd
import requests
from pathlib import Path
import sys

def download_player_images():
    """
    Download gambar muka pemain dari URL di dataset
    """
    print("="*60)
    print("DOWNLOAD GAMBAR MUKA PEMAIN")
    print("="*60)
    
    try:
        # Load data
        df = pd.read_csv('csv_files/fifa_players.csv', low_memory=False)
        print(f"[OK] Data berhasil dimuat: {len(df)} pemain\n")
        
        # Buat folder images
        img_folder = Path('player_images')
        img_folder.mkdir(exist_ok=True)
        
        # Cek kolom gambar
        if 'player_face_url' in df.columns and 'short_name' in df.columns:
            print(f"[INFO] Menemukan {len(df)} URL gambar muka pemain")
            print(f"[INFO] Folder penyimpanan: {img_folder}/")
            
            # Pilih beberapa pemain populer untuk download (contoh)
            top_players = df.nlargest(10, 'overall')
            
            print("\n" + "="*60)
            print("DOWNLOAD GAMBAR (TOP 10 PLAYERS)")
            print("="*60)
            
            for idx, (_, row) in enumerate(top_players.iterrows(), 1):
                player_name = row['short_name']
                url = row['player_face_url']
                
                if pd.notna(url):
                    # Clean filename
                    filename = player_name.replace(' ', '_').replace('/', '_') + '.png'
                    filepath = img_folder / filename
                    
                    try:
                        print(f"\n{idx}. Downloading {player_name}...")
                        response = requests.get(url, timeout=10)
                        
                        if response.status_code == 200:
                            filepath.write_bytes(response.content)
                            print(f"   [OK] Berhasil: {filename}")
                        else:
                            print(f"   [FAIL] Status: {response.status_code}")
                            
                    except Exception as e:
                        print(f"   [ERROR] {str(e)[:50]}")
                else:
                    print(f"{idx}. {player_name} - URL tidak tersedia")
            
            print("\n" + "="*60)
            print(f"DOWNLOAD SELESAI!")
            print(f"Gambar tersimpan di: {img_folder.absolute()}/")
            print("="*60)
            
        else:
            print("[ERROR] Kolom 'player_face_url' tidak ditemukan")
            
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    download_player_images()

