from player import Player
from dealer import Dealer

class Game:
    def __init__(self):
        self._player_turn = True
        self._dealer_turn = False
        self._round_over = False
        self.player = Player()
        self.dealer = Dealer()

    def _game_start(self):
        for i in range(2):
            self.player.player_draw()

        if self.player._hand_value > 21:
            self.player._hand_value -= 10

        return self.player._hand

    def _dealer_start(self):
        for i in range(2):
            self.dealer.dealer_draw()

        if self.dealer._hand_value > 21:
            self.dealer._hand_value -= 10

        self.dealer._hand.insert(1, self.dealer._deck._deck[0])

        self.dealer._hand_value = '?'

        return self.dealer._hand[:2]
