from sys import argv
script, filename = argv

def print_all(f):
    print f.read()

def rewind(f):
    print f.seek(0)
    
def print_a_line(linecount, f):
    print linecount, f.readline()
 
target = open(filename , 'r')

print "Let's print the whole file"
print_all(target)

print "Let's do a lil bit of rewind"
rewind(target)

current_line = 1
print_a_line(current_line, target)
current_line=current_line+1
print_a_line(current_line, target)
current_line= current_line+1


 
