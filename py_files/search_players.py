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
    """Memuat data pemain dari file CSV"""
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'csv_files', 'fifa_players.csv')
    try:
        df = pd.read_csv(csv_path, low_memory=False, encoding='latin-1')
        print('[OK] Data berhasil dimuat:', len(df), 'pemain ditemukan')
        return df
    except FileNotFoundError:
        print('[ERROR] File tidak ditemukan di', csv_path)
        return None
    except Exception as e:
        print('[ERROR] Error saat memuat data:', e)
        return None

def search_by_name(df):
    """Mencari pemain berdasarkan nama"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN NAMA')
    print('='*60)
    name = input('\nMasukkan nama pemain yang dicari: ').strip()
    if not name:
        print('[X] Nama tidak boleh kosong!')
        return
    
    # Normalize input dan nama pemain
    normalized_name = normalize_string(name.lower())
    df['normalized_name'] = df['long_name'].apply(normalize_string)
    results = df[df['normalized_name'].str.contains(normalized_name, case=False, na=False)]
    
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dengan nama', name, 'ditemukan')
        return
    
    print('\n[OK] Ditemukan', len(results), 'pemain')
    
    # Tampilkan hasil awal dan tanya apakah ingin filter lanjutan
    display_results(results, limit=10)
    
    if len(results) > 10:
        print('\n[TIP] Gunakan filter untuk memperkecil hasil pencarian')
    
    filter_choice = input('\nApakah Anda ingin menambahkan filter? (y/n): ').strip().lower()
    
    if filter_choice == 'y':
        final_results = apply_filter(df, results, disabled_options={'name'})
        print('\n' + '='*60)
        print('HASIL AKHIR')
        print('='*60)
        display_results(final_results, limit=20)

def search_by_club(df):
    """Mencari pemain berdasarkan klub"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN KLUB')
    print('='*60)
    
    # Tampilkan daftar liga
    leagues = df['league_name'].dropna().unique()
    leagues = sorted(leagues)
    
    print('\nDaftar Liga:')
    for i, league in enumerate(leagues, 1):
        print(f'{i}. {display_safe(league)}')
    
    try:
        league_choice = int(input('\nPilih nomor liga (atau 0 untuk skip): ').strip())
        if league_choice == 0:
            club = input('\nMasukkan nama klub yang dicari: ').strip()
            if not club:
                print('[X] Nama klub tidak boleh kosong!')
                return
        elif 1 <= league_choice <= len(leagues):
            league = leagues[league_choice - 1]
            
            # Tampilkan klub dari liga tersebut
            clubs_in_league = df[df['league_name'] == league]['club_name'].dropna().unique()
            clubs_in_league = sorted(clubs_in_league)
            
            print(f'\nDaftar Klub di {display_safe(league)}:')
            for i, club_name in enumerate(clubs_in_league, 1):
                print(f'{i}. {display_safe(club_name)}')
            
            club_choice = int(input('\nPilih nomor klub: ').strip())
            if 1 <= club_choice <= len(clubs_in_league):
                club = clubs_in_league[club_choice - 1]
            else:
                print('[X] Pilihan tidak valid!')
                return
        else:
            print('[X] Pilihan tidak valid!')
            return
    except ValueError:
        print('[X] Masukkan angka!')
        return
    
    # Cari langsung dengan nama klub yang dipilih (exact match)
    results = df[df['club_name'] == club]
    
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dari klub', display_safe(club), 'ditemukan')
        return
    
    print('\n[OK] Ditemukan', len(results), 'pemain dari klub', display_safe(club))
    display_results(results, limit=10)
    
    filter_choice = input('\nApakah Anda ingin menambahkan filter? (y/n): ').strip().lower()
    
    if filter_choice == 'y':
        final_results = apply_filter(df, results, disabled_options={'club'})
        print('\n' + '='*60)
        print('HASIL AKHIR')
        print('='*60)
        display_results(final_results, limit=20)

