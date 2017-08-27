INSTALLTION
-----------

Linux
-----
Linux is a varied operating system with a bunch of different ways to install software. I’m assuming
if you are running Linux then you know how to install packages, so here are your instructions:
1. Use your Linux package manager and install the gedit text editor.
2. Make sure you can get to gedit easily by putting it in your window manager’s menu.
a. Run gedit so we can fix some stupid defaults it has.
b. Open Preferences and select the Editor tab.
c. Change Tab width: to 4.
d. Select (make sure a check mark is in) Insert spaces instead of tabs.
e. Turn on Automatic indentation as well.
f. Open the View tab and turn on Display line numbers.
3. Find your Terminal program. It could be called GNOME Terminal, Konsole, or xterm.
4. Put your Terminal in your dock as well.
5. Run your Terminal program. It won’t look like much.
6. In your Terminal program, run Python. You run things in Terminal by just typing the
name and hitting Enter.
a. If you run Python and it’s not there, install it. Make sure you install Python 2, not
Python 3.
7. Type quit() and hit Enter to exit Python.


=================================================================================================================

excerise 1: 

print "hi "
print "hello again"
print "I'm typing this"


Example of an error message

$ python ex/ex1.py
File "ex/ex1.py", line 3
print "I like typing this.
^
SyntaxError: EOL while scanning string literal
It’s important that you can read these, since you will be making many of these mistakes. Even I
make many of these mistakes. Let’s look at this line by line.
1. Here we ran our command in the Terminal to run the ex1.py script.
2. Python then tells us that the file ex1.py has an error on line 3.
3. It then prints this line for us.
4. Then it puts a ^ (caret) character to point at where the problem is. Notice the missing "
(double- quote) character?
5. Finally, it prints out a SyntaxError and tells us something about what might be the error.
Usually these are very cryptic, but if you copy that text into a search engine, you will find someone else who’s had that error and myou can probably fi gure out how to fix it.

#********#
*WARNING!* 
#********#
If you are from another country and you get errors about ASCII encodings,then put this at the top of your Python scripts:
# - *- coding: utf- 8 - *-
It will fi x them so that you can use Unicode UTF- 8 in your scripts without a problem.
======================================================================================================================

Comments are very important in your programs. They are used to tell you what something does in English, and they also are used
 to disable parts of your program if you need to remove them temporarily.
ex 2:

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
print "I could have code like this." # and the comment after is ignored
# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."
print "This will run."
========================================================================================================================

Number and Maths

+ plus		- minus   / slash		* asterisk  % percent 	< less- than  > greater- Than 	<= less- than- equal 	
>= greater- than- equal

ex3: 
print "i will count my hens"
print "Hens", 25+30/6
print"Now i will count eggs", 3
print float(3+2+1-5+4%2-1/4+6)
print "is it true that 3+1<5-7"
print float(3+1<5-7)
print "what is 3+2", 3+2
print "what is 5-7", 5-7
print "oh that's why it is false"
print "now let's find out area of a circle with radius 5 cm", float(3.14*5*5)

What is the order of operations?
In the United States we use an acronym called PEMDAS, which stands for Parentheses Exponents
Multiplication Division Addition Subtraction. That’s the order Python follows as well.
==========================================================================================================================

Variables And Names

A variable is nothing more than a name for something so you can use the name rather than the something as you code.
ex4: 

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
if cars >= drivers:
    cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

” Every time you put " (double- quotes) around a piece of text, you have been making a string"
ex 5:

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

Conversion 		Meaning 		Notes
d 		Signed integer decimal. 	
i 		Signed integer decimal. 	
o 		Unsigned octal. 	(1)
u 		Unsigned decimal. 	
x 		Unsigned hexadecimal (lowercase). 	(2)
X 		Unsigned hexadecimal (uppercase). 	(2)
e 		Floating point exponential format (lowercase). 	
E 		Floating point exponential format (uppercase). 	
f 		Floating point decimal format. 	
F 		Floating point decimal format. 	
g 		Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise. 	
G 		Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise. 	
c 		Single character (accepts integer or single character string). 	
r 		String (converts any python object using repr()). 	(3)
s 		String (converts any python object using str()). 	(4)
% 		No argument is converted, results in a "%" character in the result. 	

 Notes:
(1)    The alternate form causes a leading zero ("0") to be inserted between left-hand padding and the formatting of the number   if the leading character of the result is not already a zero. 
(2)    The alternate form causes a leading '0x' or '0X' (depending on whether the "x" or "X" format was used) to be inserted   between left-hand padding and the formatting of the number if the leading character of the result is not already a zero. 
(3)    The %r conversion was added in Python 2.0. 
(4)    If the object or format provided is a unicode string, the resulting string will also be unicode. 
   
How can I round a fl oating point number?
You can use the round() function like this: round(1.7333).

I get this error TypeError: 'str' object is not callable.
You probably forgot the % between the string and the list of variables.
================================================================================================================================

Strings and Text
----------------
strings are allways enclosed in double quotes ("") or in single quotes ('') this is how python knows that we are making a string.
string may conatin format charecters, FOR EG %d , %s .you simply put the formatted variables in the string, and then a
% (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside ( ) (parentheses) separated by , (commas).

Python has join() method to concatenate a string.
''.join(['the','quick','brown','fox','jumps','over','dog'])
>>> print ‘red’ + ‘yellow’
Redyellow
>>> print ‘red’ * 3
Redredred
>>> print ‘red’ + str(3)
red3
>>> print ‘red’ + 3
Traceback (most recent call last):
File “”, line 1, in
TypeError: cannot concatenate ‘str’ and ‘int’ objects
>>>

String Formating with % Operator
--------------------------------
x = ‘apples’       y = ‘lemons’
z = “In the basket are %s and %s” % (x,y)

String Formating with {} Operator
---------------------------------
When you use the curly braces or {} operators, they serve as place-holders for the variables you would like to store inside a string. In order to pass variables to a string you must call upon the format() method. One benefit of using the format() method is that you do not have to convert integers into a string before concatenating the data. It will do that automatically for you. This is one reason why it is the preferred operator method.
Fname = “John”
Lname = “Doe”
Age = “24”
print “{} {} is {} years old.“ format(fname, lname, age)
ex 6: Strings

x = "There are %d types of people." % 10 #here we define a variable x which holds a string and we are inserting 10 in bet the string
binary = "binary" #here we declared and initialized the varibale biinary with value equals binary
do_not = "don't" #here we decalared and initialized another variable do_not
y = "Those who know %s and those who %s." % (binary, do_not)#here we are inserting two variable inside a string
print x #printing var x
print y #printing var y
print "I said: %r." % x #inserting a string in a string
print "I also said: '%s'." % y #inserting  string in a string
hilarious = False #declaring and initializing the variable
joke_evaluation = "Isn't that joke so funny?! %r" #initializing the variable
print joke_evaluation % hilarious #printing two var holding strings using % operator
w = "This is the left side of..." #def a var
e = "a string with a right side." #def a var
print w + e #concatenating and printing two strings

What is the difference between %r and %s?
We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and others for displaying to users.
==============================================================================================================================
More printing
-------------
ex 7: 

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do? ans print '.' 10 times
end1 = "C" # def a var end1-end12
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

Couldn’t you just not use the comma , and turn the last two lines into one single- line print?
Yes, you could very easily, but then it’d be longer than 80 characters, which in Python is bad style.
================================================================================================================================
Printing, Printing
------------------
ex 8:

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)

I tried putting Chinese (or some other non- ASCII characters) into these strings, but %r prints out
weird symbols.
Use %s to print that instead and it’ll work.
=================================================================================================================================
Printing , Printing, Printing 
-----------------------------

# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
wit the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

Why do the \n newlines not work when I use %r?
That’s how %r formatting works; it prints it the way you wrote it (or close to it). It’s the “raw” format for debugging.
=================================================================================================================================
What is That?
-------------
This use of the \ (backslash) character is a way we can put diffi cult- to- type characters into a string.
There are plenty of these “escape sequences” available.

Escape   What it does.
\\       Backslash (\)
\'       Single- quote (')
\"       Double- quote (")
\a       ASCII bell (BEL)
\b       ASCII backspace (BS)
\f       ASCII formfeed (FF)
\n       ASCII linefeed (LF)
\N       {name} Character named name in the Unicode database (Unicode only)
\r       ASCII carriage return (CR)
\t       ASCII horizontal tab (TAB)
\u       xxxx Character with 16- bit hex value xxxx (Unicode only)
\U       xxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
\v       ASCII vertical tab (VT)
\o       oo Character with octal value oo
\x       hh Character with hex value hh  

ex 10:
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat

When I use a %r format none of the escape sequences work.
That’s because %r is printing out the raw representation of what you typed, which is going to
include the original escape sequences. Use %s instead. Always remember this: %r is for debugging;
%s is for displaying.print fat_cat
=================================================================================================================================
Asking Question
---------------

