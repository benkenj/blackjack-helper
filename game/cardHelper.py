from card import Card
from suit import Suit
class CardHelper:
    faceCards = ['10', "J", "Q", "K"]
    names = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    ace = "A"
    suits = [Suit.SPADE, Suit.HEART, Suit.DIAMOND, Suit.CLUB]

    @staticmethod
    def isFaceCard(card=Card):
        for f in card.faceCards:
            if card.name == f:
                return True
        return False
    
    @staticmethod
    def isAce(card):
        return card.name == card.ace
    
    @staticmethod
    def nameToValue(card=Card):
        if card.name.isnumeric():
            return int(card.name)
        elif card.name == "A":
            return 11
        else:
            return 10



        