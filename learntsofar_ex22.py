print -->print evaluates each expression in turn and writes the resulting object to standard output. If an object is not a string,
it is first converted to a string using the rules for string
conversions. A "'\n'" character is written at the end, unless the "print" statement ends with a comma.

# --> Anything you write after this will become a comment

+ plus, also used for concatenating two strings
- minus
/ slash
* asterisk
** --> exponent operator, a**b --> a raised to power b
^ --> binary XOR of two numbers
// --> perform interger divison which is different from division in other languages, since it rounds towards negative infinity, rather than towards zero.
% percent
< less- than
> greater- than
<= less- than- equal
>= greater- than- equal
x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 

float() --> converts to float

int() --> converts to int

if <conditn>: --> defines an if conditionn

elif <condition>: --> equivalent to else if

else --> if "if" condition fails then this comes to role

<variable_name> = a way of defining a variable in python , since python is a dynamic programming language so there is no type decleration required in python.

% -> modulus operator(prints the remainder of the devision performed)
       https://docs.python.org/3/reference/expressions.html

d 	Signed integer decimal. 	
i 	Signed integer decimal. 	
o 	Unsigned octal. 	(1)
u 	Unsigned decimal. 	
x 	Unsigned hexadecimal (lowercase). 	(2)
X 	Unsigned hexadecimal (uppercase). 	(2)
e 	Floating point exponential format (lowercase). 	
E 	Floating point exponential format (uppercase). 	
f 	Floating point decimal format. 	
F 	Floating point decimal format. 	
g 	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise. 	
G 	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise. 	
c 	Single character (accepts integer or single character string). 	
r 	String (converts any python object using repr()). 	(3)
s 	String (converts any python object using str()). 	(4)
% 	No argument is converted, results in a "%" character in the result. 

string --> allways defined inside single or double quotes  https://docs.python.org/3/library/string.html
            whitespace -- a string containing all characters considered whitespace
    lowercase -- a string containing all characters considered lowercase letters
    uppercase -- a string containing all characters considered uppercase letters
    letters -- a string containing all characters considered letters
    digits -- a string containing all characters considered decimal digits
    hexdigits -- a string containing all characters considered hexadecimal digits
    octdigits -- a string containing all characters considered octal digits
    punctuation -- a string containing all characters considered punctuation
    printable -- a string containing all characters considered printable

, --> stops line termination

""" --> using this we can
define our string in multiple line and it will consider our own formatting and no formatting will be performed by the python"""

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


raw_input --> it is a input function which takes input from user and return it in the string format, later we can apply functions like int(), float() to make changes in it. raw_input([prompt]) -> string

input() --> this function was included in python 3 but this function is not secure as it considers everything as python code and executes every input  input([prompt]) -> value

argv --> It means arguments vector and it contains the arguments passed to the program. The first one is always the program name.

open() : used to open a file and we can define various mode such as read mode , write mode in which we want to open the file, 
    open(name[, mode[, buffering]]) -> file object

read() --> used to read the content of a file , <filename>.read()

file.read = read(...)
    read([size]) -> read at most size bytes, returned as a string.
    If the size argument is negative or omitted, read until EOF is reached.
    Notice that when in non-blocking mode, less data than what was requested
    may be returned, even if no size parameter was given

file.write() --> file.write = write(...)
    write(str) -> None.  Write string str to file.
    
    Note that due to buffering, flush() or close() may be needed before
    the file on disk reflects the data written
    
 file.trunctate() --> file.truncate = truncate(...)
    truncate([size]) -> None.  Truncate the file to at most size bytes.
    
    Size defaults to the current file position, as returned by tell().

file.tell = tell(...)
    tell() -> current file position, an integer (may be a long integer).
    
file.close --> ile.close = close(...)
    close() -> None or (perhaps) an integer.  Close the file.
    
    Sets data attribute .closed to True.  A closed file cannot be used for
    further I/O operations.  close() may be called more than once without
    error.  Some kinds of file objects (for example, opened by popen())
    may return an exit status upon closing.
    
file.flush --> file.flush = flush(...)
    flush() -> None.  Flush the internal I/O buffer.
    ere's typically two levels of buffering involved:

Internal buffers AND Operating system buffers

The internal buffers are buffers created by the runtime/library/language that you're programming against and is meant to speed things up by avoiding system calls for every write. Instead, when you write to a file object, you write into its buffer, and whenever the buffer fills up, the data is written to the actual file using system calls.

However, due to the operating system buffers, this might not mean that the data is written to disk. It may just mean that the data is copied from the buffers maintained by your runtime into the buffers maintained by the operating system.

If you write something, and it ends up in the buffer (only), and the power is cut to your machine, that data is not on disk when the machine turns off.

So, in order to help with that you have the flush and fsync methods, on their respective objects.

The first, flush, will simply write out any data that lingers in a program buffer to the actual file. Typically this means that the data will be copied from the program buffer to the operating system buffer.

Specifically what this means is that if another process has that same file open for reading, it will be able to access the data you just flushed to the file. However, it does not necessarily mean it has been "permanently" stored on disk.

To do that, you need to call the os.fsync method which ensures all operating system buffers are synchronized with the storage devices they're for, in other words, that method will copy data from the operating system buffers to the disk.

Typically you don't need to bother with either method, but if you're in a scenario where paranoia about what actually ends up on disk is a good thing, you should make both calls as instructed.

===============================================================================================================================================

* -->operator to unpack the arguments out of a list or tuple

def --> used to define a funcion  function definition is an executable statement.  Its execution binds
the function name in the current local namespace to a function object
(a wrapper around the executable code for the function).  This
function object contains a reference to the current global namespace
as the global namespace to be used when the function is called.

The function definition does not execute the function body; this gets
executed only when the function is called. It is also possible to create anonymous functions (functions not bound
to a name), for immediate use in expressions.  This uses lambda expressions. 

seek method
-----------
fileObject.seek(offset[, whence])


file.readline() : reads a line until the \n charecter is not encountered


