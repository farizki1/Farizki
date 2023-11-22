

daftar_nilai = {'005': {'nim':'005','nama':'Farizki','tugas1':90.0,'tugas2':90.0,'uts':90.0,'uas':80.0,'nilaiAkhir':87.5},
                '002': {'nim':'002','nama':'Fariz','tugas1':80.0,'tugas2':80.0,'uts':80.0,'uas':80.0,'nilaiAkhir':80.00}}


def menu():
    global inputMenu
    print('''SELAMAT DATANG DI PROGRAM INPUT NILAI MAHASISWA
    MATA KULIAH DATA SCIENCE PURWADHIKA
    Pilih Menu berikut:
    1. Input data Nilai Mahasiswa
    2. Menampilkan Data Nilai
    3. Update Data Nilai
    4. Hapus Data Nilai
    5. Search Data Nilai
    6. Keluar''')
    inputMenu = int(input("Pilih Menu untuk : "))
    return inputMenu

def view_nilai(dataNilai):
    print('\nDaftar Nilai Mata Kuliah Data Science Purwadhika ')
    print('No.\t NIM\t Nama\t\t Tugas1\t Tugas2\t UTS\t UAS\t Nilai')

    for i in range(len(dataNilai)): #memeriksa jumlah item
        print('{}\t {}\t {}  \t {}  \t {} \t {}\t {} \t {}'.format(i+1, dataNilai[i]['nim'], dataNilai[i]['nama'], dataNilai[i]['tugas1'], dataNilai[i]['tugas2'], dataNilai[i]['uts'], dataNilai[i]['uas'], dataNilai[i]['nilaiAkhir']))


def read_nilai(userInput):
    while True:
        
        print(''' Pilih Menu berikut:
            1. Tampilkan semua data Nilai
            2. Tampilkan data Nilai dengan NIM  
            3. Kembali ke Menu''')        
        userInput = int(input("Silakan masukkan pilihan :"))

        if(userInput == 1):
            if(len(daftar_nilai) > 0):
                view_nilai(list(daftar_nilai.values()))
                break
            else:
                print('\nData Nilai masih kosong')
        elif(userInput == 2):
            if(len(daftar_nilai) > 0):
                cari_nim = str(input('\nMasukkan NIM: '))
                if (cari_nim in daftar_nilai):
                    view_nilai([daftar_nilai[cari_nim]])
                else:
                    print('\ndata Nilai tidak ditemukan')
            else:
                print('\ndata Nilai masih kosong')
        elif(userInput == 3):
            break

def create_nilai(userInput):
    while True:
        userInput = str(input('Ingin menambahkan data nilai Mahasiswa?(y/n) : '))
        if (userInput == 'y'):
            inputnim = str(input("Masukkan NIM : "))
            if (inputnim in daftar_nilai):
                print("NIM {} sudah ada".format(inputnim))
            else:
                inputnama = input("masukkan Nama : ").capitalize()
                inputtugas1 = float(input("masukkan nilai Tugas 1 : "))
                inputtugas2 = float(input("masukkan nilai Tugas 2 : "))
                inputUts = float(input ("masukkan nilai UTS : "))
                inputUas = float(input("masukkan nilai UAS : "))
                nilai_akhir = float(inputtugas1+inputtugas2+inputUts+inputUas)*25/100
                save = input("apakah input nilai ini ingin disimpan? y/n :")
                if (save == 'y'):
                    daftar_nilai.update({inputnim:{'nim':inputnim,'nama':inputnama,'tugas1':inputtugas1,'tugas2':inputtugas2,'uts':inputUts,'uas':inputUas,'nilaiAkhir':nilai_akhir}})
                    print("Data berhasil disimpan")

                else:
                    print('Data Belum Tersimpan')
                    create_nilai(daftar_nilai)
        elif(userInput == 'n'):
            break
        else:
            pass
        
