import pygame.image

class Card:
    def __init__(self, id):
        self.value = id
        self.card = {}

    def draw(self, screen):
        card_rect = pygame.Rect(16, 16, 16, 16)
        pygame.draw.rect(screen, self.card[id], card_rect)
