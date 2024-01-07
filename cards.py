import random


class Cards:
    def __init__(self):
        self._deck = ['Face Down', 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                      'Jack', 'Queen', 'King']
        self._faces = ['♤', '♡', '♢', '♧']

    def draw(self):
        return random.choice(self._deck[1:])

    def value(self, card):
        if self._deck.index(card) == 1:
            return 11
        elif self._deck.index(card) >= 11:
            return 10
        else:
            return self._deck.index(card)

    def __str__(self):
        return str(self._deck)
