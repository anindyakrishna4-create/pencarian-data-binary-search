# File: binary_search.py (Logika Algoritma)

# List global untuk menyimpan riwayat langkah
HISTORY = []

def binary_search(data_list, target):
    """
    Mengimplementasikan Binary Search dan mencatat setiap langkah di HISTORY.
    Mengembalikan index jika ditemukan, atau -1 jika tidak ditemukan.
    """
    global HISTORY
    HISTORY = []
    
    # Prasyarat: Array harus terurut! Kita asumsikan array input sudah terurut.
    arr = sorted(data_list[:]) 
    n = len(arr)
    low = 0
    high = n - 1
    found_index = -1
    
    # Catat status awal
    HISTORY.append({
        'array': arr[:],
        'target': target,
        'low': low, 
        'high': high,
        'mid': -1, # Belum ada mid
        'status': 'Mulai',
        'action': f'Memulai pencarian untuk nilai {target}. Array harus TERURUT.'
    })

    while low <= high:
        # Hitung indeks tengah (mid)
        mid = (low + high) // 2
        
        # Catat langkah pengecekan
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'low': low, 
            'high': high,
            'mid': mid,
            'status': 'Mengecek',
            'action': f'Mengecek Indeks Tengah (mid={mid}). Nilai: {arr[mid]}. Rentang: [{low} - {high}]'
        })
        
        if arr[mid] == target:
            found_index = mid
            # Catat langkah Ditemukan
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'mid': mid,
                'status': 'Ditemukan',
                'action': f'Nilai {target} DITEMUKAN pada Indeks {mid}!'
            })
            break
            
        elif arr[mid] < target:
            # Target ada di sebelah kanan, buang sebelah kiri (low = mid + 1)
            low = mid + 1
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'mid': mid,
                'status': 'Pindah Kanan',
                'action': f'Nilai terlalu kecil. Pindahkan batas Bawah (low) ke {low}.'
            })
            
        else: # arr[mid] > target
            # Target ada di sebelah kiri, buang sebelah kanan (high = mid - 1)
            high = mid - 1
            HISTORY.append({
                'array': arr[:],
                'target': target,
                'low': low, 
                'high': high,
                'mid': mid,
                'status': 'Pindah Kiri',
                'action': f'Nilai terlalu besar. Pindahkan batas Atas (high) ke {high}.'
            })

    # Catat status selesai (HANYA jika loop berakhir)
    if found_index == -1:
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'low': low, 
            'high': high,
            'mid': -1,
            'status': 'Selesai',
            'action': f'Selesai. Rentang pencarian kosong (low > high). Nilai {target} tidak ditemukan.'
        })
        
    return found_index, HISTORY
