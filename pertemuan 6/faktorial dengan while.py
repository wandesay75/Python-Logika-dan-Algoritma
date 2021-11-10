def faktorial(j):
    if j <= 1:
        return 1
    else:
        return (j * faktorial(j-1))

j = 0
x = int(input("Masukan Bilangan x : "))

while j <= x:
    print(f'{j}! =', faktorial(j))
    j+=1