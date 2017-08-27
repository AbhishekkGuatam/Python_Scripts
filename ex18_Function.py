# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r  arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print "arg1:  %r arg2: %r" % (arg1, arg2)
    
# this will only take one argument

def print_one(arg1):
    print "arg1: %r" % arg1
    
# this will print none as no arguments

def print_no():
    print "i'm not gonna do anything"
    
print_two('zed', 'shaw')
print_two_again('abhishek', 'gautam')
print_one('abhishekGautam')
print_no()

