import pygame
import sys

pygame.init()

DARK_GREEN = (72, 163, 62)
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Black Jack")

card = pygame.image.load('assets/01.png')
card = pygame.transform.rotozoom(card, 0, 0.6)

def cards(x, y):
    screen.blit(card, (x, y))

x = 380
y = 100

clock = pygame.time.Clock()

screen.fill(DARK_GREEN)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    cards(x, y)

    pygame.display.update()
    clock.tick(60)
