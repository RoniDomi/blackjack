from cards import *

class Game:
    def __init__(self):
        self.cards = [Ace(), Two(), Three(), Four(), Five(), Six(), Seven(), Eight(), Nine(), Ten(),
                      Jack(), Queen(), King()]
        self.face_down = [FDown()]
        self.player_turn = True
        self.dealer_card_nr = 1
        self.player_card_nr = 2
        self.player_current_card_one = self.get_random_card()
        self.player_current_card_two = self.get_random_card()
        self.dealer_face_up_card = self.get_random_card()
        self.dealer_face_down_card = self.get_face_down_card()
        self.next_card = self.get_random_card()

    def get_random_card(self):
        card = random.choice(self.cards)
        return card

    def get_face_down_card(self):
        card = random.choice(self.face_down)
        return card

    def player_draw_card_one(self, screen):
        card_surface = self.player_current_card_one.get_surface()
        screen.blit(card_surface, (100, 460))

    def player_draw_card_two(self, screen):
        card_surface = self.player_current_card_two.get_surface()
        screen.blit(card_surface, (170, 460))

    def dealer_draw_face_up(self, screen):
        card_surface = self.dealer_face_up_card.get_surface()
        screen.blit(card_surface, (100, 40))

    def dealer_draw_face_down(self, screen):
        card_surface = self.dealer_face_down_card.get_surface()
        screen.blit(card_surface, (160, 40))

    def next_card_draw_dealer(self, screen):
        card_surface = self.next_card.get_surface()
        screen.blit(card_surface, ((100 * self.dealer_card_nr) + 60, 40))
        self.dealer_card_nr += 1

    def next_card_draw_player(self, screen):
        card_surface = self.next_card.get_surface()
        screen.blit(card_surface, ((100 * self.player_card_nr) + 60, 460))
        self.player_card_nr += 1