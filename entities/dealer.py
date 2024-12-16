from helpers import Constants
class Dealer():
    def __init__(self, name=Constants.defaultDealerName):
        self.name = name
        self.hand = []
        self.total = 0