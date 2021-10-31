#Judul
#Aplikasi Peduli Lindungi

#TODO:
# 1. Buat sistem login/logout
# 2. Check-in/check-out
# 3. Izin keluar

#Kamus


# --------------------------------------- SUBPROGRAM ------------------------------------------------------------------------- #
# ---------------------------------- PENDEFINISIAN FUNGSI -------------------------------------------------------------------- #

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

# Test searching
# def searchingData(keyword, nameArray, searchCode):
#     keyFound = False
#     for i in range(len(nameArray)):
#         arrNama = nameArray
#         correctCount =  0
#         for chrKeyword in keyword:
#             for chrName in arrNama[i][searchCode]:
#                 if chrKeyword.upper() == chrName.upper():
#                     arrNama[i][searchCode] = arrNama[i][searchCode].replace(chrKeyword, '')
#                     correctCount += 1
#                     print(arrNama[i])

#             if correctCount == len(keyword):
#                 print(nameArray[i])
#                 keyFound = True
#                 break
        
#     return keyFound

import os
clear = lambda: os.system('cls')

def searchingData(keyword, arrData, searchCode):
    data_ketemu = False
    i = 1
    data_found = []
    print('Berikut adalah data yang dapat kami temukan:\n')
    for data in arrData:
        if data[5] == no_kk_user:
            if keyword in data[searchCode]:
                data_ketemu = True
                data_found.append(arrData.index(data))
                print('%d. %s' % (i, data[searchCode]))
                i += 1
            else:
                pass
        else:
            pass
    if not data_ketemu:
        print("Data tidak ditemukan.")
        return False
    else:
        return data_found

def login(username_user, password_user, user_lists):
    username_salah = True
    password_salah = True
    for [username, password] in user_lists:
        if username_user == username and password_user == password:
            return True
        elif username_user == username and password_user != password:
            username_salah = False
    if username_salah:
        print("Username yang anda masukkan salah.")
        return False
    else:
        print("Password yang anda masukkan salah.")
        return False

def daftar(user_lists):
    clear()
    username_user = input("Masukkan username yang anda inginkan: ")
    password_user = input("Masukkan password yang anda inginkan: ")
    clear()
    user_lists = append(user_lists, [username_user, password_user])

    no_kk = input("\nMasukkan nomor kartu keluarga anda: ")
    nik = input("\nMasukkan nomor induk kependudukan anda: ")
    nama = input("\nMasukkan nama: ")
    nim = input("Masukkan NIM: ")
    status = int(input("\nKeterangan: \n0: Belum vaksin \n1: vaksin pertama \n2: vaksin kedua \nMasukkan status vaksin: "))
    riwayat_check_in = []

    if status != 0:
        tglVaksin = []

        for dosis_vaksin in range(status):
            # tglVaksin += input("Masukkan tanggal vaksin: ") + " "
            tglVaksin = append(tglVaksin, input("Masukkan tanggal vaksin: "))

    else:
        tglVaksin = []

    return [user_lists, [nama, nim, tglVaksin, riwayat_check_in, nik, no_kk, username_user]]

def adaData(arrData):
    return True if length(arrData) != 0 else False

def outputData(data):
    print("\nNama:", str(data[0]) + '\n')
    print("NIM:", str(data[1]) + '\n')
    print("NIK:", str(data[4]) + '\n')
    if length(data[2]) == 0:
        print("Status vaksinasi: Belum vaksinasi\n")
    elif length(data[2]) == 1:
        print("Status vaksinasi:\nDosis 1: Tanggal %s\n" % (data[2][0]))
    else:
        print("Status vaksinasi:\nDosis 1: Tanggal %s\nDosis 2: Tanggal %s\n" % (data[2][0], data[2][1]))
    # elif data[2] == 1:
    #     print("Status vaksinasi: Sudah mendapatkan suntik dosis 1 pada tanggal %s" % (data[2]))
    if length(data[3]) == 0:
        print("Riwayat check-in: Belum ada riwayat check-in")
    else:
        print("Riwayat check-in: ")
        for index in range(length(data[3])):
                print('%d. Check-in ke-%d' % (index + 1, index + 1))
                print('- Lokasi kunjungan: %s' % (data[3][index][0]))
                print('- Tanggal berkunjung: %s' % (data[3][index][1]))
                print('- Waktu check-in: %s' % (data[3][index][2]))
                print('- Waktu check-out: %s\n' % (data[3][index][3]))

# ---------------------------------------- ALGORITMA UTAMA ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

program_berjalan = True
arrData = []
login_status = False
user_lists = [['admin', 'admin']] # [[username, password]] default nya adalah admin

while (program_berjalan == True):

