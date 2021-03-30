"""               Everything Is a Number
Key principle: Everything is a number
-Computers only work with numbers
Hardware: bits(0,1)
-Can only do math

 Abstraction: Separation of interface + implementation
 Interface: What it does
 -----------------------
 Implementation: How it Does it

Everything Is a Number:Characters
Actually characters:
- A= 64,B =66
- a = 97, b = 98
- !=33

String: Sequence of characters
Ex: "Hello!"
In abstraction
--------------
72 101 108 108 111 33

Math with letters is Cryptography

            How Is That a Number?
Each image have pixels, and pixels have many tons of colors RGB(0-255 each)

To sum color you´ve the number RGB. Ex:
Pink - 255,0,255
Green - 0,255,0  +
White - 255,255,255

          Developing an Algorithm
When we works with green pixels have a algorithm to discovery which pixel a put in the image final.
That algorithm is:
Have Foreground Image
and Background image
then Output Image

We may compare the pixel colors between foreground and background. 
1°We must look at fglmage, 
If green, the color corresponding in bglmage Should put in the pixel corresponding output color. 
If other colors, not being green, we should put this pixel at the output image. It´s easy  

                A Seven Step Approach to Solving Programming Problems
1- Work example by hand - Solve small instance by hand
2- Write down what you did - Write down exact steps. - Just that instance. Tricky: do without thinking
3 - Find patterns(padrões) - Algorithm for any instance. -Find pattens. - Repetition, conditions, values 
4 - Check by hand. - Check different input
5 - Translate to code
6 - Run test cases
7 - Debug failed test cases

              Variables
Naming a Value: Variables
Ex:
var x = 3;

Can name values with variables
-This example: Declares a new variable
And initializes it to 3

everything may lowercase, if is´t he don´t recognize 
Keyword "var":"i am declaring a new variable"
keyword "x" The name of the variable
keyword "=" attribute for the variable
"3" the value to initialize the variable to
A semicolon:ends the statement

Variables declaration/initialization: Semantics

Semantics is the meaning of the write does

Assignment Statements
- Update value of a variable tha already exist
- No "var"
Ex:
var x = 3;
x = x - 1;

Could Variables hold other things?
Saw some variables with numbers
Can we hold things other than numbers?
-Everything is a Number...
But can use other types of data
-Numbers interpreted in other ways

Expression on right side: More complex(Images)
var fgimage = new SimpleImage("drewRobert.png");
var bgImage = new SimpleImage("dinos.png")

keyword"new":Make an object(It is a piece of data which also has methods that can operate on it.  )
"SimpleImage" - Name of type to creat
"dinos.png" - Parameters: Specify more information






















































































 """
