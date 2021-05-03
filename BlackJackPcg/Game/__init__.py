# need a Class for game funcitonality

from BlackJackPcg.Deck import Deck
from abc import abstractmethod, ABC


class Game:

    def __init__(self):
        self.deck = Deck.init_deck()
        self.players = []


    @abstractmethod
    def calc_score(self):
        # should sum the numbers of the cards in the hand
        # initialise the score
        score = 0
        for card in self.hand:
            score += card.get_number()
        # logic for value of the ace
        # check if hand has "gone bust"
        return score