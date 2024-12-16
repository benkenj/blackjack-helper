
from entities.suit import Suit

class Card:
    def __init__(self, suit=Suit, name=str):
        self.__suit = suit
        self.__name = name
        self.hide = False

    def getSuit(self) -> Suit:
        return self.__suit
    
    def getName(self) -> str:
        return self.__name

    

    
        
