import './card.py'

class Deck:
    def __init__(self, wildVal):
        self.store = self.populate(wildVal)
        self.store.shuffle()

    def deal(self, hand):
        hand.addCard(self.store.pop())
    
    def populate(self, wildVal):
        values = ['3', '4', '5', '6', '7', '8', ' 9', '10', '11', '12', '13']
        suits = ['Stars', 'Clubs', 'Diamonds', 'Spades', 'Hearts']
        values = values.remove(wildVal)
        cards = []
        for suit in suits:
            cards.append(Card(wildVal, suit, True))
            for value in values:
                cards.append(Card(value, suit))
        cards += cards
        for _ in range(6):
            cards.append(Card('*', 'Joker', True))
        return cards