print "how old are you?",
age=int(raw_input())
print "what is your weight?",
weight=raw_input()
print "how tall are you?",
tall=raw_input()
print "hey i want to ask some more question"
print"do you know about stuxnet",

#Notice that we put a , (comma) at the end of each print line. This is so that
#print doesn’t end the line with a new line character and go to the next line.
presents a prompt to the user (the optional arg of raw_input([arg])), gets input from the user and returns the data input by the user in a string. See the docs for raw_input().
Example:
name = raw_input("What is your name? ")
print "Hello, %s." % name

This differs from input() in that the latter tries to interpret the input given by the user; it is usually best to avoid input() and to stick with raw_input() and custom parsing/conversion code.

Note: This is for Python 2.x in python 3 is renamed to input() but note that input is a vulnerable method as it inputs everything as python code so we can input malicious python code.
How do I get a number from someone so I can do math?
That’s a little advanced, but try x = int(raw_input()), which gets the number as a string from
raw_input() then converts it to an integer using int().

What’s the difference between input() and raw_input()?
The input() function will try to convert things you enter as if they were Python code, but it has security problems so you should avoid it.
The raw_input() function in Python 2.x evaluates things before returning.
So as an example you can take a look at this -

>>> input("Enter Something : ")
Enter Something : exit()

This would cause the program to exit (as it would evaluate exit()).

Another example -

>>> input("Enter something else :")
Enter something else :__import__("os").listdir('.')
['.gtkrc-1.2-gnome2', ...]
"
"This would list out the contents of current directory , you can also use functions such as os.chdir() , os.remove() , os.removedirs() , os.rmdir()
"
=================================================================================================================================
Prompting People
----------------
For raw_input, you can also put in a prompt to show to a person so he knows what to type. Put a string that you want for the prompt inside the () so that it looks like this:
y = raw_input("Name? ")
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

raw_input(...)
    raw_input([prompt]) -> string
    
    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
input(...)
    input([prompt]) -> value
        Equivalent to eval(raw_input(prompt)).
=================================================================================================================================
Parameters, Unpacking, Variables
--------------------------------

we will cover one more input method you can use to pass variables to a script (script being another name for your .py fi les). You know how you type python ex13.py to run the ex13.py fi le? Well the ex13.py part of the command is called an “argument.” What we’ll do now is write a script that also accepts arguments.
ex 13

from sys import argv
script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

run command: python ex13_arguments.py heelo hi chai 
output:
The script is called: ex13_arguments.py
Your first variable is: heelo
Your second variable is: hi
Your third variable is: chai

Python feature set.

The argv is the “argument variable,” a very standard name in programming that you will fi nd
used in many other languages. This variable holds the arguments you pass to your Python script
when you run it.

Line 3 “unpacks” argv so that, rather than holding all the arguments, it gets assigned to four
variables you can work with: script, first, second, and third. This may look strange, but
“unpack” is probably the best word to describe what it does. It just says, “Take whatever is in
argv, unpack it, and assign it to all these variables on the left in order.”


the real name of what we are refering to feature is  module 
these are also known as liberaries

you can get errors when you donot pass enfough arguments

study drill question answer

from sys import argv

ScriptName, first, second, third = argv

print "What is your fourth variable?"
fourth = raw_input()
print "What is your fifth variable?"
fifth = raw_input()
print "What is your sixth variable?"
sixth = raw_input()

print "The script is called: ", ScriptName
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
print "Your fourth variable is: ", fourth
print "Your fifth variable is: ", fifth
print "Your sixth variable is: ", sixth

print "For your script %r, these are the variables: %r, %r, %r, %r, %r,
    and %r." % (ScriptName, first, second, third, fourth, fifth, sixth)

What’s the difference between argv and raw_input()?
The difference has to do with where the user is required to give input. If they give your script
inputs on the command line, then you use argv. If you want them to input using the keyboard
while the script is running, then use raw_input().

Are the command line arguments strings?
Yes, they come in as strings, even if you typed numbers on the command line. Use int() to con-
vert them just like with raw_input().

==================================================================================================================================================

Prompting And Passing
---------------------

ex14: prompting and passing

from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

output
------

python ex14_PromptAndPassing.py  abhishek
Hi abhishek, I'm the ex14_PromptAndPassing.py script.
I'd like to ask you a few questions.
Do you like me abhishek?
> yes
Where do you live abhishek?
> cooler
What kind of computer do you have?
> apple

Alright, so you said 'yes' about liking me.
You live in 'cooler'. Not sure where that is.
And you have a 'apple' computer. Nice.


I don’t understand what you mean by changing the prompt?
See the variable prompt = '> '. Change that to have a different value. You know this; it’s just a
string and you’ve done 13 exercises making them, so take the time to fi gure it out.


=================================================================================================================================================

Reading Files
-------------


ex15 :


1 from sys import argv  #import argv from the sys module
2 script, filename = argv #defines script and filenames are arguments
3 txt = open(raw_input(filename)) #calls a method open on the file passed as an argument
#in above line we can use open , raw_input, or open(raw_input())
4 print "Here's your file %r:" % filename #print the filename
5 print txt.read() #call the read command on the file being passed as an argument
    txt.close()
6 print "Type the filename again:" # simple print statement
7 file_again = raw_input("> ") #again ask name of the file 
8 txt_again = open(file_again) #call open method on the file name which is passed recently
9 print txt_again.read() #call read method on the file being passedrecently
    txt_again.close()


Lines 1–3 should be a familiar use of argv to get a fi lename.
line 5 where we use a new command open.

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

 read(...)
       read([size]) -> read at most size bytes, returned as a string.
       
       If the size argument is negative or omitted, read until EOF is reached.
       Notice that when in non-blocking mode, less data than what was requested
       may be returned, even if no size parameter was given.
   

Line 7 we print a little line, but on line 8 we have something very new and exciting. We call a
function on txt. What you got back from open is a file, and it’s also got commands you can
give it. You give a fi le a command by using the . (dot or period), the name of the command, and
parameters. Just like with open and raw_input. The difference is that when you say txt.read()
you are saying, “Hey txt! Do your read command with no parameters!”

argparse --- https://docs.python.org/dev/library/argparse.html

Does txt = open(filename) return the contents of the fi le?
No, it doesn’t. It actually makes something called a “fi le object.”


=================================================================================================================================================

Reading and Writing Files
-------------------------

close—Closes the fi le. Like File- >Save.. in your editor.
• read—Reads the contents of the fi le. You can assign the result to a variable.
• readline—Reads just one line of a text fi le.
• truncate—Empties the fi le. Watch out if you care about the fi le.
• write(stuff)—Writes stuff to the fi le.
ex 16 : 
from sys import argv
script, filename = argv
print "this is your script name %r" % script
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target1 = open(filename)
target2 = target1.read()
print "raw data in file \n %r" % target2
print "\n\n\n\n"
print "formatted data in file %s"%target2
target1.close()
target = open(filename, 'w')
print "Truncating the file.Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()


What does 'w' mean?
It’s really just a string with a character in it for the kind of mode for the fi le. If you use 'w', then
you’re saying “open this fi le in ‘write’ mode”—hence the 'w' character. There’s also 'r' for
“read,” 'a' for append, and modifi ers on these.
What are the modifi ers to the fi le modes we can use?
The most important one to know for now is the + modifi er, so you can do 'w+', 'r+', and 'a+'.
This will open the fi le in both read and write mode and, depending on the character used, posi-
tion the fi le in different ways.
Does just doing open(filename) open it in 'r' (read) mode?
Yes, that’s the default for the open() function.


=================================================================================================================================================

More Files
----------


ex17_morefiles.py -- program to copy one file to another

long code:
from sys import argv
from os.path import exists

script , fromfile, tofile = argv

print "copying file %s from %s" % ( fromfile, tofile)

in_file = open(fromfile, 'r')
indata  = in_file.read()

print "the input file is %d bytes long" % len(indata)
print "does the output file exist %r" % exists(tofile)

print "press ctrl+c to quit the program or Enter to continue"
raw_input("?")

out_file = open(tofile, 'w')
out_file.write(indata)

print "Allright Alldone !"

in_file.close
out_file.close

short code:

from sys import argv
script , fromfile, tofile = argv
(open(tofile, 'w')).write(((open(fromfile, 'r')).read()))


I get a Syntax:EOL while scanning string literal error.
You forgot to end a string properly with a quote. Go look at that line again.

===========================================================================================================================================

Names, Variables, Code, Functions
---------------------------------

Functions do three things:
1. They name pieces of code the way variables name strings and numbers.
2. They take arguments the way your scripts take argv.
3. Using #1 and #2, they let you make your own “mini- scripts” or “tiny commands.”

You can create a function by using the word def in Python


First we tell Python we want to make a function using def for “define.”
On the same line as def, we then give the function a name. In this case, we just called
it print_two, but it could be peanuts too. It doesn’t matter, except that your function
should have a short name that says what it does.
Then we tell it we want *args (asterisk args), which is a lot like your argv parameter but
for functions. This has to go inside () parentheses to work
Then we end this line with a : colon and start indenting.
To demonstrate how it works, we print these arguments out, just like we would in a script.


