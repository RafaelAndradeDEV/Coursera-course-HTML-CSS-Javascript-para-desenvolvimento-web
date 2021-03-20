coluna = int(input('Qual lista_inversa quantidade de colunas?(tem que ser maior que 0)'))
linha = int(input('Qual lista_inversa quantidade de linhas?(tem que ser maior que 0)'))
saida = 1
saidaencaixada = 0
while saida != 0:
    while saidaencaixada != linha:
        print(coluna * '#')
        saidaencaixada += 1
    saida = 0