def delete_nilai(userInput):
    while True:
        userInput = str(input('Ingin menghapus data nilai Mahasiswa?(y/n) : '))
        if (userInput == 'y'):
            inputnim = str(input("Masukkan NIM : "))
            if inputnim in daftar_nilai:
                view_nilai([daftar_nilai[inputnim]])
                hapus = str(input('Apakah anda ingin menghapus data nilai ini? (y/n) : '))
                if(hapus == 'y'):
                    del daftar_nilai[inputnim]
                    print('\nData Nilai Berhasil Dihapus')
                else:
                    print('\nData Belum Dihapus')
            else:
                print('\nTidak ada data nilai dengan NIM {}'.format(inputnim))
        elif(userInput == 'n'):
            break
        else:
            pass

def search_nilai(userInput):
    while True:
        userInput = str(input('Ingin Mencari data nilai Mahasiswa?(y/n) : '))
        if (userInput == 'y'):
            if(len(daftar_nilai) > 0):
                cari_nim = str(input('\nMasukkan NIM: '))
                if (cari_nim in daftar_nilai):
                    view_nilai([daftar_nilai[cari_nim]])
                else:
                    print('\ndata Nilai tidak ditemukan')
            else:
                print('\ndata Nilai masih kosong')
        elif(userInput == 'n'):
            break #berhenti paksa
        else:
            pass #tidak melakukan apapun

def update_nilai(userInput):
    while True:
        userInput = str(input('Ingin Mengupdate data nilai Mahasiswa?(y/n) : '))
        if (userInput == 'y'):
            inputnim = str(input("Masukkan NIM : "))
            if (inputnim in daftar_nilai):
                view_nilai([daftar_nilai[inputnim]])

                print(''' Pilih Menu berikut:
                1. Nilai Tugas 1
                2. Nilai Tugas 2  
                3. Nilai UTS
                4. Nilai UAS''') 
                jenisKolom = int(input("Input jenis kolom yang ingin di update : ")) 

    
                if(jenisKolom == 1):
                    updateNilai = float(input('\nMasukkan Nilai Tugas1: '))
                    save = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(save == 'y'):
                        daftar_nilai[inputnim]['tugas1'] = float(updateNilai)
                        print('\nData berhasil disimpan')
                    else:
                        print('\nData belum trsimpan')
                elif(jenisKolom == 2):
                    updateNilai = float(input('\nMasukkan Nilai Tugas2: '))
                    save = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(save == 'y'):
                        daftar_nilai[inputnim]['tugas2'] = float(updateNilai)
                        print('\nData berhasil disimpan')
                    else:
                        print('\nData belum tersimpan')                  
                elif(jenisKolom == 3):
                    updateNilai = float(input('\nMasukkan Nilai UTS: '))
                    save = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(save == 'y'):
                        daftar_nilai[inputnim]['uts'] = float(updateNilai)
                        print('\nData berhasil disimpan')
                    else:
                        print('\nData belum tersimpan')                  
                elif(jenisKolom == 4):
                    updateNilai = float(input('\nMasukkan Nilai UAS: '))
                    save = str(input('\nApakah anda ingin menyimpan data? (y/n) : '))
                    if(save == 'y'):
                        daftar_nilai[inputnim]['uas'] = float(updateNilai)
                        print('\nData berhasil disimpan')
                    else:
                        print('\nData belum tersimpan')
                
                else:
                    print('Pilih jenis kolom yang ingin diupdate')
            else:
                print('\nData nilai {} tidak ditemukan'.format(updateNilai))
        elif(userInput == 'n'):
            break
        else:
            pass



while True:
    inputMenu = menu()
    if(inputMenu == 1):
        create_nilai(daftar_nilai)
    elif(inputMenu == 2):
        read_nilai(daftar_nilai)
    elif(inputMenu == 3):
        update_nilai(daftar_nilai)
    elif(inputMenu == 4):
        delete_nilai(daftar_nilai)   
    elif(inputMenu == 5):
        search_nilai(daftar_nilai)
    elif(inputMenu == 6):
        exit()
    else:
        print('\Pilihan tidak vaid')