FUNCTION CHECKLIST
------------------
ex18_Function.py

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r  arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print "arg1:  %r arg2: %r" % (arg1, arg2)
    
# this will only take one argument

def print_one(arg1):
    print "arg1: %r" % arg1
    
# this will print none as no arguments

def print_no():
    print "i'm not gonna do anything"
    
print_two('zed', 'shaw')
print_two_again('abhishek', 'gautam')
print_one('abhishekGautam')
print_no()

1. Did you start your function defi nition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you “end” your function by going back to writing with no indent (dedenting we call it)?
And when you run (“use” or “call”) a function, check these things:
1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?
Use these two checklists on the remaining lessons until you do not need them anymore. Finally,
repeat this a few times: “To ‘run,’ ‘call,’ or ‘use’ a function all mean the same thing.”

What does the * in *args do?
That tells Python to take all the arguments to the function and then put them in args as a list. It’s
like argv that you’ve been using, but for functions. It’s not normally used too often unless specifi -
cally needed.

===============================================================================================================================================

Functions and Variables
-----------------------

The variables in your function are not connected to the variables in your script.
Multiple assignments
--------------------
In Python, multiple assignments can be made in a single statement as follows:
a, b, c = 5, 3.2, "Hello"

ex19_Func2.py

def cnc(chesecount, crackercount): #def keyword define we are making a function and cnc is name of func and there are 2 arguments
    print "The chese count is %d" % chesecount #simple print statement
    print "The Cracker count is %d" % crackercount #simple print statement
    print "that's enfough for party man" #simple print statement
    
cnc(10, 20) #function call 

amt_chese=20 #def var
amt_cracker=30 #def var

print "we can pass parameter in form of varibale" #print statement
cnc(amt_chese, amt_cracker) #passing arg via variable

print "we can even do maths while passing the argument" #print statement

cnc(10+30, 30+40) #passing no as arg and doing maths

print "we can combine both variables and maths" # print statement

cnc(amt_chese+10, amt_cracker+20) #arg and mix using var and maths



We can give it straight numbers. We can give it variables. We can give
it math. We can even combine math and variables.

Write at least one more function of your own design, and run it 10 different ways. pg 88

Is it bad to have global variables (like on lines 13 and 14) with the same name as function
variables?
Yes, since then you’re not quite sure which one you’re talking about. But sometimes necessity
means you have to use the same name, or you might do it on accident. Just avoid it whenever
you can.

is there a limit to the number of arguments a function can have?
It depends on the version of Python and the computer you’re on, but it is fairly large. The practical
limit, though, is about fi ve arguments before the function becomes annoying to use.

================================================================================================================================================

Functions and Files
-------------------

ex20_funcnFile.py

from sys import argv #import argv from sys liberary
script, input_file = argv #define the arg
def print_all(f): #def a func print_all
    print f.read() #print the content of filef  
def rewind(f): #def a func rewind 
    f.seek(0) #?????????????
def print_a_line(line_count, f): #def a func print_a_line which prints a line and tells line count
    print line_count, f.readline() #print a line
current_file = open(input_file) #open a file and store the file object in current_file
print "First let's print the whole file:\n" #simple print statement
print_all(current_file) #calling  a function
print "Now let's rewind, kind of like a tape." #simple read statement
rewind(current_file) #calling a func rewind
print "Let's print three lines:"
current_line = 1 #def a var and initialize it
print_a_line(current_line, current_file) #calling a func
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)


seek method
-----------
fileObject.seek(offset[, whence])

Parameters

    offset -- This is the position of the read/write pointer within the file.

    whence -- This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.

It has a “read head,” and you can “seek” this read head around the fi le to positions, then work with
it there. Each time you do f.seek(0), you’re moving to the start of the fi le. Each time you do f.readline(), you’re reading a line from the fi le and moving the read head to right after the \n that ends that fi le.

Why are there empty lines between the lines in the fi le?
The readline() function returns the \n that’s in the fi le at the end of that line. This means that
print’s \n is being added to the one already returned by readline(). To change this behavior
simply add a , (comma) at the end of print so that it doesn’t print its own \n.

Why does seek(0) not set the current_line to 0?
First, the seek() function is dealing in bytes, not lines. So that’s going to the 0 byte (fi rst byte) in
the fi le. Second, current_line is just a variable and has no real connection to the fi le at all. We
are manually incrementing it.

How does readline() know where each line is?
Inside readline() is code that scans each byte of the fi le until it fi nds a \n character, then stops
reading the fi le to return what it found so far. The fi le f is responsible for maintaining the current
position in the fi le after each readline() call, so that it will keep reading each line.
===============================================================================================================================================

Functions Can Return Something
------------------------------

ex21_fcontd.py

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
c=10
d=20
a=add(c, d)
s=sub(c, d)
m=mul(c, d)
e=div(c, d)
print a
print s
print m
print e

print "magic time"
print "can you do this your self",
print add(c, sub(c, mul(c, div(c, d))))

===============================================================================================================================================
ex22 -->learntsofar.py
===============================================================================================================================================

ex23 --> read some code
===============================================================================================================================================

Some more reading
-----------------

ex24_knowmore.py

print "Let's Know Every Thing" #simple print statement
print "you did \'t know everthing about \t tabs and \n new line of \\ charecters" #print statement with many escape charecters

poem =  """
\t twinkle twinkle 
little star \n how i wonder what you are
\t up above the sky so high 
\n\t like a twinkle in the sky
""" #defining a string in multiple line

print poem #print the poem variable

five = 10-2-6+3 #doing caltn and storing five variable

print "the result is ", five # printing a string and variable
def secret_formula(started): #def a function
jelly_beans = started * 500 #simple calc
jars = jelly_beans / 1000 #simple calc
crates = jars / 100 #simple calc
return jelly_beans, jars, crates #returning 3 values
start_point = 10000 #initializing a variable
beans, jars, crates = secret_formula(start_point) #***********Point to notice
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
start_point = start_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)#**************point to notice

=================================================================================================================================================

Even More Practice
------------------

string.split = split(s, sep=None, maxsplit=-1)
    split(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is given, splits at no more than
    maxsplit places (resulting in at most maxsplit+1 words).  If sep
    is not specified or is None, any whitespace string is a separator.
    
    (split and splitfields are synonymous)

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
(END)

list.pop = pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.

ex25_knowmore2.py

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """SORTED WORDS"""
    print "Sorted Words: ", sorted(words)
    return sorted(words)
    
def print_first_words(words):
    """ PRINT FIRST WORD AFTER POPING IT OFF"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print last word after poping it off"""
    word = words.pop(-1)
    print word

def sort_sentenses(sentense):
    """TAKE SENTENSE BREAK IT INTO WORDS AND RETURN THE SORTED SEQUENCE OF THE WORDS"""
    words = break_words(sentense)
    print words

def print_first_and_last(sentense):
    """PRINTS THE FIRST AND LAST WORDS"""
    words = break_words(sentense)
    print_first_words(words)
    print_last_word(words)

def print_first_and_last_sorted(sentense):
    """breaks the sentense and sorts the words and then print first and last"""
    words = break_words(sentense)
    word = sorted(words)
    print_first_words(word)
    print_last_word(word)

a = raw_input("Enter the String:  ")
print "PRINT FIRST AND LAST"
print_first_and_last(a)
print 'PRINT FIRST AND LAST SORTED'
print_first_and_last_sorted(a)
print 'PRINT SORTED SENTENSES'
sort_sentenses(a)
print 'SORT WORDS'
sort_words(break_words(a))


=================================================================================================================================================

in ide from ex25 import * --> import all form ex25
===============================================================================================================================================

Congratulations, Take a Test!
-----------------------------

ex26

pending

===============================================================================================================================================

Modernizing Logic
-----------------
Logic on a computer is all about seeing if some combination of these characters
and some variables is True at that point in the program. 

The Truth Tables
----------------
ex27_truthtables.py

NOT       True?
-------------------++
not  |   False True |
not  |   True False |
-------------------++
| OR     True?      |
---------------------++
True or False |  True |
True or True  |  True |
False or True |  True |
False or False|  False|
---------------------++
|AND        True?     |
-----------------------
True and False | False|
True and True  | True |
False and True | False|
False and False| False|
---------------------++----++
| NOT OR         True?      |
---------------------------++
not (True or False) | False |
not (True or True)  | False |
not (False or True) | False |
not (False or False)| True  |
---------------------------++
|NOT AND             | True?|
---------------------------++
not (True and False) | True |
not (True and True)  |False |
not (False and True) |True  |
not (False and False)| True |
-------------++------------++
|!=    |True? |
-------------++
1 != 0 | True |
1 != 1 | False|
0 != 1 | True |
0 != 0 | False|
-------------++
| ==   |True? |
-------------++
1 == 0 |False |
1 == 1 |True  |
0 == 1 |False |
0 == 0 |True  |
-------------++
================================================================================================================================================

Boolean Practise  
----------------
ex28
1. True and True
2. False and True
3. 1 == 1 and 2 == 1
4. "test" == "test"
5. 1 == 1 or 2 != 1
6. True and 1 == 1
7. False and 0 != 0
8. True or 1 == 1
9. "test" == "testing"
10. 1 != 0 and 2 == 1
11. "test" != "testing"
12. "test" == 1
13. not (True and False)
14. not (1 == 1 and 0 != 1)
15. not (10 == 1 or 1000 == 1000)
16. not (1 != 10 or 3 == 4)
17. not ("testing" == "testing" and "Zed" == "Cool Guy")
18. 1 == 1 and not ("testing" == 1 or 1 == 0)
19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)
20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

