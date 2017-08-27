
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
        elif next == "taunt bear" and not bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
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
