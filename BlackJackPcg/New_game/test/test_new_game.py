from unittest import TestCase
from BlackJackPcg.Deck import Deck
from BlackJackPcg.New_game import GameV2


class TestDeck(TestCase):

    def test_initialising_with_player(self):
        flag = True
        # arrange
        try:
            g = GameV2(player_list=['user'])
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_initialising_without_player(self):
        flag = True
        # arrange
        try:
            g = GameV2()
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_initialising_with_two_player(self):
        flag = True
        # arrange
        try:
            g = GameV2(player_list=['user1', 'user2'])
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_add_player(self):
        flag = True
        # arrange
        try:
            g = GameV2(player_list=['user1', 'user2'])
            g.add_player('user3')
        except RuntimeError:
            flag = False
        # assert
        if flag:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_add_player_new_name(self):
        # arrange
        g = GameV2(player_list=['user1', 'user2'])
        g.add_player('user3')
        # assert
        if len(g.get_players()) > 2:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_add_player_same_name(self):
        # arrange
        g = GameV2(player_list=['user1', 'user2'])
        g.add_player('user2')
        # assert
        if len(g.get_players()) == 2:
            self.assertTrue(True)
        else:
            self.assertTrue(False)