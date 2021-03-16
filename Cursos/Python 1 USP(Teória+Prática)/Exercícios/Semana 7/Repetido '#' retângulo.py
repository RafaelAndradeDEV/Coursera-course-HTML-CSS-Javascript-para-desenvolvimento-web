coluna = int(input('Qual a quantidade de colunas?(tem que ser maior que 0)'))
linha = int(input('Qual a quantidade de linhas?(tem que ser maior que 0)'))
saida = 0
saidaencaixada = 0
while saida != 1:
    while saidaencaixada != linha:
        print(coluna * '#')
        saidaencaixada += 1
        if coluna > 2 and linha > 2:
            while (linha-2) != saida:
                print('#', end = (coluna - 2) * ' ')
                print('#', end = '\n')
                saida += 1
                saidaencaixada += 1
    saida = 1