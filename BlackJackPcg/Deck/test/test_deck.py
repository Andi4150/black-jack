from unittest import TestCase
from BlackJackPcg.Deck import Deck
import io
import sys


# from BlackJackPcg.Utils import CardUtils

class TestDeck(TestCase):

    def test_initialising(self):
        flag = True
        # arrange
        try:
            d = Deck()
            d.init_deck()
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_deck_length(self):
        flag = True
        # arrange
        try:
            d = Deck()
            d.init_deck()
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(len(d.deck) == 52)
        else:
            self.assertTrue(False)

    def test_deck_duplicates(self):
        flag = True
        # arrange
        try:
            d = Deck()
            d.init_deck()
        except RuntimeError:
            flag = False
        # act
        dedup_deck = set(d.deck)
        # assert
        if flag:
            self.assertTrue(len(d.deck) == len(dedup_deck))
        else:
            self.assertTrue(False)


    def test_get_deck(self):
        flag = True
        # arrange
        try:
            d = Deck()
            d.init_deck()
        except RuntimeError:
            flag = False
        # act
        test_d = d.get_deck()
        # assert
        if flag:
            self.assertTrue(test_d == d.deck)
        else:
            self.assertTrue(False)

    def test_shuffle_deck(self):
        flag = True
        # arrange
        try:
            d = Deck()
            d.init_deck()
        except RuntimeError:
            flag = False
        # choose positions in the deck to check the cards
        first_card = d.deck[0]
        middle_card = d.deck[25]
        final_card = d.deck[51]
        # act
        d.shuffle_deck()
        # assert
        shuffle_count = 0
        if first_card == d.deck[0] and middle_card == d.deck[25] and final_card == d.deck[51]:
            flag = False
        if flag:
            self.assertFalse(False)
        else:
            self.assertTrue(False)

    def test_print_deck_shows_card(self):
        # arrange
        d = Deck()
        d.init_deck()
        # initialise StringIO object
        out = io.StringIO()
        sys.stdout = out
        # act
        d.print_deck()
        # getvalue() returns a str containing the entire contents of the buffer.
        output = out.getvalue().strip()
        # assert
        self.assertTrue(output.count("The card is:") == 52)

    def test_print_deck_new_line(self):
        # arrange
        d = Deck()
        d.init_deck()
        # initialise StringIO object
        out = io.StringIO()
        sys.stdout = out
        # act
        d.print_deck()
        # getvalue() returns a str containing the entire contents of the buffer.
        output = out.getvalue().strip()
        # assert
        self.assertFalse(output.find("\n") == -1)

    def test_get_next_card_length(self):
        # arrange
        d = Deck()
        d.init_deck()
        # act
        cards = d.get_next_card(2)
        # asset
        self.assertTrue(len(cards) == 2)

    def test_get_next_card_deck_length(self):
        # arrange
        d = Deck()
        d.init_deck()
        # act
        cards = d.get_next_card(2)
        # asset
        self.assertTrue(len(d.deck) == 50)

    def test_get_next_card_removed_from_deck(self):
        # arrange
        d = Deck()
        d.init_deck()
        # act
        cards = d.get_next_card(2)
        # asset
        for c in d.deck:
            for card in cards:
                self.assertFalse(c == card)

    def test_get_next_card_large_input(self):
        # arrange
        flag = True
        d = Deck()
        d.init_deck()
        # act
        try:
            cards = d.get_next_card(4)
        except RuntimeError:
            flag = False
        # assert - this should fail
        if flag:
            self.assertTrue(False)
        else:
            self.assertFalse(False)

    def test_get_next_card_neg_input(self):
        # arrange
        flag = True
        d = Deck()
        d.init_deck()
        # act
        try:
            cards = d.get_next_card(-1)
        except RuntimeError:
            flag = False
        # assert - this should fail
        if flag:
            self.assertTrue(False)
        else:
            self.assertFalse(False)


    def test_get_next_card_non_integer(self):
        # arrange
        flag = True
        d = Deck()
        d.init_deck()
        # act
        try:
            cards = d.get_next_card(1.5)
        except ValueError:
            flag = False
        # assert - this should fail
        if flag:
            self.assertTrue(False)
        else:
            self.assertFalse(False)