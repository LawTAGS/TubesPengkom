nama_tanpa_list = "bacAda"
nama = list(nama_tanpa_list)
indeks_huruf = [0 for i in range(len(nama))]

for i in range(len(nama)):
    indeks_huruf[i] = ord(nama[i])
    if 65 <= indeks_huruf[i] <= 90:
        indeks_huruf[i] += 32

for i in range(len(nama)):
    for j in range(1, len(nama)):
        if indeks_huruf[j-1] > indeks_huruf[j]:
            nama[j-1], nama[j] = nama[j], nama[j-1]
            indeks_huruf[j-1], indeks_huruf[j] = indeks_huruf[j], indeks_huruf[j-1]

for i in range(len(nama)):
    print(nama[i], end="")
