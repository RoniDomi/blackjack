import random
from cards import *

class Game:
    def __init__(self):
        self.cards = [Ace(), Two(), Three(), Four(), Five(), Six(), Seven(),
                      Eight(), Nine(), Ten(), Jack(), Queen(), King()]
        self.player_current_card_one = self.get_random_card()
        self.player_current_card_two = self.get_random_card()
        self.next_card = self.get_random_card()

    def get_random_card(self):
        card = random.choice(self.cards)
        return card

    def player_draw_card_one(self, screen):
        card_surface = self.player_current_card_one.get_surface()
        screen.blit(card_surface, (100, 400))

    def player_draw_card_two(self, screen):
        card_surface = self.player_current_card_two.get_surface()
        screen.blit(card_surface, (300, 400))
