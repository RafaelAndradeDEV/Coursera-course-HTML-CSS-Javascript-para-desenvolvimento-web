<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dia <?php echo date('d/m/y'); ?></title>
</head>
<body>
  <?php 
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
    
    $calendario .= linha($semana);  #Chamada que faz o termino do calendário. Se houver 31 dias.

    return $calendario; 
  } 

  function linha($semana) 
  {
    $linha = '<tr>'; 
    for ($i = 0; $i <= 6; $i++) { 
      if (array_key_exists($i, $semana)) { 
        $linha .= "<td>{$semana[$i]}</td>"; 
      } else {    
        $linha .= "<td></td>";  #Comando que faz os quadrados brancos
    } 
    } 
    $linha .= '<tr>'; 
        
    return $linha;

  } 
  
  
  ?>
  

  <table border="4"> 
    <tr> 
      <th>Dom</th> 
      <th>Seg</th> 
      <th>Ter</th> 
      <th>Qua</th> 
      <th>Qui</th>
      <th>Sex</th> 
      <th>Sáb</th> 
    </tr> 
    <?php echo calendario(); ?> 
  </table>


</body>
</html>
