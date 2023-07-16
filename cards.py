import pygame.image
from cardattributes import Card

class Ace(Card):
    def __init__(self):
        super().__init__(id = 1)
        self.card = pygame.image.load('assets/10.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Two(Card):
    def __init__(self):
        super().__init__(id = 2)
        self.card = pygame.image.load('assets/20.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Three(Card):
    def __init__(self):
        super().__init__(id = 3)
        self.card = pygame.image.load('assets/30.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Four(Card):
    def __init__(self):
        super().__init__(id = 4)
        self.card = pygame.image.load('assets/40.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Five(Card):
    def __init__(self):
        super().__init__(id = 5)
        self.card = pygame.image.load('assets/50.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Six(Card):
    def __init__(self):
        super().__init__(id = 6)
        self.card = pygame.image.load('assets/60.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Seven(Card):
    def __init__(self):
        super().__init__(id = 7)
        self.card = pygame.image.load('assets/70.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Eight(Card):
    def __init__(self):
        super().__init__(id = 8)
        self.card = pygame.image.load('assets/80.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Nine(Card):
    def __init__(self):
        super().__init__(id = 9)
        self.card = pygame.image.load('assets/90.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Ten(Card):
    def __init__(self):
        super().__init__(id = 10)
        self.card = pygame.image.load('assets/100.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Jack(Card):
    def __init__(self):
        super().__init__(id = 11)
        self.card = pygame.image.load('assets/110.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class Queen(Card):
    def __init__(self):
        super().__init__(id = 12)
        self.card = pygame.image.load('assets/120.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()

class King(Card):
    def __init__(self):
        super().__init__(id = 13)
        self.card = pygame.image.load('assets/130.png')
        self.card = pygame.transform.scale(self.card, (130, 200))

    def get_surface(self):
        return self.card.copy()
