
from deck import Deck
from card import Card
import random
class Shoe:
    def __init__(self, nDecks=int, penetration=1.0):
        self.__nDecks = nDecks
        self.__penetration = penetration # TODO make this configurable
        self.__nCards = nDecks * Deck.N_CARDS
        self.__cardsDealt = 0
        self.__shoe = []

        self.reset()

    def reset(self):
        self.__cardsDealt = 0
        self.__shoe = []
        deckCards = Deck().getCards()
        for _ in range(self.__nDecks):
            for c in deckCards:
                self.__shoe.append(c)

    def shuffle(self):
        self.reset()
        random.shuffle(self.__shoe)

    def draw(self) -> Card:
        card = self.__shoe.pop()
        self.__cardsDealt += 1
        return card
    

    def getCardsRemaining(self):
        return int(self.__penetration * self.__nCards) - self.__cardsDealt
    
    def getCardsDealt(self):
        return self.__cardsDealt
    
    def getPenetration(self):
        return self.__penetration
    
    def shouldShuffle(self):
        if (self.__cardsDealt / self.__nCards) > self.getPenetration():
            return True
        return False

    