================================================================================================================================================

What If
-------
A colon at the end
of a line is how you tell Python you are going to create a new “block” of code, and then
indenting four spaces tells Python what lines of code are in that block.

ex29_if.py
people=20
cats=30
dog=15

if cats > people:
    print "Too Many Cats! the world is doomed :("
if cats < people:
    print "Very less cats! save the Cats "
if dog < people:
    print "the world is drolled"
dog += 5

if dog>=people:
    print "Both People And Dog Are Equal"
if people < dog: 
    print "People Are Less Than Dogs"
if people == dog:
    print "People are dogs"
=================================================================================================================================================

Else and if
-----------
ex30_else.py

people = 30 #def and init. a var
cars = 40 #def and init. a var
buses = 15 #def and init. a var
if cars > people: #compare cars and people
    print "We should take the cars." #if above statement is true then this wil be printed
elif cars < people: #else if statement for checking the other comparision b/w people and car
    print "We should not take the cars." #print a statement if above condtn is true
else: # if both the if present above fails then this is gonna run
    print "We can't decide." #simple print statement
if buses > cars:  #comparision b/w busses and cars
    print "That's too many buses." #simple print statement
elif buses < cars: #elseif comparision b/w  cars amd busses
    print "Maybe we could take the buses." #simple print statement
else: #else statement so that no no above condition is satisfied then this will be run
    print "We still can't decide." #print statement
if people > buses: #comparision b/w people and busses
    print "Alright, let's just take the buses." #print a message
else: #else statement 
    print "Fine, let's stay home then."

What happens if multiple elif blocks are True?
Python starts at the top and runs the fi rst block that is True, so it will run only the first one.

=================================================================================================================================================

Making Decisions
----------------

ex31_decisions.py
-----------------

print "You are in a dark room with 2 doors which one you want to enter #1 or#2?"
door = int(raw_input(">"))

if door == 1:
    print "the gaint bear is eating a chese cake here what do you do? "
    print "1. Take the cake"
    print "2. Scream at the bear"
    
    bear = int(raw_input(">"))
    if bear == 1:
        print "The bear eats your face"
    elif bear == 2:
        print "The bear eats your leg"
    else:
        print "This is %s a right option to chose "% bear
elif door == 2:
    print "you are at the endless abyss"
    print "1. blue berries"
    print "2. yellow jacket "
    print "3. Understanding revolvers around melodies"
    
    insanity = int(raw_input(">"))
    
    if insanity == 1 or insanity == 2:
        print "your body survives "
    else:
        print "your body rots"
else:
    print "You stumble around and fall on a life and die, Good Job!"
    
===================================================================================================================================================

Loops And Lists
---------------

ex32_loops_n_list.py
fruits = ['apple','mango','pineapple','gauva','grapes','blue berries']
count = [1,2,3,4,5]
change = [1, 'pennies', 2, 'demies', 3, 'quaters']

for number in count:
    print "The number is %d"%number

for fruit in fruits:
    print "The fruits is %s"%fruit
    
#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print "The value : %r"%i
    
# we can also build lists, first start with an empty one
elements = []
## then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list "%i
    elements.append(i)
# now we can print them out too
for i in elements:
    print 'the value in the list is %d'%i

@ initialize a list without using for

element = []
element = range(0, 6)
print element

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

How do you make a two- dimensional (2D) list?
That’s a list in a list like this: [[1,2,3],[4,5,6]]

How come a for- loop can use variables that aren’t defi ned yet?
It defi nes that variable, initializing it to the current element of the loop iteration, each time
through.

=================================================================================================================================================

While-Loops
-----------
A while- loop will keep
executing the code block under it as long as a boolean expression is True.
do a test like an if- statement, but instead of
running the code block once, they jump back to the “top” where the while is and repeat. It keeps
doing this until the expression is False.

usually a for loop is better than a while loop because , while loop may result in a infinite loop if the condition will never become false this is good if you want to run the loop till the end of the universe
When in doubt, print out your test variable at the top and bottom of the while- loop
to see what it’s doing.

ex33_while.py
-------------
numbers = []
i = 0

while i < 6:
    print "At the top the i is %d "%i
    numbers.append(i)
    i += 1
    print "Numbers Now ", numbers
    print "At the bottom the i is %d"%i
for i in numbers:
    print numbers[i]

def while_func(check, increment): 
    numbers = []
    i = 0
    
    while i < check:
        print "At the top the i is %d "%i
        numbers.append(i)
        i += increment
        print "Numbers Now ", numbers
        print "At the bottom the i is %d"%i
    for i in numbers:
        print numbers[i]

What’s the difference between a for- loop and a while- loop?
A for- loop can only iterate (loop) “over” collections of things. A while- loop can do any kind
of iteration (looping) you want. However, while- loops are harder to get right and you normally
can get many things done with for- loops.
================================================================================================================================================

Accessing Elements of Lists
---------------------------

Lists are good but only if we know how to acess the particular element of a list properly.
indexing is allways done from, when indexing is done from zero then such number are kwnon as cardinal elements as here we pick at random so there is a need for a zeroth index, those numbers which show some sort of ordering like who came first and all then it is known as ordinal element and such an element starts indexing from one.
Remember: ordinal == ordered, 1st; cardinal == cards at random, 0.

==============================================================================================================================================

Branches And Functions
----------------------

ex35_BranchAndFunction.py

from sys import exit

def gold_room():
    print "This room is full of fold. How much do you take?"
    next = raw_input(">")
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
    dead("Man learn to type a number")
    
    if next < 50:
        print "You are not that greedy, You Win!"
        exit(0)
    else:
        dead("you are greedy bastard")
    
def bear_room(): 
    print "there is a bear here "
    print "the bear has bunch of honey"
    print "the fat bear is in front of another door"
    print "how are you going to move the beer?"
    bear_moved= False

while True:
    next = raw_input(">")
    if next == "take honey" and bear_moved:
        print "the bear takes honey and slaps off your face"
    elif next == "taunt bear" and bear_moved:
        print "The bear has moved through door you can go now"
    elif next == "taunt bear" and not bear_moved
    dead("The bear gets pissed off and chews your leg off.")
    bear_moved=True
    elif next == "open door" and bear_moved:
        gold_room()
    else:
        print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print why, "Good job!"
    exit(0)
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
    dead("You stumble around the room until you starve.")
    start() 
What does exit(0) do?
On many operating systems, a program can abort with exit(0), and the number passed in will
indicate an error or not. If you do exit(1), then it will be an error, but exit(0) will be a good
exit. The reason it’s backward from normal boolean logic (with 0==False) is that you can use
different numbers to indicate different error results. You can do exit(100) for a different error
result than exit(2) or exit(1).    
=================================================================================================================================================

Designing and Debugging
-----------------------
EXCERCISE 36

Rules for If- Statements

1. Every if- statement must have an else.
2. If this else should never be run because it doesn’t make sense, then you must use a die
function in the else that prints out an error message and dies, just like we did in the last
exercise. This will fi nd many errors.
3. Never nest if- statements more than two deep and always try to do them one deep.
This means if you put an if in an if, then you should be looking to move that second if
into another function.
4. Treat if- statements like paragraphs, where each if, elif, else grouping is like a
set of sentences. Put blank lines before and after.
5. Your boolean tests should be simple. If they are complex, move their calculations to vari-
ables earlier in your function and use a good name for the variable.

Rules for Loops

1. Use a while- loop only to loop forever, and that means probably never. This only applies
to Python; other languages are different.
2. Use a for- loop for all other kinds of looping, especially if there is a fi xed or limited
number of things to loop over.

Tips for Debugging

1. Do not use a “debugger.” A debugger is like doing a full- body scan on a sick person. You
do not get any specifi c useful information, and you fi nd a whole lot of information that
doesn’t help and is just confusing.
2. The best way to debug a program is to use print to print out the values of variables at
points in the program to see where they go wrong.
3. Make sure parts of your programs work as you work on them. Do not write massive fi les
of code before you try to run them. Code a little, run a little, fi x a little.

=============================================================================================================================================

Symbol Review
-------------
Ex 37
Keywords
------------------------------------------------------------------------------------------------------------------------------------------------
(1)and -->The expression "x and y" first evaluates *x*; if *x* is false, its
           value is returned; otherwise, *y* is evaluated and the resulting value
           is returned.
