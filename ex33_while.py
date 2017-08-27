numbers = []
i = 0

while i < 6:
    print "At the top the i is %d "%i
    numbers.append(i)
    i += 1
    print "Numbers Now ", numbers
    print "At the bottom the i is %d"%i
for i in numbers:
    print i

def while_func(check): 
    numbers = []
    i = 0
    
    while i < check:
        print "At the top the i is %d "%i
        numbers.append(i)
        i += 1
        print "Numbers Now ", numbers
        print "At the bottom the i is %d"%i
    for i in numbers:
        print numbers[i]
        
while_func(5)

