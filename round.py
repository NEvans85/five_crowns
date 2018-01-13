import './deck.py'

class Round:
    def __init__(self, rdNum, players):
        self.rdNum = rdNum
        self.players = players
        self.deck = Deck()
    
    
    