import './round.py'
import './player.py'

class Game:
    def __init__(self, players):
        self.players = players
        self.score = {}
        for player in self.players:
            self.score[player] = 0
    
    