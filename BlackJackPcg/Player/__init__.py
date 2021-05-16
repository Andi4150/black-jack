# need a Parent class called Players and two child classes for players and dealer
# assumption that this is used as the player's hand and will hold the cards of the player
# it will also contain the player's potential actions (hit or stand)

from BlackJackPcg.Deck import Deck
from abc import abstractmethod, ABC


class Person(ABC):

    def __init__(self, user_name=''):
        self.hand = []
        if not isinstance(user_name, str):
            raise RuntimeError("The user name passed to the player is not valid as it is {}".format(type(user_name)))
        else:
            self.user_name = user_name

    def add_cards_to_hand(self, cards):
        """
        program need to deal initial hands to players

        :params: deck(so that function can remove cards from deck as deals)
        :return: initial hand of two cards
        """
        if len(self.hand) == 0:
            self.hand = cards
        else:
            self.hand.extend(cards)

    def get_hand(self):
        return self.hand

    def get_user_name(self):
        return self.user_name

    def show_n_cards(self, n_cards):
        for i, card in enumerate(self.hand):
            if i == n_cards:
                break
            card.show()

    def get_points(self):
        sum_points = 0
        sum_ace = 0
        for c in self.hand:
            if c.get_points() == 11:
                sum_ace += 1
            else:
                sum_points += c.get_points()
        if sum_points + sum_ace * 11 < 21:
            return sum_points + sum_ace * 11
        elif sum_points + 11 + sum_ace - 1 < 21:
            return sum_points + 11 + sum_ace - 1
        else:
            return sum_points + sum_ace

    @abstractmethod
    def pick_a_card_decision(self):
        pass


class Player(Person):

    def __init__(self, user_name):
        Person.__init__(self, user_name)

    def pick_a_card_decision(self):
        dec = input('press 0 if you do not want a new card, or 1 if you want a new card')
        return dec


class Dealer(Person):

    def __init__(self):
        Person.__init__(self, 'Dealer')

    def pick_a_card_decision(self):
        if self.get_points() < 17:
            return True
        else:
            return False