def search_by_country(df):
    """Mencari pemain berdasarkan negara"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN NEGARA')
    print('='*60)
    # Tampilkan daftar negara
    countries = df['nationality_name'].dropna().unique()
    countries = sorted(countries)
    
    print('\nDaftar Negara:')
    for i, country_name in enumerate(countries, 1):
        print(f'{i}. {display_safe(country_name)}')
    
    try:
        country_choice = int(input('\nPilih nomor negara: ').strip())
        if 1 <= country_choice <= len(countries):
            country = countries[country_choice - 1]
        else:
            print('[X] Pilihan tidak valid!')
            return
    except ValueError:
        print('[X] Masukkan angka!')
        return
    
    # Normalize input dan nama negara
    normalized_country = normalize_string(country.lower())
    df['normalized_country'] = df['nationality_name'].apply(normalize_string)
    results = df[df['normalized_country'].str.contains(normalized_country, case=False, na=False)]
    
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dari negara', country, 'ditemukan')
        return
    
    print('\n[OK] Ditemukan', len(results), 'pemain dari negara', display_safe(country))
    display_results(results, limit=10)
    
    filter_choice = input('\nApakah Anda ingin menambahkan filter? (y/n): ').strip().lower()
    
    if filter_choice == 'y':
        final_results = apply_filter(df, results, disabled_options={'country'})
        print('\n' + '='*60)
        print('HASIL AKHIR')
        print('='*60)
        display_results(final_results, limit=20)

def search_by_potential(df):
    """Mencari pemain berdasarkan range potensi"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN POTENSI')
    print('='*60)
    
    # Tampilkan range terendah dan tertinggi
    min_pot_data = int(df['potential'].min())
    max_pot_data = int(df['potential'].max())
    
    print(f'\nPotensi:')
    print(f'[Paling rendah: {min_pot_data}]')
    print(f'[Paling tinggi: {max_pot_data}]')
    
    try:
        min_potential = input('\nMasukkan potensi minimum: ').strip()
        max_potential = input('Masukkan potensi maksimum: ').strip()
        
        min_pot = int(min_potential)
        max_pot = int(max_potential)
        
        if min_pot < 0 or max_pot > 100 or min_pot > max_pot:
            print('[X] Range tidak valid! Pastikan 0 <= minimum <= maksimum <= 100')
            return
        
        results = df[(df['potential'] >= min_pot) & (df['potential'] <= max_pot)]
        results_sorted = results.sort_values('potential', ascending=False).head(20)
        
        if len(results) == 0:
            print('\n[X] Tidak ada pemain dengan potensi', min_pot, '-', max_pot)
        else:
            print('\n[OK] Ditemukan', len(results), 'pemain dengan potensi', min_pot, '-', max_pot, ':')
            print('\n' + '-'*60)
            for idx, row in results_sorted.iterrows():
                print('\nNama:', display_safe(row['long_name']))
                print('Usia:', row['age'], 'tahun')
                print('Posisi:', display_safe(row['player_positions']))
                print('Overall:', row['overall'], '| Potential:', row['potential'])
                print('Klub:', display_safe(row['club_name']))
                print('Negara:', display_safe(row['nationality_name']))
                print('-'*60)
            
            if len(results) > 20:
                print('\n... dan', len(results) - 20, 'pemain lainnya (menampilkan 20 teratas)')
                
    except ValueError:
        print('[X] Input tidak valid! Masukkan angka saja.')
    except Exception as e:
        print('[ERROR] Error:', str(e))

