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
        self.player_hand = [self.player_current_card_one, self.player_current_card_two]
        self.dealer_hand = [self.dealer_face_up_card]

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

    def next_card_draw_player(self, screen):
        self.player_hand.append(self.next_card)
        card_surface = self.next_card.get_surface()
        screen.blit(card_surface, ((100 * self.player_card_nr) + 60, 460))
        self.player_card_nr += 1

    def next_card_draw_dealer(self, screen):
        self.dealer_hand.append(self.next_card)
        card_surface = self.next_card.get_surface()
        screen.blit(card_surface, ((100 * self.dealer_card_nr) + 60, 40))
        self.dealer_card_nr += 1

    def player_hand_value(self):
        return self.calculate_hand_value(self.player_hand)

    def dealer_hand_value(self):
        return self.calculate_hand_value(self.dealer_hand)

    def calculate_hand_value(self, hand):
        total_value = sum(card.get_value() for card in hand)
        aces_count = sum(1 for card in hand if isinstance(card, Ace))

        while total_value > 21 and aces_count > 0:
            total_value -= 10
            aces_count -= 1

        return total_value
