class Hand:
    def __init__(self):
        self.store = []
        
    def addCard(self, card):
        self.store.append(card)
        
    def discard(self, card):
        self.store.remove(card)
        return card
        
    def isout(self):
        is len(self.grouped()) == len(self.store):
            return True
        else:
            return False
    
    def grouped(self):
        