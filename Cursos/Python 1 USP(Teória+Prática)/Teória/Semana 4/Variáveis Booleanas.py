#            Indicadores de passagem
'''É lista_inversa utilização de uma variável booleana dentro de um laço de repetição, lista_inversa fim de ser uma forma de saída, isso é um indicador de passagem

Ex:
1°caso
decrescente = True
anterior = int(input('Qual o primeiro valor?'))
valor = 1
while valor != 0 and decrescente
    valor = int(input('Qual o próximo valor da sequência?'))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente:
    print('A sequência está em ordem decrescente')
else:
    print('A sequência não está em ordem decrescente')

2°caso:
meucartão = int(input('Qual o número do seu cartão?'))
cartaolido = 1
encontreimeucartão = False
while cartaolido != 0 and not encontreimeucartao
    cartao = int(input('Qual o número do cartão?'))
    if cartao == meucartao:
        encontreimeucartão = True
if encontreimeucartão:
    print('uhuhh, encontrei ele')
else:
    print('Ahhh que pena não encontrei meu cartão')
'''
#Exercício: #Fazer um reconhecedor de dígitos adjascentes(34566, 117890)
#Errado
'''n = int(input("Digite um número inteiro: "))
lista_inversa = 1
b = 1
c = 11
while b < n and n > 0:
    b = n // lista_inversa % 10
    lista_inversa = lista_inversa * 10
    if b == c:
        b = n + 1
    c = b
if b > n:
    print('Esse número é adjascente')
else:
    print('Esse número não é adjascente')
'''
#Certo
'''n = int(input("Digite um número inteiro: "))
b = 1
c = 11
while b <= n and n > 0:
    b = n // 1 % 10
    n = (n - b) // 10
    if b == c:
        b = n + 5
    c = b
if n + 2 < b or n == 0:
    print('Esse número é adjascente')
if n == b or n + 1 == b:
    print('Esse número não é adjascente')'''