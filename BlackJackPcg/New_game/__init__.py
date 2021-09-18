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
        n_players = 0
        input_count = 0
        while input_count < self.pu.get_num_of_tries():
            if input_count == self.pu.get_num_of_tries()-1:
                print("You have one more try before no players are added to the game.")
            try:
                n_players = int(input('How many players will join the game, 1 or 2?'))
                return n_players
            except ValueError as e:
                input_count += 1
                print("Incorrect input! How many players are there, 1 or 2?")
        return n_players

    def add_player(self, new_user):
        list_of_players = self.get_players()
        if new_user in list_of_players:
            print('{} is already in the game. No-one has been added'.format(new_user))
        else:
            print('Adding {} to the list of players'.format(new_user))
            list_of_players.append(new_user)
        return list_of_players

    def check_winner(self):
        # initiate variables
        winner_index_list = []
        score_21_list = []
        dealers_score = self.get_dealer().get_points()
        if dealers_score > 21:
            print("Dealer's hand went bust")
        # loop through the players
        for i, p in enumerate(self.get_players()):
            # calculate the score
            score = p.get_points()
            print('{} scored {}'.format(p.get_user_name(), score))
            # check if hand can be considered
            if score > 21:
                print("{}'s hand went bust".format(p.get_user_name()))
                # remove from list of players
                self.get_players().remove(p)
            # if score ok, check if it is highest
            elif dealers_score < score:
                winner_index_list.append(i)
            # otherwise skip this player
            elif dealers_score == score:
                print("{}'s hand scored same as Dealer - no winner!".format(p.get_user_name()))
        return winner_index_list

    def check_for_21_score(self):
        # initiate variables
        score_21_list = []
        dealers_score = self.get_dealer().get_points()
        if dealers_score == 21:
            print("Dealer's hand went bust")
            score_21_list.append(-1)
        # loop through the players
        for i, p in enumerate(self.get_players()):
            # calculate the score
            score = p.get_points()
            print('{} scored {}'.format(p.get_user_name(), score))
            # check if hand can be considered
            if score > 21:
                print("{}'s hand went bust".format(p.get_user_name()))
                # remove from list of players
                self.get_players().remove(p)
            # if score ok, check if it is highest
            elif score == 21:
                score_21_list.append(i)
        return score_21_list

    def play_game(self):
        # shuffle deck
        self.get_deck().shuffle_deck()
        # deal cards to players
        d = self.get_dealer()
        d.add_cards_to_hand(1)
        for p in self.get_players():
            p.add_cards_to_hand(2)
        # check for winner/bust
        if len(self.check_for_21_score) > 0:
            for winner in self.check_for_21_score():
                if winner == -1:
                    print('The dealer won with score of 21')
                else:
                    print('The winner(s) is {} with a score of 21'.format(self.get_players()[winner]))
            return 0
        else:
            print('No-one reached 21 with their dealt hand')
        for p in self.get_players():
            # collect decision from current player
            players_turn = True
            # repeat until bust or decision is no
            while players_turn:
                if p.pick_a_card_decision() == 1:
                    p.add_cards_to_hand(1)
                    # check if bust
                    if p.get_points > 21:
                        print("{}'s hand went bust".format(p.get_user_name()))
                        # remove from list of players
                        self.get_players().remove(p)
                        players_turn = False
                else:
                    players_turn = False
        # repeat for dealer
        if d.pick_a_card_decision() == 1:
            d.add_cards_to_hand(1)
            # check if bust
            if d.get_points > 21:
                print("Dealer's hand went bust")
        # check for winners
        list_of_winner_indexes = self.check_winner()
        if list_of_winner_indexes > 0:
            for champion in list_of_winner_indexes:
                print('{} beat the dealer!'.format(self.get_players()[champion]))
        