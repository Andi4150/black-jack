# import the packages required
from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils
from unittest import TestCase


class TestCard(TestCase):

    def test_card_for_suit(self):
        flag = False
        try:
            Card("asd", CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_color(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], "asd", CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = True
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_for_number(self):
        flag = False
        try:
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], "asd")
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
            Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])
        except RuntimeError:
            flag = False
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_card_get_colour(self):
        # arrange
        # initialise flag
        flag = True
        # don't need to try with creating cards as that is already in a different test
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
        # act
        # testing if the action is as expected
        if c.get_color() == CardUtils.get_possible_colors()[0]:
            # if these match then flag is true - test passed
            flag = True
        else:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    # then followed tutorial:
    def test_get_color_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])
        # act
        col = c.get_color()
        # assert
        self.assertTrue(col in CardUtils.get_possible_colors())

    def test_get_suit_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])
        # act
        suit = c.get_suit()
        # assert
        self.assertTrue(suit in CardUtils.get_possible_suits())

    def test_get_number_func(self):
        # arrange
        c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0],
                 CardUtils.get_possible_numbers()[0])
        # act
        num = c.get_number()
        # assert
        self.assertTrue(num in CardUtils.get_possible_numbers())

    # def test_card_show_func(self):
    #     # arrange
    #     # expect: The card is: 2SR
    #     c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
    #     # act
    #     txt = c.show()
    #     txt_1 = c.show()[0:12]
    #     print(txt_1)
    #     txt_2 = str(txt)[-3]
    #     # assert
    #     self.assertTrue(txt_1 == 'The card is:')

