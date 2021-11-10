matriks1 = [
    [2, 3, 4],
    [3, 2, 4],
    [4, 3, 2]
]
matriks2 = [
    [3, 2, 4],
    [4, 2, 3],
    [5, 3, 2]
]
#penjumlahan

hasil= []
for i in range(len(matriks1)):
    baris = []
    for j in range(len(matriks1[i])):
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)

print("Hasil Penjumlahan kedua matriks adalah : ")
for baris in hasil:
    print(baris)