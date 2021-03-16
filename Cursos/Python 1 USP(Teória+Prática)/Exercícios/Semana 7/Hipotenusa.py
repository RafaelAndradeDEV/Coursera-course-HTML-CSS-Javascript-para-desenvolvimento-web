def soma_hipotenusas(n):
    i = 1
    j = 1
    saida = 1
    soma = 0
    while n >= saida:
        while j < saida and i < saida:
            while i < (saida - 1):
                if (saida ** 2) == (i ** 2) + (j ** 2):
                    if soma != saida:
                        soma = soma + saida
                        i = saida
                if i != saida:
                    i += 1
            if i != saida:
                i = 1
                j += 1
        saida += 1
        i = 1
        j = 1
    return soma

soma_hipotenusas(10)
