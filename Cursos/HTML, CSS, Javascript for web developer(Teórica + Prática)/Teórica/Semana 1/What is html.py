"""                            Lecture 1: What is html?
HTML is "hyper text markup language" ou seja "Linguagem de marcação de hipertexto"

Hiper text is much text into document, that comeback to major text.
In the syntax of HTML, that writer: 
        wrong                   correct
<h1>                            <h1>                             
    <div>Feliz<h1>                  <div>Feliz<div>
<div>Feliz                      <h1>Feliz                       
   
Components front-end:
HTML:                                           CSS:                                    Javascript:
Empenha a função de estrutura.     Empenha a função de layout,                    "somente na estrutura"
Não possui como fazer cores.             colors, styles        Empenha a função de comporta a parte responsiva

                                Lecture 2: Relevant History of HTML
                                        How we got to HTML5
           
    HTML 4     XHTML 1.0      WHATWG: HTML         WHATWG And W3C      HTML 5
    x > 1997    x > 2000       X > 2004             x > 2007            x > 2011
    Not driven              Web Hypertext           Start work together 
    by Standards            Application technology
    And 4.01                Group

                                Lecture 3: Anatomy of an HTML Tag
    Some tags have one opening tag and closing tag, between them, exist content. Dentro do bracket, existe o nome da tag, a abreviação do que ela vai fazer, mas nem todas são assim, como por exemplo:
    <br> = Line break  and  <hr> horizontal rule. são somente tags de abertura.]


Não é permitido espaço entre o nome da tag e o bracket. Mas deve ter entre as atribuições e as tags. é bom que tenha aspas simples ou aspas duplas na atribuição de valor. 
    <p id = "myID"></p>
Attribute | Attribute
    name  |  Value

    Tags de auto fechamento podem ser <p></p>, significa que não tem conteúdo dentro dela

                                Lecture 4: Basic HTML Document Structure
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
</body>
</html>
                                Lecture 5:  HTML Content Models
Block levels:              Inline elements:
*Render to begin on         *Render on the same line
a new line(by default)      (By default)
*May contain inline or      *May only contain other 
other block elements        Inline elements
#Roughly flow content       #Roughly Phrasing content

#HTML 5 replaces these definitions with more complex set of content categories.
#However, this distinction remains practical because it aligns well with existing CSS rules.

Ex:
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>Div 1</div>
    <div>Div 2</div>
    <span>Span 1</span>
    <div>
        Content of div 3
        <span>Actually have a span inside div</span>
        continue div 3
    </div>
    <h1>Hello world</h1>
</body>

</html>

                Lecture 6: Heading Elements (and some new HTML5 semantic comments)

Semantic htlm element
Is element that implies some meaning to the content

<!Doctype HTML>
<html>
<head>
    <meta charset = "UTF-8">
    <title>Heading tags</title>
</head>
<body>
    <h1>Main tag<h1>
    <h2>2 text<h2>
    <h3>3 text<h3>
    <h4>4 text<h4>
    <h5>5 text<h5>
    <h6>6 text<h6>
</body>
</html>

<body>
<header></header> - Contém tags, navigations, header information. Company logo
<nav></nav>(short for navegation) element - Usually contains links to  different parts of the web site
<section></section> - 
<article></article> - 
make sense article inside section, but is not rule
<aside></aside> - Some information that relates to the main topic, i.e, related posts.
<Footer></footer> - Rodapé, informação que fica lá em baixo
The <div> tag defines a division or a section
</body>

                    Lecture 7: Lists
Use lists to group content, Ex: List to buy, Shopping list
<!Doctype HTML>
<html>

<head>
	<meta charset="UTF-8">
	<title>Studying Lists</title>
</head>

<body>
	<h1>List:</h1>
	<div>
		
    My lunch is:
    <ul>
			<li>Banana</li>
			<li>Maçã</li>
			<li>Alfajor
			  <ul>
				  <li>Chocolate</li>
				  <li>Cobertura</li>
				  <li>Bolacha</li>
        </ul>
      </li>
			<li>Milho</li>
		</ul>

	</div>
</body>

</html>

<ul></ul> - é para fazer lista com pontos no inicio
<ol></ol> - é para fazer listas numeradas





























 """
