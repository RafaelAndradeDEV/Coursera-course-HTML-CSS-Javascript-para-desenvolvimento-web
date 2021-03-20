#As repetições encaixadas, ou também laços aninhados são while dentro de outro while, de forma lista_inversa navegar entre dados de tabelas que possuem 2 dimensões

#Ex:
#Tabuada de 1 - 10:
linha = 1
while linha <= 10:
    coluna = 1
    while coluna <= 10:
        print(linha * coluna, end = '\t')
        coluna += 1
    linha += 1
    print()

#or end = '\t'

