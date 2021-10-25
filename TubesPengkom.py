#Judul
#Aplikasi Peduli Lindungi

#Kamus


#Subprogram
def Test(Object):
    print(Object)

    return

def tambahData(arrData, index, nama, nim, status, tglVaksin):
    arrData[index][0] = nama
    arrData[index][1] = nim
    arrData[index][2] = str(status)
    arrData[index][3] = tglVaksin

    return arrData

#Algoritma
print("=============================================== \n   Selamat datang di aplikasi PeduliLindungi  \n===============================================")

opsiMenu = int(input("Menu: \n1. Mendaftarkan data \n2. Mengecek data \nMasukkan pilihan: "))

jmlhData = 0
arrData = [['*' for j in range(4)]]

if(opsiMenu == 1):
    n = int(input("\nJumlah data yang akan dimasukkan: "))

    for i in range(n-1):
        arrData += [['*' for j in range(4)]]

    for i in range(n):
        nama = input("\nMasukkan nama: ")
        nim = input("Masukkan NIM: ")
        status = int(input("\nKeterangan: \n0: Belum vaksin \n1: vaksin pertama \n2: vaksin kedua \nMasukkan status vaksin: "))

        if status != 0:
            tglVaksin = ""

            for j in range(status):
                tglVaksin += input("Masukkan tanggal vaksin: ") + " "

        else:
            tglVaksin = "Belum vaksin"

        tambahData(arrData, jmlhData, nama, nim, status, tglVaksin)

        jmlhData += 1


print(arrData)