'''                        Prefácio

#um tanto famoso nesta área, data science se encontra na interseção de: Habilidades de hacker Conhecimento de estatística e matemática Competência significativa Originalmente, planejei escrever um livro abordando os três, mas eu rapidamente percebi que uma abordagem completa de “competência significativa” exigiria dezenas de milhares de páginas. Assim, eu decidi focar nos dois primeiros tópicos.

#Se você se tornar um cientista de dados, será íntimo de NumPy, de scikit-learn, de pandas e de diversas outras bibliotecas. Elas são ótimas para praticar data science

Capítulo 1 - Introdução
                            O que é Data Science?
#Há uma piada que diz que um cientista de dados é alguém que sabe mais sobre estatística do que um cientista da computação e mais sobre ciência da computação do que um estatístico

#basicamente não importa como você define data science, pois você encontrará praticantes para quem a definição está total e absolutamente errada. Ou seja, pode ser que vc ache pessoas fazendo marchine learning que são praticante de dados, não há uma definição específica

##De qualquer forma, não permitiremos que isso nos impeça de tentar. Digamos que um cientista de dados seja alguém que extrai conhecimento de dados desorganizados. O mundo de hoje está cheio de pessoas tentando transformar dados em conhecimento.

Ex:- O Facebook pede que você adicione sua cidade natal e sua localização atual, supostamente para facilitar que seus amigos o encontrem e se conectem com você. Porém, ele também analisa essas localizações para identificar padrões de migração global e onde vivem os fã-clubes dos times de futebol

-Em 2012, a campanha do Obama empregou muitos cientistas de dados que mineraram os dados e experimentaram uma forma de identificar os eleitores que precisavam de uma atenção extra, otimizar programas e recursos para a captação de fundos de doadores específicos e focando esforços para votos onde provavelmente eles teriam sido úteis. Normalmente, é de comum acordo pensar que esses esforços tiveram um papel importante na reeleição do presidente, o que significa que é seguro apostar que as campanhas políticas do futuro se tornarão cada vez mais dependentes de dados, resultando em uma corrida armamentista sem fim de data science e coleta de dados.

           Encontrando Conectores-Chave(29-31)
#Uma maneira de pensar sobre o que nós fizemos é uma maneira de identificar as pessoas que são, de alguma forma, centrais para a rede. Na verdade, o que acabamos de computar é uma rede métrica de grau de centralidade

Capitulo 2 - Curso Relâmpago de Python
Formatação de Espaço em Branco Muitas linguagens usam chaves para delimitar blocos de código. Python usa indentação:
for i in [1, 2, 3, 4, 5]:
  print i # primeira linha para o bloco “for i”
  for j in [1, 2, 3, 4, 5]:
    print j # primeira linha para o bloco “for j”
    print i + j # última linha para o bloco “for j”
  print i # última linha para o bloco “for i”
print "done looping"
Isso faz com que o código Python seja bem legível, mas também significa que você tem que ser muito cuidadoso com a sua formatação. O espaço em branco é ignorado dentro dos parênteses e colchetes, o que poder ser muito útil em computações intermináveis:
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

-




























































































'''

