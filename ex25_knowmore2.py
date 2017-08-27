def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """SORTED WORDS"""
    print "Sorted Words: ", sorted(words)
    return sorted(words)
    
def print_first_words(words):
    """ PRINT FIRST WORD AFTER POPING IT OFF"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print last word after poping it off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentense):
    """TAKE SENTENSE BREAK IT INTO WORDS AND RETURN THE SORTED SEQUENCE OF THE WORDS"""
    words = break_words(sentense)
    print words

def print_first_and_last(sentense):
    """PRINTS THE FIRST AND LAST WORDS"""
    words = break_words(sentense)
    print_first_words(words)
    print_last_word(words)

def print_first_and_last_sorted(sentense):
    """breaks the sentense and sorts the words and then print first and last"""
    words = break_words(sentense)
    word = sorted(words)
    print_first_words(word)
    print_last_word(word)

a = raw_input("Enter the String:  ")
print "PRINT FIRST AND LAST"
print_first_and_last(a)
print 'PRINT FIRST AND LAST SORTED'
print_first_and_last_sorted(a)
print 'PRINT SORTED SENTENSES'
sort_sentence(a)
print 'SORT WORDS'
sort_words(break_words(a))
