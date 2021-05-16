from unittest import TestCase
from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player import Person, Player, Dealer
import io
import sys


class TestDeck(TestCase):

    def test_init(self):
        flag = True
        # arrange
        try:
            p = Player('Bill')
            bot = Dealer()
        except RuntimeError:
            flag = False
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_add_cards_to_person(self):
        # arrange
        d = Deck()
        d.init_deck()
        p = Person('bill')
        # act
        init_len = len(p.get_hand())
        p.add_cards_to_hand(d.get_next_cards(2))
        new_len = len(p.get_hand())
        # assert
        if init_len + 2 != new_len:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    # def test_add_cards_to_dealer(self):
    #     # arrange
    #     d = Deck()
    #     d.init_deck()
    #     p = Dealer()
    #     # act
    #     init_len = len(p.get_hand())
    #     p.add_cards_to_hand(d.get_next_cards(1))
    #     new_len = len(p.get_hand())
    #     # assert
    #     if init_len + 1 != new_len:
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)

    def test_show_n_cards(self):
        # arrange
        d = Deck()
        p = Person()
        n_cards = 2
        out = io.StringIO()
        sys.stdout = out
        # act
        d.init_deck()
        p.add_cards_to_hand(d.get_next_cards(2))
        p.show_n_cards(n_cards)
        # getvalue() returns a str containing the entire contents of the buffer.
        output = out.getvalue().strip()
        # assert
        self.assertTrue(output.count("The card is:") == 2)
