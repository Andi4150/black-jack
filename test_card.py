

# content of test_sample.py
from main import Card
from unittest import TestCase


class TestCard(TestCase):

    def test_card_for_suit(self):
        flag = False
        try:
            Card("asd", "R", "2")
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_color(self):
        flag = False
        try:
            Card("S", "asd", "2")
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_number(self):
        flag = False
        try:
            Card("S", "R", "asd")
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)