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
