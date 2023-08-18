import pygame
import sys
from game import Game
import time

pygame.init()

DARK_GREEN = (72, 163, 62)
TITLE_COLOR = (225, 255, 224)
RED = (247, 44, 30)
title_font = pygame.font.Font('Font/game_over.ttf', 60)
game_over_font = pygame.font.Font('Font/alagard.ttf', 80)

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Black Jack")

game = Game()
clock = pygame.time.Clock()

screen.fill(DARK_GREEN)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 600)

player_hand_value = 0
dealer_hand_value = 0

def draw_cards():
    game.dealer_draw_face_up(screen)
    game.dealer_draw_face_down(screen)
    game.player_draw_card_one(screen)
    game.player_draw_card_two(screen)

def get_value():
    global player_hand_value, dealer_hand_value
    player_hand_value = game.player_hand_value()
    dealer_hand_value = game.dealer_hand_value()

def fill_player_screen():
    pygame.draw.rect(screen, DARK_GREEN, (50, 350, 250, 50))
    player_hand_value_surface = title_font.render(f"Player Hand Value: {player_hand_value}", True, TITLE_COLOR)
    screen.blit(player_hand_value_surface, (50, 350))

def fill_dealer_screen():
    pygame.draw.rect(screen, DARK_GREEN, (50, 300, 250, 50))
    dealer_hand_value_surface = title_font.render(f"Dealer Hand Value: {dealer_hand_value}", True, TITLE_COLOR)
    screen.blit(dealer_hand_value_surface, (50, 300))

fill_dealer_screen()
fill_player_screen()
draw_cards()
get_value()

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_over == False:
                if event.key == pygame.K_RETURN:
                    if player_hand_value > 21:
                        game_surface = game_over_font.render("Dealer Wins!", True, RED)
                        screen.blit(game_surface, (120, 240))
                        game_over = True
                    else:
                        game.next_card_draw_player(screen)
                        game.next_card = game.get_random_card()
                        get_value()
                        fill_player_screen()
                elif event.key == pygame.K_SPACE:
                    while dealer_hand_value < 21 or dealer_hand_value < player_hand_value:
                        game.next_card_draw_dealer(screen)
                        game.next_card = game.get_random_card()
                        dealer_hand_value = game.dealer_hand_value()
                        fill_dealer_screen()
                        if dealer_hand_value == 17 or dealer_hand_value > player_hand_value:
                            break
                    if dealer_hand_value > player_hand_value and dealer_hand_value <= 21:
                        game_surface = game_over_font.render("Dealer Wins!", True, RED)
                        screen.blit(game_surface, (120, 240))
                        game_over = True
                    elif dealer_hand_value > 21:
                        game_surface = game_over_font.render("Player Wins!", True, RED)
                        screen.blit(game_surface, (120, 390))
                        game_over = True
                    elif dealer_hand_value == player_hand_value:
                        game_surface = game_over_font.render("Draw!", True, RED)
                        screen.blit(game_surface, (120, 390))
                        game_over = True
            elif event.key == pygame.K_TAB:
                game = Game()
                screen.fill(DARK_GREEN)
                fill_dealer_screen()
                fill_player_screen()
                draw_cards()
                get_value()
                game_over = False

    pygame.display.update()
    clock.tick(60)
