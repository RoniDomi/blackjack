from game import Game


game = Game()
initial_hand = game._game_start()
initial_dealer = game._dealer_start()

print("\nBlackJack\n")


print(f'Player Hand: {initial_hand}')
print(f'Hand Value:  {game.player._hand_value}\n')

print(f'Dealer Hand: {initial_dealer}')
print(f'Hand Value:  {game.dealer._hand_value}')
