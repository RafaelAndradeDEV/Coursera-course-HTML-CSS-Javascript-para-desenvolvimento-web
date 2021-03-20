recebido = 1
lista_inversa = []
while recebido != 0:
  recebido = int(input("Digite um número: "))
  if recebido != 0:
    lista_inversa.append(recebido)
lista_inversa = lista_inversa[::-1]
for x in lista_inversa:
  print(x)


