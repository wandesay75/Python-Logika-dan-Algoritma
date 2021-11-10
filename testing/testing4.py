gaji_pokok = 5000000
produk_terjual = int(input("Produk yang terjual : "))
harga_satuan_produk = int(input("Masukan harga produk : "))
minimal_terjual = 100

if produk_terjual > minimal_terjual:
    bonus= 0.2*produk_terjual*harga_satuan_produk
else:
    bonus= 0.1*produk_terjual*harga_satuan_produk
gaji = bonus+gaji_pokok
print("Jadi, gaji salesman tersebut adalah", gaji)