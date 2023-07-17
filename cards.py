import pygame.image
import random
from cardattributes import Card


class FDown(Card):
    def __init__(self):
        super().__init__(value=0)
        self.card = pygame.image.load('assets/01.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()


class Ace(Card):
    def __init__(self):
        super().__init__(value=11)
        self.number = None
        self.random_number = None
        self.cards = {
            0: pygame.transform.scale(pygame.image.load('assets/10.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/11.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/12.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/13.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.cards[self.number]


class Two(Card):
    def __init__(self):
        super().__init__(value=2)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/20.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/21.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/22.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/23.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Three(Card):
    def __init__(self):
        super().__init__(value=3)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/30.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/31.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/32.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/33.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Four(Card):
    def __init__(self):
        super().__init__(value=4)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/40.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/41.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/42.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/43.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Five(Card):
    def __init__(self):
        super().__init__(value=5)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/50.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/51.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/52.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/53.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Six(Card):
    def __init__(self):
        super().__init__(value=6)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/60.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/61.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/62.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/63.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Seven(Card):
    def __init__(self):
        super().__init__(value=7)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/70.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/71.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/72.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/73.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Eight(Card):
    def __init__(self):
        super().__init__(value=8)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/80.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/81.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/82.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/83.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Nine(Card):
    def __init__(self):
        super().__init__(value=9)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/90.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/91.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/92.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/93.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Ten(Card):
    def __init__(self):
        super().__init__(value=10)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/100.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/101.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/102.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/103.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Jack(Card):
    def __init__(self):
        super().__init__(value=10)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/110.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/111.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/112.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/113.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class Queen(Card):
    def __init__(self):
        super().__init__(value=10)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/120.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/121.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/122.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/123.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]


class King(Card):
    def __init__(self):
        super().__init__(value=10)
        self.number = None
        self.random_number = None
        self.card = {
            0: pygame.transform.scale(pygame.image.load('assets/130.png'), (130, 200)),
            1: pygame.transform.scale(pygame.image.load('assets/131.png'), (130, 200)),
            2: pygame.transform.scale(pygame.image.load('assets/132.png'), (130, 200)),
            3: pygame.transform.scale(pygame.image.load('assets/133.png'), (130, 200))
        }

    def random_texture(self):
        self.random_number = random.randint(0, 3)
        return self.random_number

    def get_surface(self):
        self.number = self.random_texture()
        return self.card[self.number]
