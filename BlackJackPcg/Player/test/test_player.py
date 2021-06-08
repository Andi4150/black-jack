from unittest import TestCase
from BlackJackPcg.Card import Card
from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player import Person
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Player.Dealer import Dealer
import io
import sys
import mock

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
        # do the test with the temp obj that is a "bubble wrap" of the abstract obj.
        # create a temporary object inheriting Person class
        class TempObj(Person):
            # initiate temp object
            def __int__(self, user_name):
                super().__init__(user_name=user_name)
            # specify the abstract function
            def pick_a_card_decision(self):
                raise NotImplementedError("Its an abstract test")

        test_obj = TempObj("test username")
        # act
        init_len = len(test_obj.get_hand())
        test_obj.add_cards_to_hand(d.get_next_cards(2))
        new_len = len(test_obj.get_hand())
        # assert
        if init_len + 2 != new_len:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_show_n_cards(self):
        # arrange
        d = Deck()

        # do the test with the temp obj that is a "bubble wrap" of the abstract obj.
        # create a temporary object inheriting Person class
        class TempObj(Person):
            # initiate temp object
            def __int__(self, user_name):
                super().__init__(user_name=user_name)

            # specify the abstract function
            def pick_a_card_decision(self):
                raise NotImplementedError("Its an abstract test")

        test_obj = TempObj("test username")
        n_cards = 2
        out = io.StringIO()
        sys.stdout = out
        # act
        d.init_deck()
        test_obj.add_cards_to_hand(d.get_next_cards(2))
        test_obj.show_n_cards(n_cards)
        # getvalue() returns a str containing the entire contents of the buffer.
        output = out.getvalue().strip()
        # assert
        self.assertTrue(output.count("The card is:") == 2)

    def test_get_points_func(self):
        # arrange
        d = Deck()

        # do the test with the temp obj that is a "bubble wrap" of the abstract obj.
        # create a temporary object inheriting Person class
        class TempObj(Person):
            # initiate temp object
            def __int__(self, user_name):
                super().__init__(user_name=user_name)

            # specify the abstract function
            def pick_a_card_decision(self):
                raise NotImplementedError("Its an abstract test")

        test_obj = TempObj("test username")
        points = 0
        n_cards = 2
        # act
        d.init_deck()
        test_obj.add_cards_to_hand(d.get_next_cards(n_cards))
        points = test_obj.get_points()
        # assert
        self.assertTrue(points <= 22)

    def test_pick_a_card_decision_player(self):
        # arrange
        p = Player('Bill')
        expected_output = 1
        # act
        # with mock.patch.object(__builtins__, 'input', get_input(1)):
        with mock.patch('builtins.input', return_value=expected_output):
            # assert
            self.assertTrue(p.pick_a_card_decision() == expected_output)

    def test_pick_a_card_decision_player_gives_error(self):
        import io
        import contextlib
        # arrange
        p = Player("Bill")
        # act
        # make the input so it will be three and then a string
        with mock.patch("builtins.input", side_effect=[3, 'str', 1]):
            with io.StringIO() as buffer:
                # redirect the stdout to the buffer - whatever goes to stdout will go to buffer
                with contextlib.redirect_stdout(buffer):
                    p.pick_a_card_decision()
                    printed_text = buffer.getvalue()
                self.assertTrue(printed_text.count("Incorrect input! Do you want a card? Please enter 0 for no, 1 for yes") == 2)

    def test_pick_a_card_decision_dealer_no(self):
        # arrange
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
        p = Dealer()
        # act
        d.init_deck()
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], '9')])
        p.add_cards_to_hand([Card(CardUtils.get_possible_suits()[0], 'A')])
        p.pick_a_card_decision()
        # assert
        self.assertFalse(p.pick_a_card_decision())
