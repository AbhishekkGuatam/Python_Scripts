def cnc(chesecount, crackercount):
    print "The chese count is %d" % chesecount
    print "The Cracker count is %d" % crackercount
    print "that's enfough for party man"
    
cnc(10, 20)

amt_chese=20
amt_cracker=30

print "we can pass parameter in form of varibale"
cnc(amt_chese, amt_cracker)

print "we can even do maths while passing the argument"

cnc(10+30, 30+40)

print "we can combine both variables and maths"

cnc(amt_chese+10, amt_cracker+20)


