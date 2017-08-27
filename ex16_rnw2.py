
from sys import argv
script , filename = argv
print "This Program wil erase all contennt of selected file %r"%filename
print "To Continue press ENTER and to Quit press "
raw_input("?")
print "opening file"
target=open(filename, 'w')
target.truncate()

print "The Content of %r file deleted"%filename
print "Now this part of program will attempt to rewrite the contents back into the file"
print "To Continue press ENTER and to Quit press "
raw_input("?")

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")
line = line1+"\n"+line2+"\n"+line3
print "\n Now we gonna write these lines in you file using write method"
target.write(line1+"\n"+line2+"\n"+line3)
# target.write(line)

print "Now we close the file"
target.close()

