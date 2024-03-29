import random

from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils


class Deck:

    def __init__(self):
        self.deck = []

    def init_deck(self):
        for i_suit in CardUtils.get_possible_suits():
            for i_num in CardUtils.get_possible_numbers():
                self.deck.append(Card(i_suit, i_num))

    def get_deck(self):
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            card.show()

    def get_next_cards(self, num_cards):
        if not isinstance(num_cards, int):
            raise ValueError(
                "The value passed on argument num_cards in function get_next_card,should be an integer. It received: {}" \
                    .format(type(num_cards))
            )
        dealt_cards = []
        if 2 >= num_cards > 0:
            for i in range(num_cards):
                dealt_cards.append(self.deck[i])
                self.deck.remove(self.deck[i])
        else:
            raise RuntimeError("Number of cards must be greater than 0 and no more than 2")
        return dealt_cards
