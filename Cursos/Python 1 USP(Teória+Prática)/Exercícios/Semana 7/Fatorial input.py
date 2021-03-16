n = 1
while n >= 0:
    n = int(input('Qual o número?'))
    fatorial = 1
    while n != 0 and n > 0:
        fatorial = fatorial * n
        n = n - 1
    if n > 0 or n == 0:
        print(fatorial)