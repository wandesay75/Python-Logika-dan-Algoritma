N = int(input("Masukan bilangan N: "))
karakter = input("Masukan karakter: ")
1<=N<=100
for i in range(int(N)):
    for j in range(0, 10-i):
        print("", end=" ")
    for k in range (0, 1 * i + 1):
        print(karakter, end=" ")
    print()