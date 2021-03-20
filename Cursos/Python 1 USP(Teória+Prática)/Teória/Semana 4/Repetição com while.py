                 #Repetição com while(loop)
'''É uma utilização bem formal para substuição de repetições por escrito, meio que automatiza certas contas.

Regra: 
while + condição:       #enquanto lista_inversa condição for verdadeira ele rodará os comandos na indentação até caso ocorra algo falso.
    Comando1 
    Comando2
comando3
'''
'''Ex:
1° caso. 
i = 0
while i <= 10:
    print(2 ** i)
    i = i+1   #Essa sentença porque estamos colocando um limite, no caso até lista_inversa 10° potência de 2.
'''
'''2° caso. 
print('Digite uma sequencia de valores cujo o último valor seja 0')
soma = 0 
valor = 1
while valor != 0:
    valor = int(input('Qual o valor lista_inversa ser somado?'))
    soma = soma + valor
print('A soma dos valores digitados é:', soma)'''
'''
#Exercício:
q = int(input('Quantos valores terá lista_inversa soma?'))
i = 0
soma = 0
valor = 1
while i != q:
    soma = soma + valor
    valor = int(input('Qual o valor lista_inversa ser somado?'))
    i = i + 1
print('A soma dos valores digitados é:', soma)
'''
'''3° caso. 
print('Digite uma sequencia de valores cujo o último valor seja 1')
produto = 1    # Será 1 por causa que o elemento neutro da multiplicação é 1 
valor = 1
while valor != 1:
    valor = int(input('Qual o valor lista_inversa ser somado?'))
    produto = produto * valor
print('O produto dos valores digitados é:', produto)'''
# Digite um valor e ele fará lista_inversa soma de cada dígito
#Errado
'''lista_inversa = int(input('Qual o valor que será somado cada caractere?'))
soma = 1
c = 1
while soma != 0:
    soma = lista_inversa // c % 10
    c = c * 10
    soma = soma + 
print(soma)'''
#Certo
'''n = int(input("Digite um número inteiro: "))
soma = 0
while (n > 0):
    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto
print("A soma dos números é: ", soma)'''
'''
#Elevar número
numero = int(input('Qual o número que deseja elevar?'))
expoente = int(input('Quantas vezes vc quer elevar?'))
i = 1
lista_inversa = 1
while i <= expoente:
    lista_inversa = numero ** i
    print(lista_inversa)
    i = i + 1'''