# ----------------------------------------- TAMPILAN LOGIN ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
    clear()
    print("===============================================\n   Selamat datang di aplikasi PeduliLindungi  \n===============================================")

    while login_status == False:
        opsiLogin = input("Apakah anda sudah memiliki akun? (y/n)\n")
        if startswith(opsiLogin, 'y'):
            clear()
            username = input("Masukkan username anda: ")
            password = input("Masukkan password anda: ")
            if username == 'admin' and password == 'admin':
                admin_status = True
            else:
                admin_status = False
            login_status = login(username, password, user_lists)
            if login_status == True:
                if admin_status == False:
                    for index in range(length(arrData)):
                        if arrData[index][-1] == username:
                            no_kk_user = arrData[index][5]
                            username_user = username
                            clear()
        elif startswith(opsiLogin, 'n'):
            clear()
            prompt = input("Apakah anda ingin mendaftar? (y/n)\n")
            if startswith(prompt, 'y'):
                data_daftar = daftar(user_lists)
                user_lists = data_daftar[0]
                arrData = append(arrData, data_daftar[1])

                clear()
                print("Akun anda berhasil di daftarkan. Silahkan login menggunakan akun yang telah anda daftarkan.")
            # print(user_lists, arrData) # debugging

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

# --------------------------------------- MENU UTAMA ------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

    while login_status == True:

# --------------------------------------- TAMPILAN MENU ADMIN ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #
        if admin_status == True:
            clear()
            opsiMenu = int(input("Menu: \n1. Mengecek data \n2. Logout \n3. Keluar dari program \nMasukkan pilihan: "))

            # if (opsiMenu == 1):
            #     jumlah_data = int(input("\nJumlah data yang akan dimasukkan: "))

            #     # for i in range(n):
            #     #     arrData += [['*' for j in range(4)]]

            #     for data_ke in range(jumlah_data):
            #         nama = input("\nMasukkan nama: ")
            #         nim = input("Masukkan NIM: ")
            #         status = int(input("\nKeterangan: \n0: Belum vaksin \n1: vaksin pertama \n2: vaksin kedua \nMasukkan status vaksin: "))
            #         riwayat_check_in = "Belum ada riwayat check-in."

            #         if status != 0:
            #             tglVaksin = []

            #             for dosis_vaksin in range(status):
            #                 # tglVaksin += input("Masukkan tanggal vaksin: ") + " "
            #                 tglVaksin = append(tglVaksin, input("Masukkan tanggal vaksin: "))

            #         else:
            #             tglVaksin = []

            #         arrData = append(arrData, [nama, nim, tglVaksin, riwayat_check_in])

            # print(arrData) # debugging

            if (opsiMenu == 1):
                clear()
                if length(arrData) == 0:
                    print("Belum ada data yang terdaftar.")
                else:
                    for data in arrData:
                        outputData(data)
                        print('===============================================')
                input("Tekan sembarang tombol untuk melanjutkan.")

            if (opsiMenu == 2):
                clear()
                prompt = input("Anda yakin ingin logout dari akun anda?\n")
                if startswith(prompt, 'y'):
                    admin_status = False
                    login_status = False

            if (opsiMenu == 3):
                clear()
                prompt = input("Anda yakin ingin keluar dari program ini?\n")
                if startswith(prompt, 'y'):
                    program_berjalan = False
                    admin_status = False
                    login_status = False
                else:
                    program_berjalan = True

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

