def maior_primo(x):
    o = x
    y = (2.0)
    z = 2.25
    valor = 1
    outrovalor = 2.0
    divisor = 2
    divisor1 = 2
    soma = 1.0
    recebedor = 1
    valor1 = float
    valor2 = 1
    valor3 = 1
    if x >= 2:
        while x > 0 or x >= divisor:
            valor = x / divisor
            if valor == 1:
                x = -1
            while y < x:
                if valor == y:
                    x = -4
                y = y + 1
            divisor = divisor + 1
            y = 2
    if x == -1:
        recebedor = o
    if x == -4:
        while valor2 < o:
            divisor1 = 2.0
            valor2 = outrovalor + soma
            valor1 = (outrovalor + soma) / divisor1
            while divisor1 <= valor2:
                valor1 = (outrovalor + soma) / divisor1
                if valor1 == 1:
                    recebedor = valor2
                while y < valor2:
                    if valor1 == y:
                        divisor1 = valor2 + 1
                    y = y + 1
                divisor1 = divisor1 + 1
                y = 2
            soma = soma + 1
    return recebedor
