from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player.Dealer import Dealer


class GameV2:

    def __init__(self, player_list=[]):
        self.deck = Deck()
        self.deck.init_deck()
        if len(player_list) > 0:
            self.players = player_list
        else:
            self.players = []
        self.dealer = Dealer()

    def get_players(self):
        return self.players

    def get_deck(self):
        return self.deck

    def get_dealer(self):
        return self.dealer

    def number_of_players(self):
        pass

    def add_player(self, new_user):
        list_of_players = self.get_players()
        if new_user in list_of_players:
            print('{} is already in the game. No-one has been added'.format(new_user))
        else:
            print('Adding {} to the list of players'.format(new_user))
            list_of_players.append(new_user)
        return list_of_players

    def play_game(self):
        # deal cards to players
        d = self.get_dealer()
        d.add_cards_to_hand(1)
        for p in self.get_players():
            p.add_cards_to_hand(2)
        # check for winner/bust
        # add to winners or continue

        for p in self.get_players():
            # collect decision from current player
            if p.pick_a_card_decision() == 1:
                p.add_cards_to_hand(2)
            else:
                print()
        # check if bust
        # repeat until bust or decision is no
        # repeat for dealer
        # check for winners
