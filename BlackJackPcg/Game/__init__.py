from BlackJackPcg import ProgramUtils
from BlackJackPcg.Player.Dealer import Dealer
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Deck import Deck


class Game:

    def __init__(self, list_players=[]):
        self.dealer = Dealer()
        self.deck = Deck()
        self.score_dict = {}
        self.pu = ProgramUtils()
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

    def start_game(self):
        print('New game starting...')
        self.deck.init_deck()
        print('Shuffling deck')
        self.deck.shuffle_deck()
        for player in self.get_players():
            print('New hands dealt...')
            player.reset_hand()
            player.add_cards_to_hand(self.deck.get_next_cards(2))
        self.dealer.add_cards_to_hand(self.deck.get_next_cards(2))

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
            elif dealer_score > 21:
                print('dealers hand went bust - {} wins with score of {}'.format(player.get_user_name(), score))
                player.winner_streak += 1
            elif score > dealer_score:
                print("{}'s hand scored {} so they win!".format(player.get_user_name(), score))
                player.winner_streak += 1
            else:
                print("{}'s hand scored {} so dealer wins with a score of {}!".format(player.get_user_name(), score,
                                                                                      dealer_score))
                self.dealer.winner_streak += 1

    def newGameDecision(self):
        new_game = False
        incorrect_input = True
        count = 0
        while incorrect_input:  # check if correct value given
            if count == self.pu.get_num_of_tries():
                print("You tried the wrong value too many times.")
                return -1
            else:
                # collect input from user
                try:
                    dec = int(input('Enter 0 if you do not want to play again, or 1 if you want to play again'))
                    if dec == 1:
                        new_game = True
                        incorrect_input = False  # confirm exit of loop
                    elif dec == 0:
                        incorrect_input = False  # confirm exit of loop
                    else:
                        count += 1
                        print("Incorrect input! Use 1 or 0")
                # catch error if input invalid
                except ValueError as e:
                    count += 1
                    print("Incorrect input! Use 1 or 0")
        return new_game
