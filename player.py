from cards import Cards
import random


# Object class for controlling the player
class Player:
    def __init__(self):
        self._cards = 0
        self._hand_value = 0
        self._deck = Cards()
        self._hand = list()

    # Function that handles player card draw and value storing
    def player_draw(self):
        card = self._deck.draw()
        face = random.choice(self._deck._faces)

        card_value = self._deck.value(card)
        self._hand_value += card_value

        if card_value >= 10:
            self._hand.append(f'{card} {face}')
        else:
            self._hand.append(f'{card_value}{face}')

        return
