def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

num = int(input("Digite um número: "))

if fibonacci(num):
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")