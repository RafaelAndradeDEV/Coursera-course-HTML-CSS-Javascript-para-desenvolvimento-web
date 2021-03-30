<?php 
    $pessoa = []; 
    $alunos = [];
    $pessoa['nome'] = 'Linus'; 
    $pessoa['sistema'] = 'Linux'; 
    $pessoa['linguagem'] = 'C'; 
    array_push($alunos, 'Maria', 'Joana', 'Paulo', 'Pedro'); 
    echo $pessoa['nome']; 
    echo $alunos[1]; 
  ?>

<?php 
  $pessoa = [ 
    'nome' => 'Linus', 
    'sistema' => 'Linux', 
    'linguagem' => 'C', ]; 
    echo $pessoa['nome']; 
    echo $pessoa['sistema']; 
    echo $pessoa['linguagem']; 
?>

