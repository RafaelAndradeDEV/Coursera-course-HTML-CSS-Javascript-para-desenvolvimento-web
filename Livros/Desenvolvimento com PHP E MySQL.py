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

 <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dia <?php echo date('d/m/y'); ?></title>
</head>
<body>
  <?php function linha() 
  { 
    function calendario()
    {
      $calendario = '';
      $dia = 1; 
      $semana = []; 
      while ($dia <= 31) { 
        array_push($semana, $dia); 
        
        if (count($semana) == 7) { 
          $calendario .= linha($semana); 
          $semana = []; 
        } 
          
        $dia++; 
      } 
      return $calendario; 
    }

    }
    return " 
      <tr> 
        <td></td> 
        <td></td> 
        <td></td> 
        <td></td> 
        <td></td> 
        <td></td> 
        <td></td> 
      </tr> "; 
  } ?>
<table border="1"> 
  <tr> 
    <th>Dom</th> 
    <th>Seg</th> 
    <th>Ter</th> 
    <th>Qua</th> 
    <th>Qui</th>
    <th>Sex</th> 
    <th>Sáb</th> 
  </tr> 
  <?php echo linha(); ?> 
  <?php echo linha(); ?> 
  <?php echo linha(); ?> 
  <?php echo linha(); ?> 
  <?php echo linha(); ?> 
</table>

</body>
</html>


Repare que as variáveis sempre começam com um cifrão ( $ ). Esta é uma regra do PHP: nomes de variáveis sempre iniciam com cifrão seguido de uma letra ou um underline

Sendo assim, as variáveis $calendario , $dia , $semana , $pessoa e $_nome são válidas para o PHP. Porém, as variáveis $1 , $-nome e $!nome são inválidas e gerarão um erro no interpretador, caso sejam executadas.

também estamos usando um tipo de dados do PHP chamado de array para a variável $semana . Um array contém uma lista de dados e pode ser composto por strings, números, outros arrays e outros tipos de dados do PHP que veremos no decorrer do livro.

Para iniciar um novo array, é possível utilizar a sintaxe array() ou a nova sintaxe dos colchetes, que é mais simples e elegante. Veja no exemplo a seguir duas formas de se iniciar um novo array vazio: 
<?php $dias = array(); 
$meses = []; ?>

array contém, e o PHP se encarregará de criar as chaves para acessar os valores, que serão numéricas. Veja um exemplo: <?php $meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril']; echo $meses[1]; ?> Neste caso, será exibido Fevereiro,

Após criar um array, você também pode inserir valores nele. Existem duas formas de se fazer isso: uma usando a função array_push() e outra usando a sintaxe dos colchetes. Veja um exemplo onde as duas formas funcionam da mesma maneira: 
<?php 
$dias = []; 
$meses = []; 
$dias[] = 'Segunda'; 
$dias[] = 'Terça'; 
array_push($meses, 'Janeiro'); 
array_push($meses, 'Fevereiro'); 
?>
A diferença é que o push exigirá um pouco mais recursos da máquina

Perceba que, ao utilizar a forma dos colchetes, é possível nomear as chaves dos valores. Dessa forma, podemos ter não apenas chaves numéricas, mas também strings. Assim fica bem simples de montar variáveis contendo diversas informações, como nesse caso, um array com os dados de uma pessoa. 
  Já o array_push() nos permite adicionar diversos itens de uma vez só. Porém, não é possível escolher as chaves, pois elas serão numeradas automaticamente pelo PHP.

Existe ainda uma outra forma de criar arrays já atribuindo chaves e valores. Veja no exemplo: 
<?php 
  $pessoa = [ 
    'nome' => 'Linus', 
    'sistema' => 'Linux', 
    'linguagem' => 'C', ]; 
    echo $pessoa['nome']; 
    echo $pessoa['sistema']; 
    echo $pessoa['linguagem']; 
?>

Neste caso, estamos criando o array $pessoa já com os índices nome , sistema e linguagem . Após sua criação, ainda é possível modificar os valores dos índices existentes, ou mesmo criar mais índices: 
<?php
  $pessoa = [ 
    'nome' => 'Linus', 
    'sistema' => 'Linux', 
    ]; 
  $pessoa['nome'] = 'Linus Torvalds'; 
  $pessoa['linguagem'] = 'C'; 
?>

          Concatenação de strings
Em PHP, usamos o ponto ( . ) para fazer a concatenação de strings, isso é, juntar uma string ao final da outra. No exemplo anterior, a string estudando PHP será adicionada ao conteúdo já existente na variável $texto . Também podemos utilizar a forma reduzida, que é usando o .= , como na variável $calendario do exemplo. Usar o .= é a mesma coisa de usar $variavel = $variavel . 'algo a mais' . 
Veja o exemplo: 
<?php $texto = 'Estou'; 
$texto .= 'estudando PHP'; 
echo $texto; ?>

usar a função array_key_exists() , que verifica se um índice em um array existe.

++$i //first increment $i then run line
$i++ //first run line then increment $i




















"""
