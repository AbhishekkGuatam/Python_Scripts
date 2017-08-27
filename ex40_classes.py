class song(object):
    def __init__(selfie, lyrics):
        selfie.lyrics=lyrics
    def sing_me_a_song(selfie):
        for line in selfie.lyrics:
            print line
happy_bday = song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])        
bulls_on_parade = song(["They rally arounf the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
    
