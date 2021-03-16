x = int(input('Qual o número?'))
i = 2
a = 1
y = (2 or 3 or 4 or 5 or 6)
while x > 0 or x >= i:
    a = x / i
    if a == 1:
        x = -1
    if a == y:
        x = -4
    i = i + 1
if x == -1:
    print('É primo')
else:
    print('Não é primo')
while divisor1 <= valor2:
    valor3 = outrovalor + soma / divisor1
    if valor2 / divisor1 == 1:
        divisor1 = 2
    if valor2 / divisor1 != 1:
        divisor1 = divisor1 + 1

        o = x
        y = (2 or 3 or 4 or 5 or 6)
        valor = 1
        outrovalor = 2
        divisor = 2
        divisor1 = 2
        soma = 1
        recebedor = 1
        valor1 = 1
        valor2 = 1
        valor3 = 1
        if x >= 2:
            while x > 0 or x >= divisor:
                valor = x / divisor
                if valor == 1:
                    x = -1
                if valor == y:
                    x = -4
                divisor = divisor + 1
        if x == -1:
            print(o)
        if x == -4:
            while valor2 <= o:
                valor2 = outrovalor + soma
                valor1 = outrovalor + soma / divisor1
                if valor1 == 1:
                    recebedor = valor2
                while 2 < divisor1:
                    valor3 = valor2 / divisor1
                    divisor1 = divisor1 + 1
                    if valor3 % divisor1 == 0:
                        var = divisor1 == 2
                soma = soma + 1
            print(recebedor)
