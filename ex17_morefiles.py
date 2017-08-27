from sys import argv
from os.path import exists

script , fromfile, tofile = argv

print "copying file %s from %s" % ( tofile, fromfile)

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


