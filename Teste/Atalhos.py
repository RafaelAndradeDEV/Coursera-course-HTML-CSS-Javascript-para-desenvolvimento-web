
""" Para colocar comentário no vs code utiliza: Shift + alt + lista_inversa """
""" Atalhos para bookmarks : alt + windows + k """
""" Atalhos para teclas de atalho crtl + k + s """
""" Cmd:
cd .. = voltar uma pasta
cd "name folder" = vai para próxima pasta 
comandos git:
git clone https://github.com/RafaelAndradeDEV/Coursera-course-HTML-CSS-Javascript-para-desenvolvimento-web
ou seja git clone + url do repositório. Vai clonar ele no dispositivo em questão

cd + folder(no caso "Coursera-course-HTML-CSS-Javascript-para-desenvolvimento-web" )

git status = vê como está, o que falta para concluir o backup para github

mkdir + nome da pasta. Cria um diretório com esse nome, dentro da pasta que está no cmd, anterior ao comando 

depois cd "nome da pasta"

Após salvar algum arquivo dentro dessa nova pasta basta usar o comando:

git add .

veja se deu certo com "Git status"

vai faltar commit the past for git, for do it, make: git commit -m "My First page." - Dentro do "" coloque o nome da descrição

volte uma pasta com cd ..

git push  para enviar para o banco de dados do git

caso dê algum erro no push, coloque pull, e depois push de novo



OBS:Nas regras de utilização do browser, é necessário que esteja dentro da tag body para poder ele fazer o reload, ou seja, o php precisa estar dentro dessa tag

Para abrir o browser-sync:
in C:\Project>cd teste
browser-sync start --server --directory --files "*"
browser-sync start --server --files .  se estiver com nome "index.html"
Se não estiver usa:
browser-sync start --server --directory --files .

Para abrir o browse-sync com php:

trocar essa barra do Users
cd C:/Users\Antonio\XAMPP\htdocs\teste

Após iniciar o servidor no apache, no terminal colocar:

browser-sync start --proxy "http://localhost:8080/teste/index.php" --files .

Selecionar o http do "Local" indicado pelo browser-sync

TEXTO EM LATIM, COLOCAR: lorem ipsum

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Feliz!</h1>
</body>
</html>




"""
