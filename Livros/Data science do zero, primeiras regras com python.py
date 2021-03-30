'''                        Prefácio

#um tanto famoso nesta área, data science se encontra na interseção de: Habilidades de hacker Conhecimento de estatística e matemática Competência significativa Originalmente, planejei escrever um livro abordando os três, mas eu rapidamente percebi que uma abordagem completa de “competência significativa” exigiria dezenas de milhares de páginas. Assim, eu decidi focar nos dois primeiros tópicos.

#Se você se tornar um cientista de dados, será íntimo de NumPy, de scikit-learn, de pandas e de diversas outras bibliotecas. Elas são ótimas para praticar data science

Capítulo 1 - Introdução
                            O que é Data Science?
#Há uma piada que diz que um cientista de dados é alguém que sabe mais sobre estatística do que um cientista da computação e mais sobre ciência da computação do que um estatístico

#basicamente não importa como você define data science, pois você encontrará praticantes para quem lista_inversa definição está total e absolutamente errada. Ou seja, pode ser que vc ache pessoas fazendo marchine learning que são praticante de dados, não há uma definição específica

##De qualquer forma, não permitiremos que isso nos impeça de tentar. Digamos que um cientista de dados seja alguém que extrai conhecimento de dados desorganizados. O mundo de hoje está cheio de pessoas tentando transformar dados em conhecimento.

Ex:- O Facebook pede que você adicione sua cidade natal e sua localização atual, supostamente para facilitar que seus amigos o encontrem e se conectem com você. Porém, ele também analisa essas localizações para identificar padrões de migração global e onde vivem os fã-clubes dos times de futebol

-Em 2012, lista_inversa campanha do Obama empregou muitos cientistas de dados que mineraram os dados e experimentaram uma forma de identificar os eleitores que precisavam de uma atenção extra, otimizar programas e recursos para lista_inversa captação de fundos de doadores específicos e focando esforços para votos onde provavelmente eles teriam sido úteis. Normalmente, é de comum acordo pensar que esses esforços tiveram um papel importante na reeleição do presidente, o que significa que é seguro apostar que as campanhas políticas do futuro se tornarão cada vez mais dependentes de dados, resultando em uma corrida armamentista sem fim de data science e coleta de dados.

           Encontrando Conectores-Chave(29-31)
#Uma maneira de pensar sobre o que nós fizemos é uma maneira de identificar as pessoas que são, de alguma forma, centrais para lista_inversa rede. Na verdade, o que acabamos de computar é uma rede métrica de grau de centralidade

Capitulo 2 - Curso Relâmpago de Python
Formatação de Espaço em Branco Muitas linguagens usam chaves para delimitar blocos de código. Python usa indentação:
for i in [1, 2, 3, 4, 5]:
  print i # primeira linha para o bloco “for i”
  for j in [1, 2, 3, 4, 5]:
    print j # primeira linha para o bloco “for j”
    print i + j # última linha para o bloco “for j”
  print i # última linha para o bloco “for i”
print "done looping"
Isso faz com que o código Python seja bem legível, mas também significa que você tem que ser muito cuidadoso com lista_inversa sua formatação. O espaço em branco é ignorado dentro dos parênteses e colchetes, o que poder ser muito útil em computações intermináveis:
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

 Você também pode usar uma barra invertida para indicar que uma declaração continua na próxima linha, apesar de raramente fazermos isso:
 two_plus_three = 2 + \
 3

- Módulos
Alguns recursos de Python não são carregados por padrão. Isto inclui tanto recursos como parte da linguagem assim como recursos de terceiros, que você baixa por conta própria. Para usar esses recursos, você precisará import (importar) os módulos que os contêm. Uma abordagem é simplesmente importar o próprio módulo: import re
my_regex = re.compile("[0-9]+", re.I)
Aqui, re é o módulo que contém as funções e constantes para trabalhar com expressões regulares. Após esse tipo de import, você somente pode acessar tais funções usando o prefixo re… Se você já tiver um re diferente no seu código você poderia usar um alias:
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

Ao visulizar dados com matplotlib, uma convenção padrão é:
Ex:
import matplotlib.pyplot as plt

Se você precisar de alguns valores específicos de um módulo, pode importá-los explicitamente e usá-los sem qualificação:
Ex:
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

                    Funções
Uma função é uma regra para pegar zero e mais entradas e retornar uma saída correspondente. Em Python, definimos as funções usando def:
Devemos semprer colocar um comentário na entrada da função explicando para que ela funciona

As funções de Python são de primeira classe, que significa que podemos atribuí- las a variáveis e passá-las para as funções como quaisquer outros argumentos:
Ex:
def apply_to_one(f): """chama a função f com 1 como seu argumento"""
return f(1)
my_double = double # refere-se à função definida anteriormente
x = apply_to_one(my_double) # é igual a 2

Também é fácil criar pequenas funções anônimas, ou lambdas:
y = apply_to_one(lambda x: x + 4) # é igual a 5
 Você pode atribuir lambdas a variáveis, apesar de que maioria das pessoas lhe dirão para usar def:
 another_double = lambda x: 2 * x # não faça isso
 def another_double(x): return 2 * x # faça isso

Os parâmetros de função também podem receber argumentos padrões, que só precisam ser especificados quando você quiser um valor além do padrão:
def my_print(message="my default message"):
print message
my_print("hello") # exibe 'hello'
my_print() # exibe 'my default message'

Às vezes é útil especificar argumentos pelo nome:
def subtract(a=0, b=0): return a - b
subtract(10, 5) # retorna S
subtract(0, 5) # retorna -S
subtract(b=5) # mesmo que o anterior

            Strings(cadeias de caracteres)
As strings podem ser delimitadas por aspas simples ou duplas (mas elas devem combinar):
 single_quoted_string = 'data science'
 double_quoted_string = "data science"

O Python usa a barra invertida para codificar caracteres especiais. Por exemplo:
tab_string = "\t" # representa o caractere tab
len(tab_string) # é 1

Se você quiser barras invertidas como barras invertidas (que você vê nos nomes dos diretórios ou expressões regulares no Windows), você pode criar uma string bruta usando r"":
not_tab_string = r"\t" # representa os caracteres '\' e 't'
len(not_tab_string) # é 2

Você pode criar strings múltiplas usando aspas triplas ou duplas:
multi_line_string = """esta é a primeira linha.
e esta é a segunda
e esta é a terceira"""

              Exceções
Quando algo dá errado, o Python exibe uma exceção. Se não for manipulada, o programa travará. Você pode manipulá-las usando try e except:
try:
  print 0 / 0
except ZeroDivisionError:
  print "cannot divide by zero"

Apesar de serem consideradas ruins em muitas linguagens, as exceções são usadas livremente no Python para dar uma limpeza no código e, ocasionalmente, faremos o mesmo.

            Listas
Provavelmente, a estrutura de dados mais básica em Python é a list. Uma lista é apenas uma coleção ordenada. (É parecida com o array das outras linguagens, mas com algumas funcionalidades a mais.)
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ] list_length =
len(integer_list) # é igual a 3
list_sum = sum(integer_list) # é igual a 6

Você também pode usar os colchetes para repartir as listas:
x = [-1,1,2,3,4,5,6,7,8,9]
first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:]; # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
without_first_and_last = x[1:-1]; # [1, 2, ..., 8]

O Python possui o operador in para verificar a associação à lista:
1 in [1, 2, 3] # Verdadeiro
0 in [1, 2, 3] # Falso

Essa verificação envolve examinar os elementos de uma lista um de cada vez, o que significa que você provavelmente não deveria usá-la a menos que você saiba que sua lista é pequena (ou a menos que você não se importe em quanto tempo a verificação durará).

É fácil concatenar as listas juntas:
x = [1, 2, 3]
x.extend([4, 5, 6]) # x agora é [1,2,3,4,5,6]
Se você não quiser modificar x você pode usar uma adição na lista:
x = [1, 2, 3]
y = x + [4, 5, 6] # y é[1, 2, 3, 4, 5, 6]; x não mudou
Com mais frequência, anexaremos um item de cada vez nas listas:
x = [1, 2, 3]
x.append(0) # x agora é [1, 2, 3, 0]
y = x[-1] # é igual a 0
z = len(x) # é igual a 4

Às vezes é conveniente desfazer as listas se você sabe quantos elementos elas possuem:
x, y = [1, 2] # agora x é 1, y é 2

É comum usar um sublinhado para um valor que você descartará:
_, y = [1, 2] # agora y == 2, não se preocupou com o primeiro elemento

























































































'''

