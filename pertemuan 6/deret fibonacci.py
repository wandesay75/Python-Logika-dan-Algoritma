def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

x = int(input("Masukan batas deret bilangan fibonacci : "))
print("Deret Fibonacci")

for i in range(x):
    print(fibonacci(i), end=' ')