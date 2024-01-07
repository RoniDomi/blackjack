from game import Game


game = Game()
initial_hand = game._game_start()

print("\nBlackJack\n")


print(f'Player Hand: {initial_hand}')
print(f'Hand Value:  {game.player._hand_value}')
