from unittest import TestCase
from BlackJackPcg.Game import Game
from BlackJackPcg.Player.Players import Player

import mock
import io
import sys


# from BlackJackPcg.Utils import CardUtils

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
        if dealer == g.d:
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

    def test_player_turn(self):
        # arrange
        p = Player('user_1')
        g = Game([p])
        # act
        g.add_players('user_2')
        with mock.patch("builtins.input", side_effect=[0, 0]):
            scores = g.players_turn()
        # assert
        if scores.get(p) == 0:
            self.assertTrue(True)
        else:
            self.assertTrue(False)