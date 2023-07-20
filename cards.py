import pygame.image
from cardattributes import Card
import random


class Card(Card):
    def __init__(self, value, image_paths):
        super().__init__(value)
        self.image_paths = image_paths
        self.random_texture()

    def random_texture(self):
        self.card = pygame.image.load(random.choice(self.image_paths))
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

    def get_value(self):
        return self.value

class FDown(Card):
    def __init__(self):
        super().__init__(value=0, image_paths=['assets/01.png'])


class Ace(Card):
    def __init__(self):
        super().__init__(value=11, image_paths=[
            'assets/10.png',
            'assets/11.png',
            'assets/12.png',
            'assets/13.png',
        ])


class Two(Card):
    def __init__(self):
        super().__init__(value=2, image_paths=[
            'assets/20.png',
            'assets/21.png',
            'assets/22.png',
            'assets/23.png',
        ])


class Three(Card):
    def __init__(self):
        super().__init__(value=3, image_paths=[
            'assets/30.png',
            'assets/31.png',
            'assets/32.png',
            'assets/33.png',
        ])


class Four(Card):
    def __init__(self):
        super().__init__(value=4, image_paths=[
            'assets/40.png',
            'assets/41.png',
            'assets/42.png',
            'assets/43.png',
        ])


class Five(Card):
    def __init__(self):
        super().__init__(value=5, image_paths=[
            'assets/50.png',
            'assets/51.png',
            'assets/52.png',
            'assets/53.png',
        ])


class Six(Card):
    def __init__(self):
        super().__init__(value=6, image_paths=[
            'assets/60.png',
            'assets/61.png',
            'assets/62.png',
            'assets/63.png',
        ])


class Seven(Card):
    def __init__(self):
        super().__init__(value=7, image_paths=[
            'assets/70.png',
            'assets/71.png',
            'assets/72.png',
            'assets/73.png',
        ])


class Eight(Card):
    def __init__(self):
        super().__init__(value=8, image_paths=[
            'assets/80.png',
            'assets/81.png',
            'assets/82.png',
            'assets/83.png',
        ])


class Nine(Card):
    def __init__(self):
        super().__init__(value=9, image_paths=[
            'assets/90.png',
            'assets/91.png',
            'assets/92.png',
            'assets/93.png',
        ])


class Ten(Card):
    def __init__(self):
        super().__init__(value=10, image_paths=[
            'assets/100.png',
            'assets/101.png',
            'assets/102.png',
            'assets/103.png',
        ])


class Jack(Card):
    def __init__(self):
        super().__init__(value=10, image_paths=[
            'assets/110.png',
            'assets/111.png',
            'assets/112.png',
            'assets/113.png',
        ])


class Queen(Card):
    def __init__(self):
        super().__init__(value=10, image_paths=[
            'assets/120.png',
            'assets/121.png',
            'assets/122.png',
            'assets/123.png',
        ])


class King(Card):
    def __init__(self):
        super().__init__(value=10, image_paths=[
            'assets/130.png',
            'assets/131.png',
            'assets/132.png',
            'assets/133.png',
        ])