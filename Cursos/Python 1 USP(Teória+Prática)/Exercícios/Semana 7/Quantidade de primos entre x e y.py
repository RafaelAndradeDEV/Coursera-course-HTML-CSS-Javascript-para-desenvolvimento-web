def n_primos(n):
    # n = int(input('Qual valor vc quer verificar se é primo?'))
    multiplicidade = 0
    fator = 2
    saida = float(2)
    multiplos = 2
    while n >= saida:
        while saida >= fator:
            if saida / fator == 1:
                multiplicidade += 1
            while multiplos < saida:
                if saida / fator == multiplos:
                    fator = n + 1
                multiplos += 1
            fator = fator + 1
            multiplos = 2
        fator = 2
        saida += 1
    return multiplicidade


