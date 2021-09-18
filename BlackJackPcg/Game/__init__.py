from BlackJackPcg.Player.Dealer import Dealer
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Deck import Deck


class Game:

    def __init__(self, list_players=[]):
        self.d = Dealer()
        self.deck = Deck()
        self.deck.init_deck()
        if len(list_players) > 0:
            self.list_players = list_players
        else:
            self.list_players = []

    def get_dealer(self):
        return self.d

    def get_players(self):
        return self.list_players

    def get_deck(self):
        return self.deck

    def add_players(self, new_player_name):
        current_players = []
        if not isinstance(new_player_name, str):
            raise RuntimeError(
                "The user name passed to the player is not valid as it is {}".format(type(new_player_name)))
        for p in self.list_players:
            current_players.append(p.get_user_name())
        if len(current_players) > 0:
            if new_player_name in current_players:
                print('{} is already in our list - pick a new name if you still want to play'.format(new_player_name))
            else:
                self.list_players.append(Player(new_player_name))
        else:
            self.list_players.append(Player(new_player_name))

    def players_turn(self):
        # initial cards dealt already
        score_dict = {}
        # loop through players
        for player in self.list_players:
            # show points and cards
            number_of_cards = len(player.get_hand())
            print(player.get_points())
            player.show_n_cards(number_of_cards)
            # ask for game decision
            # add cards if wanted
            while player.pick_a_card_decision() == 1:
                dealt_cards = self.deck.get_next_cards(1)
                player.add_cards_to_hand(dealt_cards)
                print(player.get_hand()[-1])
                # check if bust
            if player.get_points() > 21:
                print('Players hand went bust')
                break
            elif player.get_points() == 21:
                print('Player has scored 21')
            else:
                print("{} chose to stand with score {} - moving onto next player's turn.\n".format(player.get_user_name(), player.get_points()))
            score_dict[player] = player.get_points()
        # repeat
        return score_dict