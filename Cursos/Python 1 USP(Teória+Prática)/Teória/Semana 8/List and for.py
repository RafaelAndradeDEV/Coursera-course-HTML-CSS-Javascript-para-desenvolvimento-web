                               #* Listas(array)  " [] "
'''Nas listas(array) podemos armazenar lista de valores, coleção de objetos, coleção de palavras, ou até mesmo listas. Em outros programas são chamados de array ou vetor, pois guarda valores unidimensionais linearmente
Ex: Vc quer analisar a temperatura que fez todo o mês logo:
temperatura = [29, 25.6, 24]

Para pegar um valor dentro da lista temperatura é somente escrever temperatura[0] == 29 is True.
Também é aceito a utilização de indice negativo. Ex:
temperatura[-1] == 24 is True.
Sempre começando do final para o começo da lista.

Nela podemos ter str, int, float. Diversas classes dentro de uma lista. 

Para adicionar um novo elemento colocamos ''.append'', ele ira concatenar ao final da lista esse novo elemento
temperatura.append(8)

Criação de uma lista vazia: olá = []

Trocar valores na lista:
temperatura [2] = 34


                    Repetição com for
for item in lista. Para cada item da lista, o valor ficará se armazenando no item temporariamente até que a lista seja terminada. Será executada a quantidade de Elementos que estiverem na listaEx:

amofrutas =  ["banana", "maçã", "acerola"]
for frutas in amofrutas:
    print('gosto de', frutas)

output = gosto de banana
gosto de maçã
gosto de acerola
                               
Também utilizamos "range", é um intervalo de 0 até um valor. Limite de valores com inicio e fim. Ex:
            intervalo entre ini e o fim, sendo ini diferente de 0.
for i in range(ini, fim, passo)
            Passo é para saber de quanto em quanto quero que i recebe o valor da lista.

for i in range(20):
    print(i)

output = 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

Executará 20 vezes, mas não o 20 pois começa do 0

Poderia ser também:
For i in range(len(lista))
Percorrera toda a lista, começando do 0.

Se quiser começar de um certo número até o final, pode ser:
for i in range(x, fim)

Também é aceitável o passo ser negativo:
numeros = range(100, 5, -5)
for x in numeros:
    print(x)
    
#Ele nunca vai demonstrar o valor que vc colocou como final

Pode fazer a mudança da lista dentro de uma repetição:
for i in range(len(primos))
    primos[i] = primos[i]**3
Ele vai resultar em primos ao cubo dentro da lista
                               
                               
                        Manipulação de listas
numeros = [1,2,3,4]
Para fatiar a lista podemos fazer
numeros[1:2]
output = 2   # Porque é o inicio no indíce 1 e vai até o 2

Do começo ao final pode ser:
numeros[:2]
output = 1,2

Para clonar uma lista não é somente fazer:
lista1 = [1,2]
lista2 = lista1
Porque se vc mudar algum valor, ou adicionar. As listas vão mudar simultaneamente 

Pode ser feito:
lista2 = lista1[:]
ou então:
def clone(lista):
    clone = []
    for objeto in lista:
        clone.append((objeto))
    return clone
    
Verificar se algo está na lista basta escrever:
"NOME" in lista:
Output = True, or false

Juntar lista em diferentes ordens usamos:
a = [1,2,3]
b = [4,5,6]
a + b
output: [1,2,3,4,5,6]
E para armazer esse valor é simple
b = a + b

 O .append muda uma lista existente e o '+' ele gera uma nova lista sem alterar as listas existentes
 
 a_triplicado = a * 3
 output = [1,2,3,1,2,3,1,2,3]
 
 Para excluir algo da lista basta:
 del a[1]
 ou:
 del a[1:13]
 
 Ex de treino:
 a = [1,2,3]
for x in range(len(a)):
    a[x] = a[x]*3
print(a)

a = [1,2,3]
for x in range(1,4):
    print((x*3), end=", ")
                        
                               
                               
                               














'''