""" 
Url = Uniform Resource locator
HTML5 Begin be standard in 2014
                          Different Types of Elements    
*Metadata elements:
  Information about the page. EX: html, head, title...
  <html> : * Contains all other elements * Specifies using HTML standart
  <head> : * Information about the page: title, scripts, CSS
  <title> : * specifies page title * Nested inside <head></head> tags

*Sectioning elements:
  Define regions.Ex:Body, h1, div
  <body> : * Contains all items seen on page
  <h1> : * Section header * Also <h2> <h3> ... <h6>
  <div> : * Defines section of web page *Useful CSS
  <b> : Bold
  <em> : Emphasize

                  Formatting Text and Nesting Tags
Semantic or Style HTML Tags:
Tags surround text ou page elements
<b>Make text stylistically different </b>
<b>Traditionally bold face, but can change</b>                  
<em>Emphasize text!</em>
<b>this</b><em>is an<b>example fo nested</b>tags</em>
nesting: Aninhando

                  Adding Images and Links
Image and Multimedia Tags:
*Web pages can include images, video, audio:
Different kinds of tags. Ex:
Image tag:
<img src="link" />
<img src="link" width = ""pixels ou porcentagem" height = "Pixels ou porcentagem" />

Altura e largura são opcionais, mas são importantes de usar. Não possui end tag, src required.

Linking Pages Together:
<a href = "link">"Texto que vai aparecer"</a> Pode colocar texto após.
anchor tag, href attribute, clickable text"

Creating web resources:
*Making a web page look good isn´t easy
Designers understand HTML very well, Designers know how to use tools, You are learning the basic, a foundation, can be display in mobile too, interactivity makes this a challenge

                Images and Storage
What to use for src=".."? src is attribute is used to specify the URL of the source image      
- Copyright concerns(preocupação). Existe casos em que uma empresa pode abrir uma ação contra o uso da imagem dela em seu site
-Image Storage. Lugares que hospedam imagens
-What about videos? Mesmo caso, tem que haver cuidado com o copyright

Usage rights for images/photos
*some images are copyrighted
-Laws vary across countries. Typically ok, for personal, non-commercial use.. Usage rights with copyright holder
*Some images in public domain. Podem ser usado sem haver direito sobre. Creative Commons, não é ilegal se não usar para uso comercial.

Inline or Hot linking
-Inline linking also called "hot-linking"
For personal pages, copyright usually ok
Websites with lots of traffic? Maybe a concern

Finding links to online photos
*Create links to photos found online
-Right click and copy Url, then paste
*Some sites don´t allow hot-linking
-Test your webpage
--Use incognito or private browsing
-Have someone else test it too!

Links sites for take photos:
https://www.flickr.com/
http://postimage.org/
http://photobucket.com/
https://www.dropbox.com/
https://www.base64-image.de/
http://tinypic.com/

              Lists and Tables
<p> is paragraph        
*Simple Lists
Some lists use circles or bullets
- These are unordered lists, tag:<ul></ul>
- Content viewed in order, list labels all the same

<ul> is point
<ol> is ordered list


Ex:<ul>
<li>Feliz</li>
<li>Jogador</li>
</ul>

<li> is each item at lists
This is are the struture of Lists

Inside <ul></ul> must have sequence of <li></li> elements
-Anything between <li></li> elements, not just text: <img>,<a href>,<ul>,...

May want ordered list
-Numbers can be important
-Also possible: Letters

<ol> is ordered list
-<li></li> required
- Automatic numbering
- - Add, remove <li>
- - Numbers change

We can compose HTML elements
-Composition important concept in Computer Science and other disciplines
-Construct web pages with elements that can contain other elements
-lists of images 
-list of lists

*Nested Lists
<ul> in <li></li>
-bullets "change"
-Indentation helps

<ul>
    <li>Feliz</li>
      <ul>
        <li>Feliz</li>
          <ul></ul>Termos #or <br> without end tag
          <ul>
            <li>Nice</li>
            <li>GG</li>
          </ul>
      </ul>
</ul>

*HTML Tables
Tables information in rows and columns
-General organization? CSS preferred
Tables constructed from HTML elements that correspond to visible table

HTML table elements
<tr> - Table row
<td> - Table cells
<th> - Table header

<table></table>
Contains rows <tr></tr> - 

Rows contain
header elements <th></th>
table cells <td></td>
Ex:
<table>
 <tr>
  <th>Adjetivos</th>
  <th>Móveis</th>
 </tr>
 <tr>
  <td>Feliz</td>
  <td>Guarda Roupa</td>
 </tr>
 
</table>

You can put images inside <td> tag and other things

HTML tables and lists help organize information
- From simple to complex
- <li> elements can contain tables
- <td> elements can contain lists

            How CSS is Used to Design Web pag
          
*Viewing and Experiencing Web Pages
Web Page may be displayed differently
-kind of device, kind of screen
-Design to accommodate users
Experience web pages differently - Colorblind, difficult in click link
-Typical computer monitor
-Mobile device
-Huge display screen

*Web Page Accessibility
Work to ensure(Garantir) web pages accessible
-Remove Barriers(Barreiras), Help everyone
-Sight, Hearing, color, clicking, more
-Example: Help Screen-reading
-Example: Colors and fonts
Good UX(User experience)
-Pages load quickly 

CSS(Cascading Style Sheets)
-Specifies look and formatting
-Separates content from presentation
- - How big is <h1>?
- - Color for <h1>?
- - Mobile or Desktop?
-Design that Scales
- - 1000 Pages on website

                CSS Basics
*Css              
Last time: Why CSS?
-Reusability :Vc conseguir fazer um código de estilo e usar em vários códigos
- Maintainability(Capacidade de Manutenção):Easy to maintainability
This time: How to write your own 

For you link css you should use: <link> or <style>

CSS Syntax
Ex:
h1 {
  text-align: center;
  color: blue;
}
h1 is "Selector: What element to format"
{} is Curly braces around formatting for that element
text-align: is Property to change, and later have ":" The colon and later Value, late semicolon
color is property to change

CSS: Select Some Elements
li {
  Color: green;
}
Makes all <li>s green
What if we want some green?

Three approaches:

First:  CSS: Classes
Classes: named styles, various elements
- In HTML code:
<li class="foodLi"> Chocolate </li>
<li class="foodLi"> Cherries </li>
<li class="foodLi"> Ice Cream </li>
- In CSS:
.foodLi {            #The point before "foodLi" is a Dot: Making a class, after him you have Class name: Anything you want, don´t able to put spaces and other things
  color:green;
}

Second: CSS:IDs
IDs: Name one element
- In HTML Code:
<img src = "cake.jpg" id="cakeImg" />
- In CSS:
#CakeImg {
  float:right;
 }

 Third: CSS: Combinators
Combinators: Select by relationship
-Style <li> inside of <ul>:
ul li {...}
-More advanced relationships exist

*Classes ans IDs: Name and Reuse
Class and ID: name Style
- Re-use as needed
- Many elements in one page
- Across pages. You can make one stylus for every pag that you´ve
- Name + use: recurring concept in CS

                  Colors and Names in CSS
Colors
-Names and Numbers

140 Standard color names
Exist millions of colors
The RGB come from 0 to 255
Can specify 16 millions colors

We can specify with RGB, such gold:(255,215,0)
or entire number: # + 6 hex digits
-Hexadecimal: base 16
-Digits: 0-9, A (10)-F(15)
like: gold = #FFD700
2 first hexadecimal numbers are R(red)
2 Second hexadecimal numbers are G(green)
2 third hexadecimal numbers are B(Blue)

To convert in Numbers, take the Fórmula:
Ex: #8A2BE2
2° 8 * 16 + 10 * 1 = 138
2°2 2* 16 + 11 * 1 = 43
2°3 14 * 16 + 3 * 1 = 226
RGB=(138,43,226)

Have tools to take a color ex:
ColorPicker

Code:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Studying Lists</title>
  <link rel="stylesheet" href="teste.css" type="text/css">
</head>
<body>
  <div>
    <h1>Quentin's Page of Interests</h1>
    <p>The world wants to know: who is Quentin Ruiz-Esparza? Read this page to learn about Quentin's likes (and maybe his dislikes)!</p>
  </div>
  <div>
    <h2>What's Your Top 5?</h2>
    <p>Quentin was recently asked about his top 5 movies, musicians, and places he has visited. Here are his answers!</p>
    <h3>Movies: Justice league</h3>
    <h3>Music Artists: None</h3>
    <h3>Places I've Visited: Ceará, Brazil</h3>
  </div>
  <div>
    <table>
      <tr>
        <th>Foods</th>
        <th>Books</th>
        <th>Peoples to meet</th>
      </tr>
      <tr>  
        <td>
          <ol>
            <li>french fries</li>
            <li>Cake</li>
            <li>Hamburger</li>
          </ol>
        </td>
        <td>
          <ol>
            <li>How to sleep</li>
            <li>How to programming in Python</l>
            <li>Python for data science</li>
          </ol>
        </td>
        <td>
          <ul>
            <li>Emily</li>
            <li>Deyse</li>
            <li>Lucas</li>
          </ul> 
        </td>
      </tr>
    </table>
  </div>

</body>
</html>






















 """
