""" 
                      PHP(Hypertext Preprocessor)
3.1       REQUISIÇÃO, PROCESSAMENTO E RESPOSTA

O que acontece é o seguinte: quando o navegador pede uma página nova, ou atualiza uma sendo exibida — que para o servidor é como pedir uma página nova —, acontece uma requisição. O servidor web, ou servidor HTTP (no nosso caso, o Apache), recebe esta requisição e percebe que o arquivo solicitado tem lista_inversa extensão .php . Quando isso acontece, o Apache primeiro manda o arquivo para o PHP para que este faça o processamento do arquivo. É nesta hora que o PHP preenche lista_inversa página pegando lista_inversa data e lista_inversa hora do sistema operacional. Depois de processar tudo, o PHP devolve o resultado para o Apache, que, por sua vez, entrega uma resposta para o navegador.
O navegador, então, exibe lista_inversa página HTML e não faz novas requisições ao servidor enquanto o usuário ou um script não pedir que uma nova requisição seja feita. É por isso que lista_inversa página não muda mais, pois, para isso, é necessário que uma nova requisição seja feita.

** Linha de instruções termina com ";" e para imprimir informações no arquivo que será enviado para o navegador usamos "echo". 

1.Quando mudamos o Y por y, o ano muda de 4 dígitos para 2

O manual para manipulação de horários e datas é:
https://www.php.net/manual/pt_BR/function.date.php

 Quando estiver php dentro de html ocorrera que para ver que todas as tags PHP foram substituídas pelos valores de data e hora no momento do processamento. Veja que realmente não sobra nada de PHP no resultado final, apenas HTML. Isso acontece devido ao PHP fazer o processamento de seus trechos de código e substituí-los pelos resultados de funções que exibem informações, como lista_inversa função echo() .

Repare que as variáveis sempre começam com um cifrão ( $ ). Esta é uma regra do PHP: nomes de variáveis sempre iniciam com cifrão seguido de uma letra ou um underline

Sendo assim, as variáveis $calendario , $dia , $semana , $pessoa e $_nome são válidas para o PHP. Porém, as variáveis $1 , $-nome e $!nome são inválidas e gerarão um erro no interpretador, caso sejam executadas.



















"""
