from BlackJackPcg.Player.Dealer import Dealer
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Deck import Deck


class Game:

    def __init__(self, list_players=[]):
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.init_deck()
        self.score_dict = {}
        if len(list_players) > 0:
            self.list_players = list_players
        else:
            self.list_players = []

    def get_dealer(self):
        return self.dealer

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
        # loop through players
        for player in self.list_players:
            # show points and cards
            number_of_cards = len(player.get_hand())
            print('{} has a score of:'.format(player.get_user_name()), player.get_points())
            print('{} has a hand of:'.format(player.get_user_name()))
            player.show_n_cards(number_of_cards)
            print('Dealer cards:')
            self.dealer.show_n_cards(1)
            # ask for game decision
            # add cards if wanted
            while player.pick_a_card_decision() == 1:
                dealt_cards = self.deck.get_next_cards(1)
                player.add_cards_to_hand(dealt_cards)
                player.get_hand()[-1].show()
                # check if bust
                if player.get_points() > 21:
                    print('Players hand went bust')
                    break
            if player.get_points() == 21:
                print('Player has scored 21')
            else:
                print(
                    "{} chose to stand with score {} - moving onto next player's turn.\n".format(player.get_user_name(),
                                                                                                 player.get_points()))
            self.score_dict[player] = player.get_points()
        # repeat

    def dealer_turn(self):
        number_of_cards = len(self.dealer.get_hand())
        self.dealer.show_n_cards(number_of_cards)
        if min(self.score_dict.values()) > 21:
            print("The dealer won as all players had scores over 21.\n")
        else:
            while self.dealer.pick_a_card_decision() == 1:
                dealt_cards = self.deck.get_next_cards(1)
                self.dealer.add_cards_to_hand(dealt_cards)
                self.dealer.get_hand()[-1].show()

    def calculate_winner(self):
        dealer_score = self.dealer.get_points()
        for player, score in self.score_dict.items():
            if score > 21:
                print("{}'s hand went bust - dealer wins!".format(player.get_user_name()))
                self.dealer.winner_streak += 1
            elif score > dealer_score:
                print("{}'s hand scored {} so they win!".format(player.get_user_name(), score))
                player.winner_streak += 1
            else:
                print("{}'s hand scored {} so dealer wins with a score of {}!".format(player.get_user_name(), score, dealer_score))
                self.dealer.winner_streak += 1