------------------------------------------------------------------------------------------------------------------------------------------------
(2)del -->Deletion of a target list recursively deletes each target, from left
        to right. Deletion of a name removes the binding of that name  from the local or
        global namespace, depending on whether the name occurs in a "global"
        statement in the same code block.  If the name is unbound, a "NameError" exception will be raised.
        It is illegal to delete a name from the local namespace if it occurs as a free variable in a nested block.
------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------
(3)from --> for importing a specific variable, class or a function from a module
------------------------------------------------------------------------------------------------------------------------------------------------
(4)not --> The operator "not" yields "True" if its argument is false, "False" otherwise. 
------------------------------------------------------------------------------------------------------------------------------------------------
(5)while --> The "while" statement is used for repeated execution as long as an expression is true.
------------------------------------------------------------------------------------------------------------------------------------------------
(6)as --> if we want to give a module a different alias
------------------------------------------------------------------------------------------------------------------------------------------------
(7)elif -->stands for else if.If the first test evaluates to False, then it continues with the next one
------------------------------------------------------------------------------------------------------------------------------------------------
(8)global --> access variables defined outside functions
------------------------------------------------------------------------------------------------------------------------------------------------
(9)or --> If Any one is true then whole expression results in true . 
------------------------------------------------------------------------------------------------------------------------------------------------
(10)with -->with statement is used to wrap the execution of a block of code within methods defined by the context manager. 
            eg. with open('example.txt', 'w') as my_file:
               my_file.write('Hello world!')
------------------------------------------------------------------------------------------------------------------------------------------------
(11)assert -->assert is used for debugging purposes. While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. assert is followed by a condition. If the condition is true, nothing happens. But if the condition is false, AssertionError is raised. For example:
        a=4
        assert a>5
        assert a<5
------------------------------------------------------------------------------------------------------------------------------------------------
(12)else -->else is the block which is executed if the condition is false. 
------------------------------------------------------------------------------------------------------------------------------------------------
(13)if --> The "if" statement is used for conditional execution
------------------------------------------------------------------------------------------------------------------------------------------------
(14)pass --> "pass" is a null operation --- when it is executed, nothing happens. It is useful as a placeholder when a statement is required
           syntactically, but no code needs to be executed, pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder. Suppose we have a function that is not implemented yet, but we want to implement it in the future. Simply writing,
        def function(args):
in the middle of a program will give us IndentationError. Instead of this, we construct a blank body with the pass statement.
        def function(args):
            pass
We can do the same thing in an empty class as well.
class example:
    pass
------------------------------------------------------------------------------------------------------------------------------------------------
(15)yield --> yield is used inside a function like a return statement. But yield returns a generator. Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory. Generators are useful in this situation as it generates only one value at a time instead of storing all the values in memory. For example,
>>> g = (2**x for x in range(100))
will create a generator g which generates powers of 2 up to the number two raised to the power 99. We can generate the numbers using the next() function as shown below.

>>> next(g)
1
>>> next(g)
2
>>> next(g)
4
>>> next(g)
8
>>> next(g)
16
And so on… This type of generator is returned by the yield statement from a function. Here is an example.

def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)

Output
0
1
4
9
16
25
Here, the function generator() returns a generator that generates square of numbers from 0 to 5. This is printed in the for loop.
------------------------------------------------------------------------------------------------------------------------------------------------
(16)break --> break will end the smallest loop it is in and control flows to the statement immediately below the loop.
------------------------------------------------------------------------------------------------------------------------------------------------
(17)except --> The "except" clause(s) specify one or more exception handlers. When no exception occurs in the "try" clause, no exception handler    is executed. When an exception occurs in the "try" suite, a search for an exception handler is started.  This search inspects the except clauses
in turn until one is found that matches the exception.
------------------------------------------------------------------------------------------------------------------------------------------------
(18)import --> Import statements are executed in two steps: 
    (1) find a module, andinitialize it if necessary; 
    (2) define a name or names in the local namespace (of the scope where the "import" statement occurs). 
    The statement comes in two forms differing on whether it uses the "from" keyword. The first form (without "from") repeats these steps for each
    identifier in the list. The form with "from" performs step (1) once, and then performs step (2) repeatedly. Once a module name is known , 
    searching for the module or package can begin. The first place checked is "sys.modules", the cache of all modules that have been imported
    previously. If the module is found there then it is used in step (2) of import.
------------------------------------------------------------------------------------------------------------------------------------------------
(17)print --> "print" evaluates each expression in turn and writes the resulting object to standard output (see below).  If an object is not a string, it is first converted to a string using the rules for string conversions.  The (resulting or original) string is then written.  A
space is written before each object is (converted and) written, unless the output system believes it is positioned at the beginning of a
line.  This is the case (1) when no characters have yet been written to standard output, (2) when the last character written to standard
output is a whitespace character except "' '", or (3) when the last write operation on standard output was not a "print" statement. (In
some cases it may be functional to write an empty string to standard output for this reason.)
Note: Objects which act like file objects but which are not the
  built-in file objects often do not properly emulate this aspect of
  the file object's behavior, so it is best not to rely on this
------------------------------------------------------------------------------------------------------------------------------------------------
(18)class -->A class definition defines a class object. 
      classdef    ::= "class" classname [inheritance] ":" suite
      inheritance ::= "(" [expression_list] ")"
      classname   ::= identifier
        A class definition is an executable statement.  It first evaluates the inheritance list, if present. 
------------------------------------------------------------------------------------------------------------------------------------------------
(19)exec --> This statement supports dynamic execution of Python code.
------------------------------------------------------------------------------------------------------------------------------------------------
(20)in --> The in keyword has a number of uses. The two most used functions to check if a value is in a range of values, the other usage is used when traversing a tuple in a for loop.
------------------------------------------------------------------------------------------------------------------------------------------------
(21)raise --> it is used to raise exceptions.
    if num == 0:
    raise ZeroDivisionError('cannot divide')
------------------------------------------------------------------------------------------------------------------------------------------------
(22)continue -->continue causes to end the current iteration of the loop, but not the whole loop.
------------------------------------------------------------------------------------------------------------------------------------------------
(23)finally --> finally is used with try…except block to close up resources or file streams. Using finally ensures that the block of code inside it gets executed even if there is an unhandled exception. 
------------------------------------------------------------------------------------------------------------------------------------------------
(24)is --> is is used in Python for testing object identity. While the == operator is used to test if two variables are equal or not, is is used to test if the two variables refer to the same object. It returns True if the objects are identical and False if not. >>> [] == [] --> True
------------------------------------------------------------------------------------------------------------------------------------------------
(25)return --> return statement is used inside a function to exit it and return a value. If we do not return a value explicitly, None is returned automatically.
------------------------------------------------------------------------------------------------------------------------------------------------
(26)def --> def is used to define a user-defined function. Function is a block of related statements, which together does some specific task. It helps us organize code into manageable chunks and also to do some repetitive task. The usage of def is shown below:
------------------------------------------------------------------------------------------------------------------------------------------------
(27)for --> for is used for looping. Generally we use for when we know the number of times we want to loop. In Python we can use it with any type of sequence like a list or a string.
------------------------------------------------------------------------------------------------------------------------------------------------
(28)lambda --> lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned. For example:
a = lambda x: x*2
for i in range(1,6):
    print(a(i))
------------------------------------------------------------------------------------------------------------------------------------------------
(29)try --> If an error is encountered, a try block code execution is stopped and transferred down to the except block. 
------------------------------------------------------------------------------------------------------------------------------------------------

What is NameSpace?
Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

Supose we do a=2 here 2 is associated to an object named a.
Then we do a=a+1, Now a new object 3 is created and a is associated with it.
This is efficient as Python doesnt have to create a new duplicate object. This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

>>> a = 5
>>> a = 'Hello World!'
>>> a = [1,2,3]
Functions are a name to so an object can refer to them as well.

NameSpace is a collection of name. namespace can be imaginned as a mapping of each name we have defined in python to the particular object.
Different namespaces can coexist in python at any time but they are completly isolated from each other.
A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.
This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace. Due to the isolation property of name spaces the same name in different namespaces donot collide.
 local namespace is created when a function is called, which has all the names defined in it.
 
+--------------------------------------------------+
|           BUILT IN NameSpace                     | 
|   +------------------------------------------+   | 
|   |       MODULE: Global NameSpace           |   |
|   |    +--------------------------------+    |   |
|   |    | FUNCTION: Local NameSpace      |    |   |
|   |    +--------------------------------+    |   |
|   +------------------------------------------+   |
+--------------------------------------------------+

Python Variable Scope
---------------------
Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

    1.Scope of the current function which has local names
    2.Scope of the module which has global names
    3.Outermost scope which has built-in names
When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.If there is a function inside another function, a new scope is nested inside the local scope. 

Pakage --> A package can contain other packages and modules while modules cannot contain other modules or packages. From a file system
           perspective, packages are directories and modules are files.
Module:---> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.

