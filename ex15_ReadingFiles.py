
from sys import argv  #import argv from the sys module
script, filename = argv #defines script and filenames are arguments
txt = open(filename) #calls a method open on the file passed as an argument
print "Here's your file %r:" % filename #print the filename
print txt.read() #call the read command on the file being passed as an argument
txt.close()
print "Type the filename again:" # simple print statement
file_again = raw_input("> ") #again ask name of the file 
txt_again = open(file_again) #call open method on the file name which is passed recently
print txt_again.read() #call read method on the file being passedrecently
txt_again.close()

