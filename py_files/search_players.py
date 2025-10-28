# -*- coding: utf-8 -*-
import pandas as pd
import os
import unicodedata

def normalize_string(s):
    """Menghapus accent dari string untuk mempermudah pencarian"""
    if pd.isna(s):
        return s
    try:
        # Coba normalisasi dengan UTF-8
        s = str(s).encode('latin-1').decode('utf-8')
        s = unicodedata.normalize('NFD', s)
        return ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    except:
        # Fallback: hapus karakter khusus secara manual
        s = str(s)
        replacements = {
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
            'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
            'ç': 'c', 'ñ': 'n', 'ß': 's'
        }
        for old, new in replacements.items():
            s = s.replace(old, new).replace(old.upper(), new.upper())
        return s

def display_safe(s):
    """Menampilkan string yang sudah dinormalisasi (tanpa accent) untuk Windows console"""
    if pd.isna(s):
        return str(s)
    # Tampilkan versi yang sudah dinormalisasi untuk konsistensi
    return normalize_string(s)

def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'csv_files', 'fifa_players.csv')
    try:
        df = pd.read_csv(csv_path, low_memory=False, encoding='latin-1')
        print('[OK] Data berhasil dimuat:', len(df), 'pemain ditemukan')
        return df
    except Exception as e:
        print('[ERROR] Error saat memuat data:', e)
        return None

def search_by_name(df):
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN NAMA')
    print('='*60)
    name = input('\nMasukkan nama pemain yang dicari: ').strip()
    if not name:
        print('[X] Nama tidak boleh kosong!')
        return
    
    # Normalize input dan nama pemain untuk mempermudah pencarian (tanpa accent)
    normalized_name = normalize_string(name.lower())
    df['normalized_name'] = df['long_name'].apply(normalize_string)
    results = df[df['normalized_name'].str.contains(normalized_name, case=False, na=False)]
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dengan nama', name, 'ditemukan')
    else:
        print('\n[OK] Ditemukan', len(results), 'pemain:')
        print('\n' + '-'*60)
        for idx, row in results.head(20).iterrows():
            print('\nNama:', display_safe(row['long_name']))
            print('Usia:', row['age'], 'tahun')
            print('Posisi:', display_safe(row['player_positions']))
            print('Overall:', row['overall'])
            print('Potential:', row['potential'])
            print('Klub:', display_safe(row['club_name']))
            print('Negara:', display_safe(row['nationality_name']))
            print('-'*60)
        if len(results) > 20:
            print('\n... dan', len(results) - 20, 'pemain lainnya')

def search_by_club(df):
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN KLUB')
    print('='*60)
    club = input('\nMasukkan nama klub yang dicari: ').strip()
    if not club:
        print('[X] Nama klub tidak boleh kosong!')
        return
    
    # Normalize input dan nama klub
    normalized_club = normalize_string(club.lower())
    df['normalized_club'] = df['club_name'].apply(normalize_string)
    results = df[df['normalized_club'].str.contains(normalized_club, case=False, na=False)]
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dari klub', club, 'ditemukan')
    else:
        print('\n[OK] Ditemukan', len(results), 'pemain dari klub', club)
        print('\n' + '-'*60)
        results_sorted = results.sort_values('overall', ascending=False).head(15)
        for idx, row in results_sorted.iterrows():
            print('\nNama:', display_safe(row['long_name']))
            print('Posisi:', display_safe(row['player_positions']))
            print('Overall:', row['overall'], '| Potential:', row['potential'])
            print('Usia:', row['age'], 'tahun')
            print('-'*60)
        if len(results) > 15:
            print('\n... dan', len(results) - 15, 'pemain lainnya')

def search_by_country(df):
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN NEGARA')
    print('='*60)
    country = input('\nMasukkan nama negara yang dicari: ').strip()
    if not country:
        print('[X] Nama negara tidak boleh kosong!')
        return
    
    # Normalize input dan nama negara
    normalized_country = normalize_string(country.lower())
    df['normalized_country'] = df['nationality_name'].apply(normalize_string)
    results = df[df['normalized_country'].str.contains(normalized_country, case=False, na=False)]
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dari negara', country, 'ditemukan')
    else:
        print('\n[OK] Ditemukan', len(results), 'pemain dari negara', country)
        print('\n' + '-'*60)
        results_sorted = results.sort_values('overall', ascending=False).head(15)
        for idx, row in results_sorted.iterrows():
            print('\nNama:', display_safe(row['long_name']))
            print('Posisi:', display_safe(row['player_positions']))
            print('Overall:', row['overall'], '| Potential:', row['potential'])
            print('Klub:', display_safe(row['club_name']))
            print('Usia:', row['age'], 'tahun')
            print('-'*60)
        if len(results) > 15:
            print('\n... dan', len(results) - 15, 'pemain lainnya')

def show_menu():
    print('\n' + '='*60)
    print('         PENCARIAN DATA PEMAIN FIFA')
    print('='*60)
    print('\nPilih opsi pencarian:')
    print('1. Cari berdasarkan nama pemain')
    print('2. Cari berdasarkan klub')
    print('3. Cari berdasarkan negara')
    print('0. Keluar')
    print('='*60)

def main():
    print('\nMemuat data pemain...')
    df = load_data()
    if df is None:
        print('\nProgram tidak dapat berjalan tanpa data.')
        return
    while True:
        show_menu()
        choice = input('\nMasukkan pilihan (1-3, atau 0 untuk keluar): ').strip()
        if choice == '0':
            print('\nTerima kasih telah menggunakan program ini!')
            break
        elif choice == '1':
            search_by_name(df)
        elif choice == '2':
            search_by_club(df)
        elif choice == '3':
            search_by_country(df)
        else:
            print('\n[X] Pilihan tidak valid! Masukkan angka 1, 2, 3, atau 0.')
        input('\nTekan Enter untuk melanjutkan...')

if __name__ == '__main__':
    main()