Data Types
----------
Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.
True -->Belongs to boolean data type
False -->Belongs to boolean data type
------------------------------------------------------------------------------------------------------------------------------------------------
None --> There is another special data type — None. This data type means non existent, not known, or empty. check none.py program. 
strings --> String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' ''' or """ """ . Strings are immutable.
numbers --> Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python. We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class. eg: print(a, "is complex number?", isinstance(1+2j,complex))
------------------------------------------------------------------------------------------------------------------------------------------------
Integer --> Integers can be of any length, it is only limited by the memory available.
------------------------------------------------------------------------------------------------------------------------------------------------
floats --> A floating point number is accurate up to 15 decimal places.
------------------------------------------------------------------------------------------------------------------------------------------------
complex --> Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. ------------------------------------------------------------------------------------------------------------------------------------------------
lists --> List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.
------------------------------------------------------------------------------------------------------------------------------------------------
Tuples --> Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified. Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically. It is defined within parentheses () where items are separated by commas.
>>> t = (5,'program', 1+3j)
We can use the slicing operator [] to extract items but we cannot change its value.
t = (5,'program', 1+3j)
# t[1] = 'program'
print("t[1] = ", t[1])
# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])
# Generates error
# Tuples are immutable
t[0] = 10
------------------------------------------------------------------------------------------------------------------------------------------------
Set -->Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered . a = {5,2,3,1,4}
# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))
We can perform set operations like union, intersection on two sets. Set have unique values. They eliminate duplicates.
>>> a = {1,2,2,3,3,3}
>>> a
{1, 2, 3}
Since, set are unordered collection, indexing has no meaning. Hence the slicing operator [] does not work.
Sets are implemented in a way, which doesn't allow mutable objects. The following example demonstrates that we cannot include for example lists as elements:
>>> cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
>>> cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

Frozensets are like sets except that they cannot be changed, i.e. they are immutable:
>>> cities = frozenset(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
******************************************************************************************************************
a) add(element) --> colours.add("yellow")
b) clear(element) --> cities.clear()
c) copy --> Creates a shallow copy, which is returned. 
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
>>> cities_backup = more_cities.copy()
d)difference() --> Returns difference of two sets as new set. x.difference(y)
e) difference_update() --> The method difference_update removes all elements of another set from this set. x.difference_update(y) is the same as "x = x - y" . x.difference_update(y)
f)discard(el): An element el will be removed from the set, if it is contained in the set. If el is not a member of the set, nothing will be done.
x = {"a","b","c","d","e"}   >>> x.discard("a")
g)remove(el)--> works like discard(), but if el is not a member of the set, a KeyError will be raised. eg x.remove("a")
h)intersection(s)-->  Returns the intersection of the instance set and the set s as a new set. In other words: A set with all the elements which are contained in both sets is returned. x.intersection(y).
i)isdisjoint() -->    This method returns True if two sets have a null intersection.  
j)issubset() --> x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for "Subset of" and ">=" for "superset of"
"<" is used to check if a set is a proper subset of a set. 
K)issuperset() --> x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation for "issuperset of"
">" is used to check if a set is a proper superset of a set.
l)pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty . eg x.pop()
------------------------------------------------------------------------------------------------------------------------------------------------
Python Dictionary-->  Dictionary is an unordered collection of key-value pairs. It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value. In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.
>>> d = {1:'value','key':2}
>>> type(d)
<class 'dict'>
We use key to retrieve the respective value. But not the other way around.
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);
# Generates error
print("d[2] = ", d[2]);
------------------------------------------------------------------------------------------------------------------------------------------------
String Escape Sequences
For string escape sequences, use them in strings to make sure they do what you think they do.
• \\ --> print \
• \' --> print single quote
• \" --> print double quote
• \a --> ASCII bell
• \b --> ASCII backspace
• \f --> ASCII FormFeed
• \n --> ASCII LineFeed
• \r --> ASCII CarriageReturn
• \t --> ASCII Horizonatal Tab
• \v --> ASCII Vertical Tab
\ooo 	ASCII character with octal value ooo
\xhh... 	ASCII character with hex value hh...
-------------------------------------------------------------------------------------------------------------------------------------------------
String Formats
Same thing for string formats: use them in some strings to know what they do.
• %d --> integer number
• %i
• %o
• %u
• %x
• %X
• %e
• %E
• %f --> floating point number
• %F
• %g
• %G
• %c
• %r
• %s --> String (or any object with a string representation, like numbers)
• %%
125
Operators
Some of these may be unfamiliar to you, but look them up anyway. Find out what they do, and if
you still can’t fi gure it out, save it for later.
• +
• -
• *
• **
• /
• //
• %
• <
• >
• <=
• >=
• ==
• !=
• <>
• ( )
• [ ]
• { }
• @
• ,
• :
• .
• =
• ;
• +=
• - =
• *=
• /=
• //=
• %=
• **=
-------------------------------------------------------------------------------------------------------------------------------------------------
Doing Things to Lists
---------------------
Python List
-----------
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0. 
 Example: 
  colors = ['red', 'blue', 'green']
  print colors[0]    ## red
  print colors[2]    ## green
  print len(colors)  ## 3

CREATE A LIST
-------------
    created in [] , elements are seperated by a comma
    my_list = []    # empty list
    my_list = [1, 2, 3]    # list of integers
    my_list = [1, "Hello", 3.4]   # list with mixed datatypes
    

NOTE: A list can have another list as an element!
        eg : # such a list is called a nested list
             my_list = ["mouse", [8, 4, 6], ['a']]

INDEXING --> In python the list indexing starts from 0 but python also suports negitve indexing in which -1 means last element and -2 will mean the second last element.

How to slice lists in Python?
-----------------------------
We can access a range of items in a list by using the slicing operator (colon).
    my_list = ['p','r','o','g','r','a','m','i','z']
    print(my_list[2:5])    # elements 3rd to 5th
    print(my_list[:-5])    # elements beginning to 4th
    print(my_list[5:])     # elements 6th to end
    print(my_list[:])      # elements beginning to end
    
How to change or add elements to a list?
----------------------------------------
List are mutable, meaning, their elements can be changed unlike string or tuple.
We can use assignment operator (=) to change an item or a range of items.
odd = [2, 4, 6, 8] # mistake values
odd[0] = 1  # change the 1st item    
print(odd)  # Output: [1, 4, 6, 8]
odd[1:4] = [3, 5, 7] # change 2nd to 4th items
print(odd) # Output: [1, 3, 5, 7]
                   
We can add one item to a list using append() method or add several items using extend() method.

odd = [1, 3, 5]
odd.append(7) # Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

APPEND VS EXTEND
----------------
append: Appends object at end.
x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]

We can also use + operator to combine two lists. This is also called concatenation.
The * operator repeats a list for the given number of times.

odd = [1, 3, 5]
print(odd + [9, 7, 5]) # Output: [1, 3, 5, 9, 7, 5]
print(["re"] * 3)  #Output: ["re", "re", "re"]

we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.
odd = [1, 9]
odd.insert(1,3)
print(odd) # Output: [1, 3, 9] 
odd[2:2] = [5, 7]
print(odd) # Output: [1, 3, 5, 7, 9]

How to delete or remove elements from a list?
---------------------------------------------
We can delete one or more items from a list using the keyword del. It can even delete the list entirely.
We can use remove() method to remove the given item or pop() method to remove an item at the given index. The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).
We can also use the clear() method to empty a list

my_list = ['p','r','o','b','l','e','m']
del my_list[2]    # delete one item
print(my_list)    # Output: ['p', 'r', 'b', 'l', 'e', 'm']     
del my_list[1:5]  # delete multiple items
print(my_list)    # Output: ['p', 'm']
del my_list       # delete entire list
# my_list.clear() is an alternative way of deleting all elements of a lsit
print(my_list)    # Error: List not defined

we can also delete items in a list by assigning an empty list to a slice of elements.

>>> my_list = ['p','r','o','b','l','e','m']
>>> my_list[2:3] = []
>>> my_list
['p', 'r', 'b', 'l', 'e', 'm']
>>> my_list[2:5] = []
>>> my_list
['p', 'r', 'm']

List Membership Test
--------------------
We can test if an item exists in a list or not, using the keyword in
my_list = ['p','r','o','b','l','e','m']
print('p' in my_list) # Output: True
print('a' in my_list) # Output: False
print('c' not in my_list) # Output: True

Iterating Through a List
------------------------
Using a for loop we can iterate though each item in a list.
for fruit in ['apple','banana','mango']:
    print("I like",fruit)

Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory. 
+=====================================================================================+
|    COLORS =====> |red|blue|green| (intiallly)                                       |
|-------------------------------------------------------------------------------------|
|   b= colors                                                                         |
|                                                                                     |
|   COLORS =====> |red|blue|green| (both variables now point to the same list)        |
|                        ^                                                            |
|                        |                                                            |
|                        b(now b will also point to the list)                         |
|                                                                                     |              
+=====================================================================================+
The "empty list" is just an empty pair of brackets [ ]. The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).

FOR and IN
----------