# ---------------------------------------------- TAMPILAN MENU SELAIN ADMIN -------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

        else:
            clear()
            opsiMenu = int(input("Menu: \n1. Mendaftarkan data \n2. Data keluarga \n3. Check-in \n4. Logout \n5. Keluar dari program \nMasukkan pilihan: "))

            if (opsiMenu == 1):
                clear()
                jumlah_data = int(input("\nJumlah data yang akan dimasukkan: "))

                # for i in range(n):
                #     arrData += [['*' for j in range(4)]]

                for data_ke in range(jumlah_data):
                    clear()
                    nama = input("\nMasukkan nama: ")
                    nim = input("Masukkan NIM: ")
                    status = int(input("\nKeterangan: \n0: Belum vaksin \n1: vaksin pertama \n2: vaksin kedua \nMasukkan status vaksin: "))
                    nik = input("\nMasukkan nomor induk kependudukan anda: ")
                    no_kk = no_kk_user
                    riwayat_check_in = []

                    if status != 0:
                        tglVaksin = []

                        for dosis_vaksin in range(status):
                            # tglVaksin += input("Masukkan tanggal vaksin: ") + " "
                            tglVaksin = append(tglVaksin, input("Masukkan tanggal vaksin: "))

                    else:
                        tglVaksin = []

                    arrData = append(arrData, [nama, nim, tglVaksin, riwayat_check_in, nik, no_kk, username_user])
                    clear()
                    print("Data berhasil ditambahkan.")
                    input("Tekan sembarang tombol untuk melanjutkan.")

            # print(arrData) # debugging

            if (opsiMenu == 2):
                clear()
                if adaData(arrData):
                    jenis_data_yang_dicari = input("\nPencarian dapat dilakukan berdasarkan: \n1. Nama \n2. NIM \n3. Tampilkan semua \nPilihan menu: ")
                    if startswith(jenis_data_yang_dicari, '1'):
                        # data_ketemu = False
                        clear()
                        data_yang_dicari = input("\nMasukkan nama yang ingin dicari: ")
                        # for data_pengguna in arrData:
                        #     if data_pengguna[0] == data_yang_dicari and data_pengguna[5] == no_kk_user:
                        #         data_ketemu = True
                        #         outputData(data_pengguna)
                        #         print('===============================================')
                        #         input("Tekan sembarang tombol untuk melanjutkan.")
                        # if data_ketemu == False:
                        #     print("Data tidak ditemukan.")

                        clear()
                        data_found = searchingData(data_yang_dicari, arrData, searchCode = 0)
                        # kodePencariannya yang 1. Nama, 2. NIM, jadi kalau dipilih 1 ak cukup ngecek dari indeks ke 0 aja
                        # if hasil:
                        #     hasil

                        pilihanUser = int(input("Data mana yang ingin anda cari (masukkan angka): "))
                        clear()
                        outputData(arrData[data_found[pilihanUser - 1]])
                        input("Tekan sembarang tombol untuk melanjutkan.")

                        # elif not hasil:
                        #     print("Data tidak ditemukan.")

                    elif startswith(jenis_data_yang_dicari, '2'):
                        clear()
                        data_yang_dicari = input("\nMasukkan NIM yang ingin dicari: ")
                        # for data_pengguna in arrData:
                        #     if data_pengguna[1] == data_yang_dicari and data_pengguna[5] == no_kk_user:
                        #         data_ketemu = True
                        #         outputData(data_pengguna)
                        #         print('===============================================')
                        #         input("Tekan sembarang tombol untuk melanjutkan.")
                        #     else:
                        #         pass
                        # if data_ketemu == False:
                        #     print("\nData tidak ditemukan.\n")

                        clear()
                        data_found = searchingData(data_yang_dicari, arrData, searchCode = 1)
                        # hasil = searchingData(data_yang_dicari, arrData, searchCode = 1)
                        
                        # if hasil:
                        #     hasil

                        pilihanUser = int(input("Data mana yang ingin anda cari (masukkan angka): "))
                        clear()
                        outputData(arrData[data_found[pilihanUser - 1]])
                        input("Tekan sembarang tombol untuk melanjutkan.")

                        # elif not hasil:
                        #     print("Data tidak ditemukan.")

                    elif startswith(jenis_data_yang_dicari, '3'):
                        clear()
                        data_ketemu = False
                        for data_pengguna in arrData:
                            if data_pengguna[5] == no_kk_user:
                                outputData(data_pengguna)
                                print('===============================================')
                                input("Tekan sembarang tombol untuk melanjutkan.")

                else:
                    print("\nBelum ada data yang terdaftar.\n")
                    input("Tekan sembarang tombol untuk melanjutkan.")

            if (opsiMenu == 3):
                clear()
                if adaData(arrData):
                    i = 1
                    available_names = []
                    print("\nSiapa yang akan check-in?\n")
                    for index in range(length(arrData)):
                        if arrData[index][5] == no_kk_user:
                            available_names.append([arrData[index], index])
                            print('%d. %s' % (i, arrData[index][0]))
                    
                    valid_choice = False
                    while not valid_choice:
                        pilihanUser = int(input("Masukkan pilihan anda (berupa angka): "))
                        if pilihanUser in [i for i in range(1, len(available_names) + 1)]:
                            valid_choice = True
                        else:
                            pass

                    clear()
                    lokasi_kunjungan = input("Masukkan lokasi kunjungan anda: ")
                    tanggal_kunjungan = input("Masukkan tanggal berkunjung: ")
                    waktu_check_in = input("Masukkan waktu check-in: ")
                    waktu_check_out = input("Masukkan waktu check-out: ")
                    arrData[available_names[pilihanUser - 1][1]][3] = append(arrData[available_names[pilihanUser - 1][1]][3], [lokasi_kunjungan, tanggal_kunjungan, waktu_check_in, waktu_check_out])
                    clear()
                    print("Proses check-in berhasil.")
                    input("Tekan sembarang tombol untuk melanjutkan.")
                else:
                    print("\nBelum ada data yang terdaftar.\n")

            if (opsiMenu == 4):
                clear()
                prompt = input("Anda yakin ingin logout dari akun anda?\n")
                if startswith(prompt, 'y'):
                    login_status = False

            if (opsiMenu == 5):
                clear()
                prompt = input("Anda yakin ingin keluar dari program ini?\n")
                if startswith(prompt, 'y'):
                    program_berjalan = False
                    login_status = False
                else:
                    program_berjalan = True

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------- SESAAT SEBELUM KELUAR ---------------------------------------------------------- #
# ----------------------------------------------- DARI PROGRAM --------------------------------------------------------------- #

clear()
print("Terima kasih!")
input("Tekan sembarang tombol untuk keluar dari program.")

# ---------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------- #