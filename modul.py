def tampilan():
    print ('-----selamat datang di program manajemen stok barang-----'.upper())
    print('='*25)
    print('Pilihan : ')
    print ('1. Tambah Data Barang')
    print ('2. Edit Barang')
    print ('3. Hapus Data Barang')
    print ('4. Cari Data Barang')
    print ('5. Tampilkan Data Barang')
    print ('6. Tampilkan Jumlah Barang')
    print ('7. Keluar')
    print('='*25)

barang_dic = []

def insert():
    nama = str(input('Masukan Nama Barang : '))
    stok = int(input('Masukan Stok Barang : '))
    data_baru = {'nama barang':nama,'stok':stok}
    barang_dic.append(data_baru)

def delete():
    hapus = int(input('Hapus Data Index Ke - : '))
    del barang_dic[hapus]

def display():
    if len(barang_dic)==0:
        print('\n')
        print('='*25)
        print('---DATA BARANG KOSONG---')
        print('='*25)
        print('\n')
    else:
        print('\n')
        print('='*25)
        print('data barang elektronik'.upper())
        for barang in barang_dic:
            print(barang['nama barang'],', stok :',barang['stok'],'Buah')
        print('='*25)
        print('\n')

def total():
    print('\n')
    print('='*25)
    print('Total Barang Yang Tersimpan :',len(barang_dic))
    print('='*25)
    print('\n')

def search():
    cari = str(input('Cari Barang : ')).lower()
    print('\n')
    print('=== Hasil Pencarian ==='.upper())
    print('='*23)
    found = False

    for barang in barang_dic:
        if cari.lower() in barang['nama barang'.lower()]:
            print(barang['nama barang'],', Stok Barang :', barang['stok'])
            found = True

    if not found:
        print('---DATA BARANG TIDAK DITEMUKAN---')
    print('='*23)
    print('\n')


def edit():
    deleteIndex = int(input('Hapus Data Index Ke - : '))
    del barang_dic[deleteIndex]
    nama = str(input('Masukan Nama Barang : '))
    stok = int(input('Masukan Stok Barang : '))
    data_baru = {'nama barang':nama,'stok':stok}
    barang_dic.insert(deleteIndex,data_baru)

def end():
    print('\n')
    print('='*25)
    print('Terimakasih Telah Mencoba')
    print('='*25)
    print('\n')


# def validasi():