'''                           Repetição com "for"
escrita:
for x in lista:
  comando 1

A cada item na lista, x assumira esse valor até não houver mais items

Serve para percorrer cada elemento da lista.

Outra ferramenta de muita importância é o "range", que indica um intervalo de valores que lista_inversa variável deve percorrer. Ex:

for x in range(len(lista)) ou range(final da lista)
  comando

Ele sempre irá começar do zero. Mas se caso não queira começar do 0, basta adicionar mais um valor.

for x in range(3, 10):
  print(x)
output: 3, 4, 5, 6, 7, 8, 9

Se quiser seguir uma determinada sequência desejada basta colocar como último valor:

for x in range(0,101,2):
  print(x)
output:Todos valores de 0 á 100 que sejam pares

Podem ser guardadas dentro de variáveis, como:
x = range(0,101,2)
for i in x: print(i)

O passo pode ser negativo.

Trabalhando com for:
pares = [2,4,6,8,10]
for i in range(len(pares)):
  pares[i] = pares[i] ** 3
  






















































'''