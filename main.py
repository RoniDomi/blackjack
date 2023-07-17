import pygame
import sys
from game import Game

pygame.init()

DARK_GREEN = (72, 163, 62)
TITLE_COLOR = (225, 255, 224)
title_font = pygame.font.Font('Font/game_over.ttf', 60)

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
game.player_draw_card_one(screen)
game.player_draw_card_two(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.next_card_draw_dealer(screen)
                game.next_card = game.get_random_card()
            if event.key == pygame.K_RETURN:
                game.next_card_draw_player(screen)
                game.next_card = game.get_random_card()


    title_surface = title_font.render("Press Space To Stand", True, TITLE_COLOR)
    screen.blit(title_surface, (100, 660))
    title_surface = title_font.render("Press Enter To Hit", True, TITLE_COLOR)
    screen.blit(title_surface, (400, 660))

    pygame.display.update()
    clock.tick(60)
