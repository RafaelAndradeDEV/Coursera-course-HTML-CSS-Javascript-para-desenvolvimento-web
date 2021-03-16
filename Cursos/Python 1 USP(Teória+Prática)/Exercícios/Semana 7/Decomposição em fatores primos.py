n = int(input('Qual o número?'))
variavel = n
multiplicidade = 0
fator = 2
while n > 1:
    while n % fator == 0:
        n = n // fator
        multiplicidade = multiplicidade + 1
    if multiplicidade > 0:
        print('fator {} multiplicidade {}'.format(fator, multiplicidade))
    fator = fator + 1
    multiplicidade = 0

#Se é primo
n = int(input('Qual valor vc quer verificar se é primo?'))
multiplicidade = 0
fator = 2
while n >= fator:
    if n % fator == 0:
        multiplicidade = multiplicidade + 1
    fator = fator + 1

if multiplicidade == 1:
    print('True')
if multiplicidade != 1:
    print('False')