Python *for* and *in* constructs are extremely useful, and the first use of them we will see is with lists. The *for* construct -- for var in list -- is an easy way to look at each element in a list (or other collection). Do not add or remove from the list during iteration.

  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum 
 
 list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print 'yay'
    
Built-in Functions with List 
----------------------------
Function 	Description
all()    	Return True if all elements of the list are true (or if the list is empty).
any()    	Return True if any element of the list is true. If the list is empty, return False.
enumerate()  	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()    	    Return the length (the number of items) in the list.
list()   	Convert an iterable (tuple, string, set, dictionary) to a list.
max() 	    Return the largest item in the list.
min() 	    Return the smallest item in the list
sorted()     	Return a new sorted list (does not sort the list itself).
sum() 	    Return the sum of all elements in the list. 

ex38_list.py

ten_things = "Apple Oranges Crows Sugar Light Telephone"
print "Wait! There is Not 10 Tings In The List Let's Fix This"
stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding next one !", next_one
    stuff.append(next_one)
    print "There are %d elements in the list right now"%len(stuff)
print "There we go ", stuff
print "Let's do something with stuff"
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)     # cool!
print "#".join(stuff[3:6]) #super cool but how # comes between the words
print "#".join(stuff[3:5]) #how in opuput # comes in between the two words

================================================================================================================================================
Dictionaries, Oh Lovely Dictionaries
------------------------------------
In other Languages it is called as Hashes. A dict associate one thing to another no matter what it is. 
Eg. >>>stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
    >>>print stuff['name']
    Zed
del d[key] --> it is used to delete a element from list.

# empty dictionary
my_dict = {}
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
Aceessing elements of dictionary
--------------------------------
To access any element of dictionary we can use key . Key can be used either inside square brackets or with the get() method.
print(my_dict['name'])
print(my_dict.get('age'))  #If we try to acess those keys which don't exist then it will generate an error.

Insertion Of Elements
---------------------
Dictionary are mutable. We can add new items or change the value of existing items using assignment operator. If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
my_dict['address'] = 'Downtown'  
Deletion Of Elements
--------------------
We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value. The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method. We can also use the del keyword to remove individual items or the entire dictionary itself.

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
# remove a particular item
print(squares.pop(4))  
# Output: 16
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
# remove an arbitrary item
print(squares.popitem())
# Output: (1, 1)
print(squares)
# Output: {2: 4, 3: 9, 5: 25}
# delete a particular item
del squares[5]  
print(squares)
# Output: {2: 4, 3: 9}
# remove all items
squares.clear()
print(squares)
# Output: {}
# delete the dictionary itself
del squares
# Throws Error
# print(squares)

Python Dictionary Methods
-------------------------
Method 	                    Description
clear() 	        Remove all items form the dictionary.
copy() 	            Return a shallow copy of the dictionary.
fromkeys(seq[, v]) 	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d]) 	    Return the value of key. If key doesnot exit, return d (defaults to None).
items() 	        Return a new view of the dictionary's items (key, value).
keys() 	            Return a new view of the dictionary's keys.
pop(key[,d]) 	    Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises    KeyError.
popitem() 	        Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d]) If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other]) 	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values() 	        Return a new view of the dictionary's values

Python Dictionary Comprehension
-------------------------------
Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python. Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.
Eg: squares = {x: x*x for x in range(6)}
            # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(squares)

A dictionary comprehension can optionally contain more for or if statements. An optional if statement can filter out items to form the new dictionary.
    odd_squares = {x: x*x for x in range(11) if x%2 == 1}
    # Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    print(odd_squares)
    
Dictionary Membership Test
--------------------------
We can test if a key is in a dictionary or not using the keyword in. Notice that membership test is for keys only, not for values.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)
Iterating Through a Dictionary
------------------------------
Using a for loop we can iterate though each key in a dictionary.
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

Built-in Functions with Dictionary
----------------------------------
Function 	Description
all()    	Return True if all keys of the dictionary are true (or if the dictionary is empty).
any() 	    Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len() 	    Return the length (the number of items) in the dictionary.
cmp() 	    Compares items of two dictionaries.
sorted()    Return a new sorted list of keys in the dictionary.

What the difference between a list and a dictionary?
A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called “keys”)
to other items (called “values”).

Ex39_Dictionary.py
# create a mapping of state to abbreviation
states = [
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
]


# create a basic set of states and some cities in them
cities = [
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
]
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '- ' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
# print some states
print '- ' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
# do it by using the state then cities dict
print '- ' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
# print every state abbreviation
print '- ' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
# print every city in state
print '- ' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
state, abbrev, cities[abbrev])
print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas."
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

What would I use a dictionary for?
Use it any time you have to take one value and “look up” another value. In fact, you could call dictionaries “look up tables.”

What if I need a dictionary, but I need it to be in order?
Take a look at the collections.OrderedDict data structure in Python. Search for it online to fi nd the documentation.
==================================================================================================================================================
Modules, Classes, and Objects
-----------------------------
There is a construct in python called classes which lets you structure your program in a partivular way.
**Modules Are Like Dictionaries
**Classes Are Like Modules --> Classes are like blueprints or defi nitions for creating new mini- modules
A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the '.' (dot) operator.
**Objects Are Like Mini- Imports --> When you instantiate a class, what you get is called an object. Instantiation is how you make one of these mini- modules and import it at the same time. The resulting created mini- module is called an object and you then assign it to a vari-
able to work with it. The way you do this is you call the class like it’s a function, like this:
    thing = MyStuff()
    thing.apple()
    print thing.tangerine
A Python class starts with the reserved word class, followed by the class name. A class name is mostly Capatalized but this is just a conventiona and not an requirement.Python classes donot have explicit constructors and destructors. Python classes do have something similar to a constructor: the __init__ method. 

Getting Things from Things
--------------------------
I now have three ways to get things from things:
mystuff['apples'] # dict style
mystuff.apples() # module style
print mystuff.tangerine
thing = MyStuff()# class style
thing.apples()
print thing.tangerine

ex40_classes.py
class song(object):
    def __init__(self, lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])        
bulls_on_parade = song(["They rally arounf the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

Why do I need self when I make __init__ or other functions for classes?
If you don’t have self, then code like cheese = 'Frank' is ambiguous. That code isn’t clear
about whether you mean the instance’s cheese attribute or a local variable named cheese. With
self.cheese = 'Frank' it’s very clear you mean the instance attribute self.cheese.
EXAMPLE OF DEF OF A CLASS
-------------------------
from UserDict import UserDict
class FileInfo(UserDict):
the ancestor of a class is simply listed in parentheses immediately after the class name. So the FileInfo class is inherited from the UserDict class . Python does not have any special word like java has extends. Python supports multiple inheritance so in parenthesis you can place as many ancestors as you want each seperated by a comma. A class creates a new local namespace where all its attributes are defined. Attributes may be data or functions.There are also special attributes in it that begins with double underscores (__). For example, __doc__ gives us the docstring of that class.print(MyClass.__doc__)--> it is what we write in the first line of class as a string. it is the metadata for a class
INITIALIZING AND CODING CLASSES
-------------------------------
class FileInfo(UserDict):
    "store file metadata"              1
    def __init__(self, filename=None): 2 3 4
1. Class can and should have a doc string just like modules or functions.
2. __init__ is imediately called as soon as the instance of class is created. it is not at all similar to constructers because by the time the __inti__ method was called the object we allready have a valid reference to it. 
3. The first argument of every class method, including __init__, is always a reference to the current instance of the class. By convention, this argument is always named self. In the __init__ method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called. Although you need to specify self explicitly when defining the method, you do not specify it when calling the method; Python will add it for you automatically.
4. __init__ methods can take any number of arguments, and just like functions, the arguments can be defined with default values, making them optional to the caller. In this case, filename has a default value of None, which is the Python null value. 

self is not a reserve keyword it is just the convention and a very strong one.
EXAMPLE: 
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)
# Call getData() function
# Output: 2+3j
c1.getData()
# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10
# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))
# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
c1.attr

CODE THE FILE INFO CLASS
------------------------
class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)        1
        self["name"] = filename        2
                                       3
1. 	Some pseudo-object-oriented languages like Powerbuilder have a concept of “extending” constructors and other events, where the ancestor's method is called automatically before the descendant's method is executed. Python does not do this; you must always explicitly call the appropriate method in the ancestor class.
2. 	I told you that this class acts like a dictionary, and here is the first sign of it. You're assigning the argument filename as the value of this object's name key.
3. 	Note that the __init__ method never returns a value.  	

KNOWING WHEN TO USE __init__ AND WHEN TO USE SELF
-------------------------------------------------
When defining your class methods, you must explicitly list self as the first argument for each method, including __init__.  When you call a method of an ancestor class from within your class, you must include the self argument. But when you call your class method from outside, you do not specify anything for the self argument. __init__ methods are optional, but when you define one, you must remember to explicitly call the ancestors __init__ method (if it defines one). This is more generally true: whenever a descendant wants to extend the behavior of the ancestor, the descendant method must explicitly call the ancestor method at the proper time, with the proper arguments. 

