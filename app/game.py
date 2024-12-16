from entities import Shoe
from helpers import Constants
from helpers import CardHelper
from .analytics import Analytics
from entities import Player
from entities import Dealer
from .state import State
import time
class Game:
    def __init__(self, nDecks=int, initalAmount=Constants.defaultInitialAmount):
        self.shoe = Shoe(nDecks)
        self.analytics = Analytics()
        self.player = Player()
        self.dealer = Dealer()
        self.state = State.GAME_NOT_STARTED
        self.bet = 100 # TODO get defaults
        
        # shuffle decks
        self.setupGame()
        
        
        self.play()
        
        
        
        


            
    def setupGame(self):
        self.shoe.shuffle()
     
    def __printPlayerHand(self):
        s = ["P: "]
        
        for h in self.player.hand:
            s.append(h.getName())
        print("Total: " + str(self.player.total))
        print(" ".join(s))
        
    def __printDealerHand(self):
        s = ["D: "]
        
        for h in self.dealer.hand:
            if h.hide == True:
                s.append("*")
            else:
                s.append(h.getName())
        print(" ".join(s))
     
    def __printHands(self):
        print("XXXXXXXXXXXXXXXXXX")
        print(" ")
        self.__printDealerHand()
        self.__printPlayerHand()
        print(" ")
        print("XXXXXXXXXXXXXXXXXX")
        
    
    def play(self):
        
        while self.state != State.GAME_OVER:
            print(self.state.name)
            self.__printHands()
            time.sleep(1)

            if self.state == State.GAME_NOT_STARTED:
                startingAmount = 2500#input("How Much to start with? Default is 2500")
                
                self.player.bankroll = startingAmount
                
                start = 'y'#input("StartGame? (y/n)")
                if start == "yes" or start == 'y':
                    self.state = State.SETUP
            
            elif self.state == State.SETUP:
                # Place bet
                self.bet = -1
                while self.bet == -1:
                    x = input("How much would you like to bet")
                    if x.isnumeric() and int(x) > 5: # TODO min bet
                        self.bet = int(x)
                    else:
                        print("invalid input")
                self.player.bankroll -= self.bet
            
                
                
                # Deal cards
                card1 = self.shoe.draw()
                dcard1 = self.shoe.draw()  
                card2 = self.shoe.draw()
                dcard2 = self.shoe.draw()
                self.player.hand.append(card1)
                self.player.hand.append(card2)
                self.player.total += CardHelper.nameToValue(card1)
                self.player.total += CardHelper.nameToValue(card2)
                 
                dcard2.hide = True
                self.dealer.hand.append(dcard1)
                self.dealer.hand.append(dcard2)
                self.dealer.total += CardHelper.nameToValue(dcard1)
                self.dealer.total += CardHelper.nameToValue(dcard2)
                
                # if player total == 21, player wins 2:1, go to end round state
                if self.player.total == 21:
                    self.state = State.END_ROUND_WIN
                    continue
                
                shouldHit = 'y'
                
                self.state = State.PLAYER_TURN
                
                
                
                
               
                
            
            
            elif self.state == State.PLAYER_TURN:
                shouldHit = input("Hit? (y/n)")
                if shouldHit == 'n':
                    self.state = State.DEALER_TURN
                    self.dealer.hand[1].hide = False
            
                else: 
                    nextCard = self.shoe.draw()
                    self.player.hand.append(nextCard)
                    if self.player.total > 10 and nextCard.getName == "A":
                        self.player.total += 1
                    else:
                        self.player.total += CardHelper.nameToValue(nextCard)
                        
                    if self.player.total == 21:
                        self.state = State.END_ROUND_WIN


            elif self.state == State.DEALER_TURN:
                nextCard = self.shoe.draw()
                self.dealer.hand.append(nextCard)
                if self.dealer.total > 10 and nextCard.getName == "A":
                    self.dealer.total += 1
                else:
                    self.dealer.total += CardHelper.nameToValue(nextCard)
                    
                if self.dealer.total > 21:
                    self.state = State.END_ROUND_WIN
                elif self.dealer.total > self.player.total:
                    self.state = State.END_ROUND_WIN
                elif self.dealer.total >= 17:
                    self.state = State.END_ROUND_WIN
                
                    
                
            elif self.state == State.END_ROUND_WIN:
                print("WIN")
                self.player.bankroll += (2*self.bet)
                
                input("Press any key to continue")
                pass
            elif self.state == State.END_ROUND_LOSE:
                print("LOST")
                input("Press any key to continue")
                pass
            else:
                #Done
                pass
            
        
        
        
        '''
        while game state not done
            player hits
        
        return who won/winnings
        
        '''
        
        

    
            
        


#game = Game(2)

