import exercase1 as np


while True :
    print('selamat datang di sini')
    print('pilihan')
    print('1. tambah data barang')
    print('2. hapus data barang')
    print('3. tampilkan data barang')
    print('4. keluar')
    pilihan = int(input('masukkan pilihan :'))
    if pilihan == 1:
        np.insert()
    elif pilihan == 2:
        np.hapus_data()
    elif pilihan == 3:
        np.view_data()
    elif pilihan == 4:
        break