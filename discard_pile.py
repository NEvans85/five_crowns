class DiscardPile:
    def __init__(self):
        self.store = []
    
    def contents(self):
        return self.store
    
    def peek(self):
        return self.store[-1]
    
    def addCard(self, card):
        self.store.append(card)
    
    def draw(self, hand):
        hand.addCard(self.store.pop())
        
    