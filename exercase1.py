data = []
def insert():

    nama = input('nama barang = ')
    stok = int(input('stok barang = '))
    data_baru = {'nama' : nama,'stok' : stok}
    data.append(data_baru)

def view_data():
    for i in data:
        print('-',i['nama'],i['stok'])
def hapus_data():
    id = int(input('masukkan data yang keberapa : '))
    del data[id]
    print('hapus data berhasil')