def search_by_age(df):
    """Mencari pemain berdasarkan range umur"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN UMUR')
    print('='*60)
    
    # Tampilkan range terendah dan tertinggi
    min_age_data = int(df['age'].min())
    max_age_data = int(df['age'].max())
    
    print(f'\nUmur:')
    print(f'[Paling rendah: {min_age_data}]')
    print(f'[Paling tinggi: {max_age_data}]')
    
    try:
        min_age = input('\nMasukkan umur minimum: ').strip()
        max_age = input('Masukkan umur maksimum: ').strip()
        
        min_a = int(min_age)
        max_a = int(max_age)
        
        if min_a < 15 or max_a > 60 or min_a > max_a:
            print('[X] Range tidak valid! Pastikan 15 <= minimum <= maksimum <= 60')
            return
        
        results = df[(df['age'] >= min_a) & (df['age'] <= max_a)]
        results_sorted = results.sort_values('overall', ascending=False).head(20)
        
        if len(results) == 0:
            print('\n[X] Tidak ada pemain berumur', min_a, '-', max_a, 'tahun')
        else:
            print('\n[OK] Ditemukan', len(results), 'pemain berumur', min_a, '-', max_a, 'tahun:')
            print('\n' + '-'*60)
            for idx, row in results_sorted.iterrows():
                print('\nNama:', display_safe(row['long_name']))
                print('Usia:', row['age'], 'tahun')
                print('Posisi:', display_safe(row['player_positions']))
                print('Overall:', row['overall'], '| Potential:', row['potential'])
                print('Klub:', display_safe(row['club_name']))
                print('Negara:', display_safe(row['nationality_name']))
                print('-'*60)
            
            if len(results) > 20:
                print('\n... dan', len(results) - 20, 'pemain lainnya (menampilkan 20 teratas)')
                
    except ValueError:
        print('[X] Input tidak valid! Masukkan angka saja.')
    except Exception as e:
        print('[ERROR] Error:', str(e))

def search_by_position(df):
    """Mencari pemain berdasarkan posisi"""
    print('\n' + '='*60)
    print('PENCARIAN PEMAIN BERDASARKAN POSISI')
    print('='*60)
    
    # Tampilkan daftar posisi
    # Ambil semua posisi dari data dan unikkan
    all_positions = set()
    for pos in df['player_positions'].dropna():
        # Pisahkan jika ada multiple posisi (dipisahkan koma)
        for p in str(pos).split(','):
            all_positions.add(p.strip())
    
    positions_list = sorted(list(all_positions))
    
    print('\nDaftar Posisi:')
    for i, pos in enumerate(positions_list, 1):
        print(f'{i}. {display_safe(pos)}')
    
    try:
        pos_choice = int(input('\nPilih nomor posisi: ').strip())
        if 1 <= pos_choice <= len(positions_list):
            position = positions_list[pos_choice - 1]
        else:
            print('[X] Pilihan tidak valid!')
            return
    except ValueError:
        print('[X] Masukkan angka!')
        return
    
    # Normalize input
    normalized_position = normalize_string(position.lower())
    df['normalized_positions'] = df['player_positions'].apply(normalize_string)
    results = df[df['normalized_positions'].str.contains(normalized_position, case=False, na=False)]
    results_sorted = results.sort_values('overall', ascending=False).head(20)
    
    if len(results) == 0:
        print('\n[X] Tidak ada pemain dengan posisi', position)
    else:
        print('\n[OK] Ditemukan', len(results), 'pemain dengan posisi', display_safe(position), ':')
        print('\n' + '-'*60)
        for idx, row in results_sorted.iterrows():
            print('\nNama:', display_safe(row['long_name']))
            print('Usia:', row['age'], 'tahun')
            print('Posisi:', display_safe(row['player_positions']))
            print('Overall:', row['overall'], '| Potential:', row['potential'])
            print('Klub:', display_safe(row['club_name']))
            print('Negara:', display_safe(row['nationality_name']))
            print('-'*60)
        
        if len(results) > 20:
            print('\n... dan', len(results) - 20, 'pemain lainnya (menampilkan 20 teratas)')

def show_filter_menu(disabled_options=None):
    if disabled_options is None:
        disabled_options = set()
    print('\n' + '='*60)
    print('      FILTER TAMBAHAN')
    print('='*60)
    print('Pilih opsi filter:')
    if 'club' not in disabled_options:
        print('1. Filter berdasarkan klub')
    if 'country' not in disabled_options:
        print('2. Filter berdasarkan negara')
    if 'potential' not in disabled_options:
        print('3. Filter berdasarkan potensi (range)')
    if 'age' not in disabled_options:
        print('4. Filter berdasarkan umur (range)')
    if 'position' not in disabled_options:
        print('5. Filter berdasarkan posisi')
    print('6. Lihat hasil sekarang')
    print('0. Kembali ke menu utama')
    print('='*60)

def apply_filter(df, current_results, disabled_options=None):
    if disabled_options is None:
        disabled_options = set()
    results = current_results.copy()
    while True:
        show_filter_menu(disabled_options)
        choice = input('\nPilih filter (1-6, atau 0 untuk kembali): ').strip()
        if choice == '0':
            return results
        elif choice == '1' and 'club' not in disabled_options:
            # Tampilkan daftar liga dari hasil saat ini
            leagues = results['league_name'].dropna().unique()
            leagues = sorted(leagues)
            
            print('\nDaftar Liga:')
            for i, league in enumerate(leagues, 1):
                print(f'{i}. {display_safe(league)}')
            
            try:
                league_choice = int(input('\nPilih nomor liga: ').strip())
                if 1 <= league_choice <= len(leagues):
                    league = leagues[league_choice - 1]
                    
                    # Tampilkan klub dari liga tersebut
                    clubs_in_league = results[results['league_name'] == league]['club_name'].dropna().unique()
                    clubs_in_league = sorted(clubs_in_league)
                    
                    print(f'\nDaftar Klub di {display_safe(league)}:')
                    for i, club_name in enumerate(clubs_in_league, 1):
                        print(f'{i}. {display_safe(club_name)}')
                    
                    club_choice = int(input('\nPilih nomor klub: ').strip())
                    if 1 <= club_choice <= len(clubs_in_league):
                        club = clubs_in_league[club_choice - 1]
                        # Gunakan exact match untuk menghindari masalah encoding
                        results = results[results['club_name'] == club]
                        print('[OK] Filter klub diterapkan. Sisa:', len(results), 'pemain')
                        disabled_options.add('club')
                    else:
                        print('[X] Pilihan tidak valid!')
                else:
                    print('[X] Pilihan tidak valid!')
            except ValueError:
                print('[X] Masukkan angka!')
        elif choice == '2' and 'country' not in disabled_options:
            countries = results['nationality_name'].dropna().unique()
            countries = sorted(countries)
            print('\nDaftar Negara:')
            for i, country_name in enumerate(countries, 1):
                print(f'{i}. {display_safe(country_name)}')
            try:
                country_choice = int(input('\nPilih nomor negara: ').strip())
                if 1 <= country_choice <= len(countries):
                    country = countries[country_choice - 1]
                    normalized_country = normalize_string(country.lower())
                    results['normalized_country'] = results['nationality_name'].apply(normalize_string)
                    results = results[results['normalized_country'].str.contains(normalized_country, case=False, na=False)]
                    print('[OK] Filter negara diterapkan. Sisa:', len(results), 'pemain')
                    disabled_options.add('country')
                else:
                    print('[X] Pilihan tidak valid!')
            except ValueError:
                print('[X] Masukkan angka!')
        elif choice == '3' and 'potential' not in disabled_options:
            # Tampilkan range dari hasil saat ini
            min_pot_data = int(results['potential'].min())
            max_pot_data = int(results['potential'].max())
            print(f'\nPotensi pada hasil saat ini:')
            print(f'[Paling rendah: {min_pot_data}]')
            print(f'[Paling tinggi: {max_pot_data}]')
            
            try:
                min_pot = int(input('\nPotensi minimum: ').strip())
                max_pot = int(input('Potensi maksimum: ').strip())
                if 0 <= min_pot <= max_pot <= 100:
                    results = results[(results['potential'] >= min_pot) & (results['potential'] <= max_pot)]
                    print('[OK] Filter potensi diterapkan. Sisa:', len(results), 'pemain')
                    disabled_options.add('potential')
                else:
                    print('[X] Range tidak valid!')
            except ValueError:
                print('[X] Input tidak valid!')
        elif choice == '4' and 'age' not in disabled_options:
            # Tampilkan range dari hasil saat ini
            min_age_data = int(results['age'].min())
            max_age_data = int(results['age'].max())
            print(f'\nUmur pada hasil saat ini:')
            print(f'[Paling rendah: {min_age_data}]')
            print(f'[Paling tinggi: {max_age_data}]')
            
            try:
                min_a = int(input('\nUmur minimum: ').strip())
                max_a = int(input('Umur maksimum: ').strip())
                if 15 <= min_a <= max_a <= 60:
                    results = results[(results['age'] >= min_a) & (results['age'] <= max_a)]
                    print('[OK] Filter umur diterapkan. Sisa:', len(results), 'pemain')
                    disabled_options.add('age')
                else:
                    print('[X] Range tidak valid!')
            except ValueError:
                print('[X] Input tidak valid!')
        elif choice == '5' and 'position' not in disabled_options:
            all_positions = set()
            for pos in results['player_positions'].dropna():
                for p in str(pos).split(','):
                    all_positions.add(p.strip())
            positions_list = sorted(list(all_positions))
            print('\nDaftar Posisi:')
            for i, pos in enumerate(positions_list, 1):
                print(f'{i}. {display_safe(pos)}')
            try:
                pos_choice = int(input('\nPilih nomor posisi: ').strip())
                if 1 <= pos_choice <= len(positions_list):
                    position = positions_list[pos_choice - 1]
                    normalized_position = normalize_string(position.lower())
                    results['normalized_positions'] = results['player_positions'].apply(normalize_string)
                    results = results[results['normalized_positions'].str.contains(normalized_position, case=False, na=False)]
                    print('[OK] Filter posisi diterapkan. Sisa:', len(results), 'pemain')
                    disabled_options.add('position')
                else:
                    print('[X] Pilihan tidak valid!')
            except ValueError:
                print('[X] Masukkan angka!')
        elif choice == '6':
            display_results(results, limit=20)
            input('\nTekan Enter untuk kembali ke menu filter...')
            continue
        else:
            print('[X] Pilihan tidak valid atau opsi sudah digunakan!')
        print('\n[INFO] Hasil saat ini:', len(results), 'pemain')
        if len(results) == 0:
            print('[X] Tidak ada hasil setelah filter. Mengembalikan hasil sebelumnya.')
            return current_results

def display_results(results, limit=20):
    """Menampilkan hasil pencarian"""
    if len(results) == 0:
        print('[X] Tidak ada pemain ditemukan')
    else:
        results_sorted = results.sort_values('overall', ascending=False).head(limit)
        print('\n' + '-'*60)
        for idx, row in results_sorted.iterrows():
            print('\nNama:', display_safe(row['long_name']))
            print('Usia:', row['age'], 'tahun')
            print('Posisi:', display_safe(row['player_positions']))
            print('Overall:', row['overall'], '| Potential:', row['potential'])
            print('Klub:', display_safe(row['club_name']))
            print('Negara:', display_safe(row['nationality_name']))
            print('-'*60)
        
        if len(results) > limit:
            print('\n... dan', len(results) - limit, 'pemain lainnya (menampilkan', limit, 'teratas)')

def show_menu():
    """Menampilkan menu utama"""
    print('\n' + '='*60)
    print('         PENCARIAN DATA PEMAIN FIFA')
    print('='*60)
    print('\nPilih opsi pencarian:')
    print('1. Cari berdasarkan nama pemain')
    print('2. Cari berdasarkan klub')
    print('3. Cari berdasarkan negara')
    print('4. Cari berdasarkan potensi (range)')
    print('5. Cari berdasarkan umur (range)')
    print('6. Cari berdasarkan posisi')
    print('0. Keluar')
    print('='*60)

def main():
    """Fungsi utama program"""
    print('\nMemuat data pemain...')
    df = load_data()
    
    if df is None:
        print('\nProgram tidak dapat berjalan tanpa data.')
        return
    
    while True:
        show_menu()
        choice = input('\nMasukkan pilihan (1-6, atau 0 untuk keluar): ').strip()
        
        if choice == '0':
            print('\nTerima kasih telah menggunakan program ini!')
            break
        elif choice == '1':
            search_by_name(df)
        elif choice == '2':
            search_by_club(df)
        elif choice == '3':
            search_by_country(df)
        elif choice == '4':
            search_by_potential(df)
        elif choice == '5':
            search_by_age(df)
        elif choice == '6':
            search_by_position(df)
        else:
            print('\n[X] Pilihan tidak valid! Masukkan angka 1-6, atau 0.')
        
        input('\nTekan Enter untuk melanjutkan...')

if __name__ == '__main__':
    main()

