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

# Calculate and display initial hand values
player_hand_value = game.player_hand_value()
dealer_hand_value = game.dealer_hand_value()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.next_card_draw_dealer(screen)
                game.next_card = game.get_random_card()
                dealer_hand_value = game.dealer_hand_value()
            if event.key == pygame.K_RETURN:
                game.next_card_draw_player(screen)
                game.next_card = game.get_random_card()
                player_hand_value = game.player_hand_value()

    title_surface = title_font.render("Press Space To Stand", True, TITLE_COLOR)
    screen.blit(title_surface, (100, 660))
    title_surface = title_font.render("Press Enter To Hit", True, TITLE_COLOR)
    screen.blit(title_surface, (400, 660))

    # Fill background rectangle for player hand value display
    pygame.draw.rect(screen, DARK_GREEN, (50, 350, 250, 50))
    player_hand_value_surface = title_font.render(f"Hand Value: {player_hand_value}", True, TITLE_COLOR)
    screen.blit(player_hand_value_surface, (50, 350))

    # Fill background rectangle for dealer hand value display
    pygame.draw.rect(screen, DARK_GREEN, (50, 300, 250, 50))
    dealer_hand_value_surface = title_font.render(f"Dealer: {dealer_hand_value}", True, TITLE_COLOR)
    screen.blit(dealer_hand_value_surface, (50, 300))

    pygame.display.update()
    clock.tick(60)
