#Judul
#Aplikasi Peduli Lindungi

#Kamus


#Subprogram
from fungsi_dasar import * # Import fungsi dasar buatan sendiri, dari file fungsi_dasar.py

# def tambahData(arrData, nama, nim, status, tglVaksin):
#     arrData = append(arrData, [nama, nim, status, tglVaksin])
#     return arrData

# def tambahData(arrData, index, nama, nim, status, tglVaksin):
#     arrData[index][0] = nama
#     arrData[index][1] = nim
#     arrData[index][2] = str(status)
#     arrData[index][3] = tglVaksin

#     return arrData

def adaData(arrData):
    return True if length(arrData) != 0 else False

def outputData(data):
    print("\nNama:", str(data[0]) + '\n')
    print("NIM:", str(data[1]) + '\n')
    if length(data[2]) == 0:
        print("Status vaksinasi: Belum vaksinasi\n")
    elif length(data[2]) == 1:
        print("Status vaksinasi:\nDosis 1: Tanggal %s\n" % (data[2][0]))
    else:
        print("Status vaksinasi:\nDosis 1: Tanggal %s\nDosis 2: Tanggal %s\n" % (data[2][0], data[2][1]))
    # elif data[2] == 1:
    #     print("Status vaksinasi: Sudah mendapatkan suntik dosis 1 pada tanggal %s" % (data[2]))
    print("Riwayat check-in:", str(data[3]) + '\n')

#Algoritma
program_berjalan = True
jmlhData = 0
arrData = []

while (program_berjalan == True):
    print("===============================================\n   Selamat datang di aplikasi PeduliLindungi  \n===============================================")

    opsiMenu = int(input("Menu: \n1. Mendaftarkan data \n2. Mengecek data \n3. Check-in \n4. Keluar \nMasukkan pilihan: "))

    if (opsiMenu == 1):
        n = int(input("\nJumlah data yang akan dimasukkan: "))

        # for i in range(n):
        #     arrData += [['*' for j in range(4)]]

        for i in range(n):
            nama = input("\nMasukkan nama: ")
            nim = input("Masukkan NIM: ")
            status = int(input("\nKeterangan: \n0: Belum vaksin \n1: vaksin pertama \n2: vaksin kedua \nMasukkan status vaksin: "))
            riwayat_check_in = "Belum ada riwayat check-in."

            if status != 0:
                tglVaksin = []

                for j in range(status):
                    # tglVaksin += input("Masukkan tanggal vaksin: ") + " "
                    tglVaksin = append(tglVaksin, input("Masukkan tanggal vaksin: "))

            else:
                tglVaksin = []

            arrData = append(arrData, [nama, nim, tglVaksin, riwayat_check_in])

    print(arrData) # debugging

    if (opsiMenu == 2):
        if adaData(arrData):
            jenis_data_yang_dicari = input("\nData yang tersedia\n1. Nama \n2. NIM \nJenis data apa yang ingin anda cari? ").lower().replace(' ', '')
            if jenis_data_yang_dicari.startswith('1'):
                data_ketemu = False
                data_yang_dicari = input("\nMasukkan nama yang ingin dicari: ")
                for data_pengguna in arrData:
                    if data_pengguna[0] == data_yang_dicari:
                        data_ketemu = True
                        outputData(data_pengguna)
                        input("Tekan sembarang tombol untuk melanjutkan.")
                    else:
                        pass
                if data_ketemu == False:
                    print("Data tidak ditemukan.")

            elif jenis_data_yang_dicari.startswith('2'):
                data_ketemu = False
                data_yang_dicari = input("\nMasukkan NIM yang ingin dicari: ")
                for data_pengguna in arrData:
                    if data_pengguna[1] == data_yang_dicari:
                        data_ketemu = True
                        outputData(data_pengguna)
                        input("Tekan sembarang tombol untuk melanjutkan.")
                    else:
                        pass
                if data_ketemu == False:
                    print("\nData tidak ditemukan.\n")

        else:
            print("\nBelum ada data yang terdaftar.\n")

    if (opsiMenu == 3):
        if adaData(arrData):
            pass
        else:
            print("\nBelum ada data yang terdaftar.\n")

    if (opsiMenu == 4):
        prompt = input("Anda yakin ingin keluar dari program ini?\n")
        if prompt.startswith('y'):
            program_berjalan = False
        else:
            program_berjalan = True

# Sesaat sebelum keluar program
print("Terima kasih!")
input("Tekan sembarang tombol untuk keluar dari program.")