Creating an Object in Python
----------------------------
An object itself can be used to create a new instance object of a class. for eg:    ob = MyClass(). Method of an object are corresponding function of class. This means to say, since MyClass.func is a function object (attribute of class), ob.func will be a method object. While calling the func with object we need not pass self becuase whenever an object calls its method, the object itself is passed as the first argument. So, ob.func() translates into MyClass.func(ob).For this reason the first argument of the func in class must be object itslef. 

Deleting Attributes and Objects
-------------------------------
Any attribute(methods and variables) of any object can be deleted anytime using the del attribute.
>>> c1 = ComplexNumber(2,3)
>>> del c1.imag
>>> c1.getData()
Traceback (most recent call last):
AttributeError: 'ComplexNumber' object has no attribute 'imag'
>>> del ComplexNumber.getData
>>> c1.getData()
Traceback (most recent call last):
AttributeError: 'ComplexNumber' object has no attribute 'getData'
We can even delete the object itself, using the del statement.
>>> c1 = ComplexNumber(1,3)
>>> del c1
>>> c1
Traceback (most recent call last):
NameError: name 'c1' is not defined
It is a bit complex here as when we do the del c1 then the binding is removed b/w c1 and object in memeory and c1 is deleted from the namspecae but the object continue to exist in memory which is later automatically destroyed.
================================================================================================================================================
Learning to Speak Object Oriented
---------------------------------
Word Drills
1)class—Tell Python to make a new kind of thing.
2)object—Two meanings: the most basic kind of thing, and any instance of some thing.
3)instance—What you get when you tell Python to create a class.
4)def—How you defi ne a function inside a class.
5)self—Inside the functions in a class, self is a variable for the instance/object being accessed.
6)inheritance—The concept that one class can inherit traits from another class, much like you and your parents.
7)composition—The concept that a class can be composed of other classes as parts, much like how a car has wheels.
8)attribute—A property classes have that are from composition and are usually variables.
8)is-a — A phrase to say that something inherits from another, as in a “salmon” is- a “fi sh.”
9)has-a — A phrase to say that something is composed of other things or has a trait, as in “a salmon has- a mouth.”

Phrase Drills
class X(Y)--> “Make a class named X that is- a Y.”
class X(object): def __init__(self, J) --> “class X has- a __init__ that takes self and J parameters.”
class X(object): def M(self, J) --> “class X has- a function named M that takes self and J parameters.”
foo = X() --> “Set foo to an instance of class X.”
foo.M(J) --> “From foo get the M function, and call it with parameters self, J.”
foo.K = Q --> “From foo get the K attribute, and set it to Q.”

ex41_oop.py
-----------
import random
from urllib import urlopen
/*urllib --> This module provides a high-level interface for fetching data across the World Wide Web
/*urlopen() -->  the urlopen() function is similar to the built-in function open(), but accepts Universal Resource Locators (URLs) instead of filenames. Some restrictions apply — it can only open URLs for reading, and no seek operations are available.
/*urllib.urlopen = urlopen(url, data=None, proxies=None, context=None)
    Create a file-like object for the specified URL to read from.

import sys
/* sys --> This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

/* strip() -->The method strip() returns a copy of the string in which all chars have been stripped from the beginning and the end of the string (default whitespace characters).
/*string.strip = strip(s, chars=None)
    strip(s [,chars]) -> string
/*str.strip([chars]);

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
/*sample(self, population, k) method of random.Random instance
    Chooses k unique random elements from a population sequence.
    
    Returns a new list containing elements from the population while
    leaving the original population unchanged.  The resulting list is
    in selection order so that all sub-slices will also be valid random
    samples.  This allows raffle winners (the sample) to be partitioned
    into grand prize and second place winners (the subslices).
    
    Members of the population need not be hashable or unique.  If the
    population contains repeats, then each occurrence is a possible
    selection in the sample.
    
    To choose a sample in a range of integers, use xrange as an argument.
    This is especially fast and space efficient for sampling from a
    large population:   sample(xrange(10000000), 60)
*/
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"

What does result = sentence[:] do?
That's a Python way of copying a list. You're using the list slice syntax [:] to effectively make a slice from the very first element to the very last one.
=================================================================================================================================================
Is- A, Has- A, Objects, and Classes
-----------------------------------
Is-A is used when we talk about objects objects and classes being related to each other by a class relationship. You use
has- a when you talk about objects and classes that are related only because they reference each other.
What does super(Employee, self).__init__(name) do? That’s how you can run the __init__ method of a parent class reliably. Go search for “python super” and read the various advice on it being evil and good for you.
ex42_is_a_has_a.py
#Animal is an Object
class Animal(object):
    pass
#Dog is an Animal
class Dog(Animal):
    def __init__(self,name):
        #Dog HAS-A Name
        self.name = name
#cat is an Animal
class Cat(Animal):
    def __init__(self,name):
        #Cat Has-A Name
        self.name = name
#person is a object
class Person(object):
    def __init__(self,name):
        #person Has-A Name
        self.name = name
        #Person has a pet of somekind
        self.pet = None
#Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        #
        super(Employee,self).__init__(name)
        #Employee has a salary 
        self.salary = salary
#class Fish is a object
class Fish(object):
    pass
#Salmon is a fish
class Salmon(Fish):
     pass
#Halibut is a fish
class Halibut(Fish):
    pass
#rover is a dog
rover = Dog("Rover")
#satan is a cat
satan = Cat("Satan")
#mary is a person
mary = Person("mary")
#mary has a pet which is satan
mary.pet=satan
#Frank is a Employee whose salary 120000
frank = Employee("Frank",120000)
#frank has a pet which is rover
frank.pet=rover
flipper = Fish()
course = Salmon()
harry = Halibut()
=================================================================================================================================================
Basic Object- Oriented Analysis and Design
------------------------------------------

The process is as follows:
1. Write or draw about the problem.
2. Extract key concepts from #1 and research them.
3. Create a class hierarchy and object map for the concepts.
4. Code the classes and a test to run them.
5. Repeat and refine.

Allways solve a problem in a top-down approach i.e. start from the very abstract, loose idea and slowly refines it untill the idea is solid and something you can code.
Allways try to draw daigrams or maps to solve a particular problem. After than analyize these daigrams and identify the key concpets. Simply make a list of all the nouns and verbs in your writing and drawings, then write out how they’re related. This gives me a good list of names for classes, objects, and functions in the next step.Then try to obtain the relationships between the classes so that you get a class heirarchy . if you have any problem in any part of the process then start all over again and rethink. 

ANALYISIS OF A GAME
-------------------
Here we are going to make a small game “Gothons from Planet Percal #25”. it is an adventure based game. 
Write or Draw about the Problem
-------------------------------
I’m going to write a little paragraph for the game:
“Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating
them so he can escape into an escape pod to the planet below. The game will be more like a Zork
or Adventure type game with text outputs and funny ways to die. The game will involve an engine
that runs a map full of rooms or scenes. Each room will print its own description when the player
enters it and then tell the engine what room to run next out of the map.”

DEATH : This iis when the player dies and it should be something funny.
CENTRAL CORIDOR : this is the starting point and a gothon is allready stannding there with the player has defeat with a joke.
LASER WEAPON ARMY: this is where the hero gets neutron bomb to blow up the ship before entering the escape pod.it has a keypad and he has to guess a number for it. 
THE BRIDGE: another battle scene eith gothon where the hero has to place the bomb.
ESCAPE POD: where the hero escape but only after guessesing the right pod.

EXTRACT KEY TERMS AND RESEARCH THEM
-----------------------------------
List of NOUNS: 
--------------
• Alien
• Player
• Ship
• Maze
• Room
• Scene
• Gothon
• Escape Pod
• Planet
• Map
• Engine
• Death
• Central Corridor
• Laser Weapon Armory
• The Bridge
for the research part I may play a few similar games so that i know how these games work. research about the ships and the bombs or study about some techincal issues like how to store a gamestate in the database.

CREATE A CLASS HERIRARCHY AND OBJECT MAP FOR THE CONCEPTS: 
----------------------------------------------------------
turn it into a class hierarchy by asking, “What is similar to other things?” I also ask, “What is basically just another word for another thing?”
Room and Scene are same thing-->Pick(scene)
Central Coridor is a special room which just becomes a scene.
Death is also a scene
maze and map are some --> pick(map)
planet can also be another scene instead of something specific
The class heirarchy is as follows:
* Map
* Engine
* Scene
    ** Death
    ** Central Corridor
    ** Laser Weapon Armory
    ** The Bridge
    ** Escape Pod
Now based on verbs we can go through each classes and see what nessesary actions are required.
* Map
    - next_scene
    - opening_scene
* Engine
    - play
* Scene
    - enter
    * Death
    * Central Corridor
    * Laser Weapon Armory
    * The Bridge
    * Escape Pod
we will inherit enter and overide it the child classes.

CODE THE CLASSES AND A TEST TO RUN THEM
---------------------------------------

