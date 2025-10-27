"""
Analisis Top 10 Pemain dengan Passing Tertinggi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Fix encoding untuk Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def analyze_top_passers():
    """
    Analisis top 10 pemain dengan passing tertinggi
    """
    print("="*60)
    print("TOP 10 PEMAIN DENGAN PASSING TERTINGGI")
    print("="*60)
    
    try:
        # Load data
        df = pd.read_csv('fifa_players.csv', low_memory=False)
        print(f"\n[OK] Data berhasil dimuat: {len(df)} pemain\n")
        
        # Analisis passing
        if 'passing' in df.columns:
            # Ambil top 10 pemain dengan passing tertinggi
            top_passers = df.nlargest(10, 'passing')
            
            # Pilih kolom yang relevan
            result = top_passers[['short_name', 'club_name', 'nationality_name', 'passing', 'overall', 'age']]
            
            print("Rank | Nama Pemain           | Klub                    | Negara      | Passing | Overall | Umur")
            print("-" * 100)
            
            for idx, (_, row) in enumerate(result.iterrows(), 1):
                name = row['short_name'][:20] if len(row['short_name']) > 20 else row['short_name']
                club = row['club_name'][:20] if len(str(row['club_name'])) > 20 else row['club_name']
                nation = row['nationality_name'][:11] if len(str(row['nationality_name'])) > 11 else row['nationality_name']
                
                print(f"{idx:2d}.  | {name:20s} | {club:20s} | {nation:11s} | {row['passing']:7.0f} | {row['overall']:7.0f} | {row['age']:4.0f}")
            
            print("\n" + "="*60)
            print("DETAIL PEMAIN")
            print("="*60)
            
            for idx, (_, row) in enumerate(result.iterrows(), 1):
                print(f"\n{idx}. {row['short_name']}")
                print(f"   Klub: {row['club_name']}")
                print(f"   Negara: {row['nationality_name']}")
                print(f"   Passing: {row['passing']}")
                print(f"   Overall Rating: {row['overall']}")
                print(f"   Umur: {int(row['age'])} tahun")
            
            # Visualisasi
            print("\n[INFO] Membuat visualisasi...")
            
            plt.figure(figsize=(14, 10))
            
            # Subplot 1: Bar chart passing
            plt.subplot(2, 1, 1)
            colors = plt.cm.viridis(range(len(result)))
            bars = plt.barh(range(len(result)), result['passing'], color=colors)
            plt.yticks(range(len(result)), result['short_name'])
            plt.xlabel('Passing Rating', fontsize=12, fontweight='bold')
            plt.title('Top 10 Pemain dengan Passing Tertinggi', fontsize=14, fontweight='bold')
            plt.gca().invert_yaxis()
            plt.grid(axis='x', alpha=0.3)
            
            # Tambahkan nilai di setiap bar
            for i, (idx, row) in enumerate(result.iterrows()):
                plt.text(row['passing'] + 0.5, i, f"{row['passing']:.0f}", 
                        va='center', fontweight='bold')
            
            # Subplot 2: Overall rating comparison
            plt.subplot(2, 1, 2)
            x = range(len(result))
            width = 0.35
            plt.bar([i - width/2 for i in x], result['passing'], width, label='Passing', color='steelblue')
            plt.bar([i + width/2 for i in x], result['overall'], width, label='Overall Rating', color='coral')
            plt.xlabel('Pemain')
            plt.ylabel('Rating')
            plt.title('Perbandingan Passing vs Overall Rating')
            plt.xticks(x, result['short_name'], rotation=45, ha='right')
            plt.legend()
            plt.grid(axis='y', alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('top_10_passers.png', dpi=300, bbox_inches='tight')
            print("[OK] Visualisasi disimpan sebagai 'top_10_passers.png'")
            plt.show()
            
            # Simpan ke CSV
            result.to_csv('top_10_passers.csv', index=False)
            print("[OK] Data disimpan sebagai 'top_10_passers.csv'")
            
        else:
            print("[ERROR] Kolom 'passing' tidak ditemukan dalam dataset")
            
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    analyze_top_passers()

