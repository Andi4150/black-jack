from unittest import TestCase

from BlackJackPcg.Card import Card
from BlackJackPcg.Game import Game
from BlackJackPcg.Player.Players import Player

import mock
import io
import sys

# from BlackJackPcg.Utils import CardUtils
from BlackJackPcg.Utils import CardUtils


class TestGame(TestCase):

    def test_initialising(self):
        flag = True
        # arrange
        try:
            d = Game()
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_initialising_w_list(self):
        flag = True
        # arrange
        p = Player('user_1')
        g = Game([p])
        p_list = g.get_players()
        # assert
        if len(p_list) == 1:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_get_dealer(self):
        flag = True
        # arrange
        p = Player('user_1')
        g = Game([p])
        dealer = g.get_dealer()
        # assert
        if dealer == g.dealer:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_add_players(self):
        # arrange
        p = Player('user_1')
        g = Game([p])
        # act
        g.add_players('user_2')
        p_list = g.get_players()
        # assert
        if len(p_list) == 2:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_username_input(self):
        # arrange
        g = Game()
        # act
        with mock.patch("builtins.input", side_effect=['Andi']):
            g.add_players(g.request_player_name())
        p_list = g.get_players()
        # assert
        if p_list[0].get_user_name() == 'Andi':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_new_player_decision(self):
        pass

    def test_player_turn(self):
        # arrange
        p = Player('user_1')
        g = Game([p])
        # act
        g.add_players('user_2')
        with mock.patch("builtins.input", side_effect=[0, 0]):
            g.players_turn()
        # assert
        if g.score_dict.get(p) == 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_dealer_turn(self):
        # arrange
        p = Player('user_1')
        c1 = Card(CardUtils.get_possible_suits()[0], '9')
        c2 = Card(CardUtils.get_possible_suits()[0], '10')
        p.add_cards_to_hand(([c1, c2]))
        g = Game([p])
        g.start_game()
        # act
        with mock.patch("builtins.input", side_effect=[0]):
            g.players_turn()
            g.dealer_turn()
        # assert
        if g.dealer.get_points() > 17:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_calculate_win(self):
        # arrange
        p = Player('user_1')
        c1 = Card(CardUtils.get_possible_suits()[0], '8')
        c2 = Card(CardUtils.get_possible_suits()[0], '10')
        c3 = Card(CardUtils.get_possible_suits()[0], 'J')
        c4 = Card(CardUtils.get_possible_suits()[0], '9')
        p.add_cards_to_hand(([c1, c2]))
        g = Game([p])
        g.dealer.add_cards_to_hand([c3, c4])
        # act
        with mock.patch("builtins.input", side_effect=[0]):
            g.players_turn()
            g.dealer_turn()
            g.calculate_winner()
        # assert
        if g.dealer.winner_streak > 1:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_calculate_win(self):
        # arrange
        p = Player('user_1')
        c1 = Card(CardUtils.get_possible_suits()[0], 'Q')
        c2 = Card(CardUtils.get_possible_suits()[0], '10')
        c3 = Card(CardUtils.get_possible_suits()[0], 'J')
        c4 = Card(CardUtils.get_possible_suits()[0], '8')
        p.add_cards_to_hand(([c1, c2]))
        g = Game([p])
        g.dealer.add_cards_to_hand([c3, c4])
        # act
        with mock.patch("builtins.input", side_effect=[0]):
            g.players_turn()
            g.dealer_turn()
            g.calculate_winner()
        # assert
        if p.get_winner_streak() == 1:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
