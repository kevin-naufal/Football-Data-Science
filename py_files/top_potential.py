"""
Analisis Top 10 Pemain dengan Potensi Tertinggi
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

def analyze_top_potential():
    """
    Analisis top 10 pemain dengan potensi tertinggi
    """
    print("="*60)
    print("TOP 10 PEMAIN DENGAN POTENSI TERTINGGI")
    print("="*60)
    
    try:
        # Load data
        df = pd.read_csv('fifa_players.csv', low_memory=False)
        print(f"\n[OK] Data berhasil dimuat: {len(df)} pemain\n")
        
        # Analisis potensi
        if 'potential' in df.columns:
            # Ambil top 10 pemain dengan potential tertinggi
            top_potential = df.nlargest(10, 'potential')
            
            # Pilih kolom yang relevan
            result = top_potential[['short_name', 'club_name', 'nationality_name', 'potential', 'overall', 'age']]
            
            print("Rank | Nama Pemain           | Klub                    | Negara      | Potential | Overall | Umur")
            print("-" * 105)
            
            for idx, (_, row) in enumerate(result.iterrows(), 1):
                name = row['short_name'][:20] if len(row['short_name']) > 20 else row['short_name']
                club = row['club_name'][:20] if len(str(row['club_name'])) > 20 else row['club_name']
                nation = row['nationality_name'][:11] if len(str(row['nationality_name'])) > 11 else row['nationality_name']
                
                print(f"{idx:2d}.  | {name:20s} | {club:20s} | {nation:11s} | {row['potential']:9.0f} | {row['overall']:7.0f} | {row['age']:4.0f}")
            
            print("\n" + "="*60)
            print("DETAIL PEMAIN")
            print("="*60)
            
            for idx, (_, row) in enumerate(result.iterrows(), 1):
                print(f"\n{idx}. {row['short_name']}")
                print(f"   Klub: {row['club_name']}")
                print(f"   Negara: {row['nationality_name']}")
                print(f"   Potential: {row['potential']}")
                print(f"   Overall Rating: {row['overall']}")
                print(f"   Umur: {int(row['age'])} tahun")
            
            # Visualisasi
            print("\n[INFO] Membuat visualisasi...")
            
            fig, axes = plt.subplots(2, 1, figsize=(14, 12))
            
            # Subplot 1: Bar chart potential
            ax1 = axes[0]
            colors = plt.cm.plasma(range(len(result)))
            bars = ax1.barh(range(len(result)), result['potential'], color=colors)
            ax1.set_yticks(range(len(result)))
            ax1.set_yticklabels(result['short_name'])
            ax1.set_xlabel('Potential Rating', fontsize=12, fontweight='bold')
            ax1.set_title('Top 10 Pemain dengan Potensi Tertinggi', fontsize=14, fontweight='bold')
            ax1.invert_yaxis()
            ax1.grid(axis='x', alpha=0.3)
            
            # Tambahkan nilai di setiap bar
            for i, (idx, row) in enumerate(result.iterrows()):
                ax1.text(row['potential'] + 0.5, i, f"{row['potential']:.0f}", 
                        va='center', fontweight='bold')
            
            # Subplot 2: Perbandingan Potential vs Overall Rating
            ax2 = axes[1]
            x = range(len(result))
            width = 0.35
            ax2.bar([i - width/2 for i in x], result['potential'], width, 
                   label='Potential', color='mediumpurple')
            ax2.bar([i + width/2 for i in x], result['overall'], width, 
                   label='Overall Rating', color='orange')
            ax2.set_xlabel('Pemain')
            ax2.set_ylabel('Rating')
            ax2.set_title('Perbandingan Potential vs Overall Rating', fontweight='bold')
            ax2.set_xticks(x)
            ax2.set_xticklabels(result['short_name'], rotation=45, ha='right')
            ax2.legend()
            ax2.grid(axis='y', alpha=0.3)
            
            plt.tight_layout()
            plt.savefig('top_10_potential.png', dpi=300, bbox_inches='tight')
            print("[OK] Visualisasi disimpan sebagai 'top_10_potential.png'")
            plt.show()
            
            # Simpan ke CSV
            result.to_csv('top_10_potential.csv', index=False)
            print("[OK] Data disimpan sebagai 'top_10_potential.csv'")
            
            # Analisis tambahan
            print("\n" + "="*60)
            print("ANALISIS TAMBAHAN")
            print("="*60)
            
            gap = result['potential'] - result['overall']
            print(f"\nPemain dengan Gap Potential vs Overall Terbesar (Prospek Tinggi):")
            result_with_gap = result.copy()
            result_with_gap['gap'] = gap
            
            # Sort by gap
            top_gap = result_with_gap.nlargest(5, 'gap')
            print("\nPemain dengan potensi belum maksimal:")
            for idx, (_, row) in enumerate(top_gap.iterrows(), 1):
                print(f"{idx}. {row['short_name']} - Gap: {row['gap']:.0f} point")
            
        else:
            print("[ERROR] Kolom 'potential' tidak ditemukan dalam dataset")
            
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    analyze_top_potential()

