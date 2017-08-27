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
 
