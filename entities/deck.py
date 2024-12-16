from typing import List
from helpers.cardHelper import CardHelper
from entities.card import Card
class Deck:
    N_CARDS = 52

    def __init__(self):
        self.__cards = []
        for name in CardHelper.names:
            for suit in CardHelper.suits:
                self.__cards.append(Card(suit,name))
    
    def getCards(self) -> List[Card]:
        return self.__cards
    


    '''
    draw
    shuffle
    ncardsleft
    '''