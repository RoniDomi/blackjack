import pygame
import sys
from game import Game

pygame.init()

DARK_GREEN = (72, 163, 62)
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Black Jack")

game = Game()
clock = pygame.time.Clock()

screen.fill(DARK_GREEN)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

running = True

game.dealer_draw_face_up(screen)
game.dealer_draw_face_down(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.next_card_draw(screen)


    game.player_draw_card_one(screen)
    game.player_draw_card_two(screen)

    pygame.display.update()
    clock.tick(60)
