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
