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

















 """
