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
