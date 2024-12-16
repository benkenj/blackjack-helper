from entities import Shoe
class Game:
    def __init__(self, nDecks=int):
        self.shoe = Shoe(nDecks)

        self.shoe.shuffle()

        while self.shoe.getCardsRemaining() > 0:
            c = self.shoe.draw()

            print(c.getName() + " " + c.getSuit().name)


#game = Game(2)

