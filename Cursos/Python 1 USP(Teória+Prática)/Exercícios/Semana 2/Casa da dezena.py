a = int(input(('Digite um número inteiro:')))
b = a // 100 % 10  #Centenas
c = a // 10 % 10  #Dezenas
d = a // 1 % 10  #Unidades
print('O dígito das dezenas é {}'.format(c))
