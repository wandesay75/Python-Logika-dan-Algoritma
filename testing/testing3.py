Jam_Billing = int(input("Masukan jam billing : "))
Jam_Pertama = 6000
Jam_Berikutnya = 5000
if Jam_Billing <= 3:
    Tarif = Jam_Pertama*Jam_Billing
    print("Untuk tarif 3 jam pertama maka dikenakan biaya sebesar", Tarif)
else:
    Tarif = Jam_Berikutnya*Jam_Billing
    print("Untuk tarif 3 jam berikutnya maka dikenakan biaya sebesar", Tarif)