from enum import Enum

class State(Enum):
    GAME_NOT_STARTED = 1
    SETUP = 2
    PLAYER_TURN = 3
    DEALER_TURN = 4
    END_ROUND_WIN = 5
    END_ROUND_LOSE = 6
    GAME_OVER = 7
    
    