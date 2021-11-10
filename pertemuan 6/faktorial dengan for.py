def faktorial (n):
    if n <= 1:
        return (n)
    else:
        return (n * faktorial (n-1))

n = int(input('Masukkan nilai n: '))
faktorial = 1

for a in range(1, n + 1):
  faktorial *= a

print(f'{n}! = {faktorial}')