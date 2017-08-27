fruits = ['apple','mango','pineapple','gauva','grapes','blue berries']
count = [1,2,3,4,5]
change = [1, 'pennies', 2, 'demies', 3, 'quaters']

for number in count:
    print "The number is %d"%number

for fruit in fruits:
    print "The fruits is %s"%fruit
    
#also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print "The value : %r"%i
    
# we can also build lists, first start with an empty one
elements = []
## then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list "%i
    elements.append(i)
# now we can print them out too
for i in elements:
    print 'the value in the list is %d'%i
