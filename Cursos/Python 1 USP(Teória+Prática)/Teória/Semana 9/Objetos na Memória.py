'''                                         Objetos na memória
Os objetos são estrutura de dados e funções que vão manilupar esses dados, e são armazenados na memória do computador. Para isso o computador disponibiliza um pedaço da memória para esse objeto, que pode ser consultado como uma variável

                                  Objetos e referências
str são imutáveis no python e listas são mutáveis
se: a = "banana"
a recebe um local na memória que está atrelado juntamente, banana
se colocarmos b = "banana"

A memória irá apontar para a mesma str, mas com variáveis diferentes
para testarmos isso colocamos:
a is b
output:True

Já se forem listas ocorre o seguinte caso:
a = [1,2,3]
b = [1,2,3]
a is b
output:False
mas se colocarmos
a == b
output: True

Isso ocorre porque listas são mutáveis e são reconhecidas como diferentes lugares na memória, é como se cada variável possuisse uma lista diferente, mas não é o caso.

                                        Repetições e referências
-Podemos criar uma nova lista fazendo repetições de uma lista.

Ex:
Lista = [1,2,3]
Lista1 = [Lista]*3

Se mudar um valor em Lista, será mudado nas 3 listas da Lista1, isso porque existe um seta apontando para cada lista, se mudarmos uma, mudamos todas as outras. A lista1 está apontando 3 vezes para o mesmo objeto(Lista)



























'''