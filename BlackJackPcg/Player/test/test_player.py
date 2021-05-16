from unittest import TestCase
from BlackJackPcg.Card import Card
from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player import Person, Player, Dealer
import io
import sys

from BlackJackPcg.Utils import CardUtils


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
        # p = Person('bill')
        p = Player('Bill')
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
        # p = Person()
        p = Player('Bill')
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

    def test_get_points_func(self):
        # arrange
        d = Deck()
        # p = Person()
        p = Player('Bill')
        point = 0
        n_cards = 2
        # act
        d.init_deck()
        p.add_cards_to_hand(d.get_next_cards(2))
        points = p.get_points()
        # assert
        self.assertTrue(points <= 22)

    # def test_pick_a_card_decision_player(self):
    #     # arrange
    #     d = Deck()
    #     # p = Person()
    #     p = Player('Bill')
    #     # act
    #     d.init_deck()
    #     dec = p.pick_a_card_decision()
    #     # assert
    #     self.assertTrue(dec == 0)

    def test_pick_a_card_decision_dealer_no(self):
        # arrange
        # p = Person()
        p = Dealer()
        # act
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], '5')])
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], '2')])
        p.pick_a_card_decision()
        # assert
        self.assertTrue(p.pick_a_card_decision())

    def test_pick_a_card_decision_dealer_yes(self):
        # arrange
        d = Deck()
        # p = Person()
        p = Dealer()
        # act
        d.init_deck()
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], '9')])
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], 'A')])
        p.pick_a_card_decision()
        # assert
        self.assertFalse(p.pick_a_card_decision())
