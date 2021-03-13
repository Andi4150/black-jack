# need a Parent class called Players and two child classes for players and dealer
# assumption that this is used as the player's hand and will hold the cards of the player
# it will also contain the player's potential actions (hit or stand)

from BlackJackPcg.Deck import Deck
from abc import abstractmethod


class Players:

    def __init__(self):
        self.hand = []

    @abstractmethod
    def init_hand(self):
        """
        program need to deal initial hands to players
        # num_cards = 2 # initially hand is dealt 2 cards
        # self.hand.append(Deck.get_next_card(num_cards))

        :return: initial hand of two cards
        """
        pass

    @abstractmethod
    def get_hand(self):
        return self.hand

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

    @abstractmethod
    def hit(self):
        """
        This function will add a card to the hand if the player chooses

        :param
        :return: hand with additional cards
        """
        # num_cards = 1 # hit means that one card is added to the hand
        # self.hand.append(Deck.get_next_card(num_cards))
        pass

    def stand(self):
        # end the players turn - not sure this needs to be a function...
        pass


class Player(Players):

    def __init__(self):
        Players.__init__()

    def init_hand(self):
        """
        program need to deal initial hands to players
        num_cards = 2 # initially hand is dealt 2 cards
        dealt_cards = Deck.get_next_card(num_cards)
        for cards in dealt_cards:
            self.hand.append(cards)

        :return: self.hand or nothing...
        """
        pass

    def get_hand(self):
        return self.hand

    def calc_score(self):
        """
        function should sum the numbers of the cards in the hand
        # initialise the score
        score = 0
        for card in self.hand:
            score += card.get_number()
        # logic for value of the ace
        # check if hand has "gone bust"
        :return: score

        """
        pass

    def hit(self):
        """
        This function will add a card to the hand if the player chooses

        num_cards = 1 # hit means that one card is added to the hand
        dealt_cards = Deck.get_next_card(num_cards)
        for cards in dealt_cards:
            self.hand.append(cards)

        :param
        :return: hand with additional cards
        """
        pass


class Dealer(Players):

    def __init__(self):
        Players.__init__()

    def init_hand(self):
        """
        program need to deal initial hands to players
        num_cards = 2 # initially hand is dealt 2 cards
        dealt_cards = Deck.get_next_card(num_cards)
        for cards in dealt_cards:
            self.hand.append(cards)

        :return: self.hand or nothing...
        """
        pass

    def get_hand(self):
        return self.hand

    def calc_score(self):
        """
        function should sum the numbers of the cards in the hand
        # initialise the score
        score = 0
        for card in self.hand:
            score += card.get_number()
        # logic for value of the ace - different for a dealer
        # check if hand has "gone bust"
        :return: score

        """
        pass

    def hit(self):
        """
        This function will add a card to the hand of the dealer if the calculated score is less than 17

        if self.calc_score() < 17
            num_cards = 1 # hit means that one card is added to the hand
            dealt_cards = Deck.get_next_card(num_cards)
            for cards in dealt_cards:
                self.hand.append(cards)

        :param
        :return: hand with additional cards
        """
        pass
