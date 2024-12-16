from helpers import Constants
class Player:
    def __init__(self, name=Constants.defaultPlayerName, bankroll=Constants.defaultInitialAmount):
        self.name = name
        self.hand = []
        self.bankroll = bankroll
        self.total = 0