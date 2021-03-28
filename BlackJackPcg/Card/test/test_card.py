# import the packages required
import io
import sys

from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils
from unittest import TestCase


class TestCard(TestCase):

    def test_card_for_suit(self):
        flag = False
        try:
            Card("asd", CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_number(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], "asd")
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_creation(self):
        # except this to be successful
        flag = True
        try:
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = False
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_get_suit_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        # act
        suit = c.get_suit()
        # assert
        self.assertTrue(suit in CardUtils.get_possible_suits())

    def test_get_number_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        # act
        num = c.get_number()
        # assert
        self.assertTrue(num in CardUtils.get_possible_numbers())

    def test_card_show_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_numbers()[0])
        # In-memory text streams are available as StringIO objects. (https://docs.python.org/3/library/io.html)
        # For strings, StringIO can be used like a file opened in text mode.
        # initialise StringIO object
        out = io.StringIO()
        # https://docs.python.org/3/library/sys.html#sys.stdout
        # stdout is used for the output of print() and expression statements and for the prompts of input();
        sys.stdout = out
        # act
        c.show()
        # getvalue() returns a str containing the entire contents of the buffer.
        output = out.getvalue().strip()
        # assert
        self.assertTrue(output == "The card is: {}{}".format(c.number, c.suit))


