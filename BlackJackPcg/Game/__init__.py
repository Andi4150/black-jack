# need a Class for game functionality

from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Player.Dealer import Dealer


# this was taken out of the class by recommendation of PyCharm
# is this because it is better suited to being a method which is applied within game
# rather than using the game properties themselves


def players_turn_actions(bust_hands, player, dealer, deck):
    # Player is told what their 2 cards are and one of the dealer's cards.
    print("{} points are {} from the following cards:".format(player.get_user_name(), player.get_points()))
    player.show_n_cards(len(player.get_hand()))
    if player != dealer:
        print('One of Dealers cards are:')
        dealer.show_n_cards(1)
    # Player given option to get more cards, if no next player,
    action = player.pick_a_card_decision()
    # if they want another card, add card, show points and cards
    if action == 1:
        player.add_cards_to_hand(deck.get_next_cards(1))
        points = player.get_points()
        # check if hand went bust, and otherwise repeat offer of card
        if points > 21:
            print('{} has gone bust and loses'.format(player.get_user_name()))
            bust_hands += 1
            return False
        else:
            return True
    else:
        return False


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.init_deck()
        self.players = []

    def get_players(self):
        return self.players

    def get_deck(self):
        return self.deck

    def add_player(self, username):
        self.players.append(Player(username))

    def add_dealer(self):
        self.players.append(Dealer())

    def number_of_players(self, input_count, limit):
        n_players = 0
        while input_count < limit:
            try:
                n_players = int(input('How many players are there, 1 or 2?'))
                return n_players
            except ValueError as e:
                input_count += 1
                print("Incorrect input! How many players are there, 1 or 2?")
        return n_players

    def new_game_decision(self, ng_count, limit):
        if ng_count < limit:
            try:
                new_game = int(input('Play again? 1 for yes, 0 for no'))
                return new_game
            except ValueError as e:
                ng_count += 1
                print("Incorrect input! Play again? 1 for yes, 0 for no")
        else:
            return 0


    def check_if_dealt_hand_wins(self):
        # check for a winner
        winners = []
        for i, p in enumerate(self.get_players()):
            score = p.get_points()
            if score == 21:
                winners.append(i)
        # If the player's cards add up to 21 and the dealer's two cards do not then player wins.
        # If player and dealer both have a sum of 21 then its a draw.
        # If only the dealer's cards sum to 21 then player loses.
        if len(winners) == 0:
            print('No-one has a hand adding up to 21 yet')
            return 0
        elif len(winners) == 1:
            # use index stored in winners to select teh player from list of players who won
            champion = self.get_players()[winners[0]]
            print('Winner of game with 21 points is {}'.format(champion.get_user_name()))
            return 1
        else:
            champions = []
            # loop through indexes stored in winner and select the players who won
            for pl in winners:
                champions.append(self.get_players()[pl].get_user_name())
            print('Game is a draw between {}'.format(champions))
            return 1

    def calculate_winner(self):
        # initiate the variables
        max_score_pos = 0
        max_score = 0
        draw_score_pos = []
        # loop through the players
        for i, p in enumerate(self.get_players()):
            # calculate the score
            score = p.get_points()
            print('{} scored {}'.format(p.get_user_name(), score))
            # check if hand can be considered
            if score > 21:
                print("{}'s hand went bust".format(p.get_user_name()))
            # if score ok, check if it is highest
            elif max_score < score:
                max_score = score
                max_score_pos = i
            # otherwise skip this player
            elif max_score == score:
                draw_score_pos = [max_score_pos, i]
            # otherwise skip this player
            else:
                pass  # is an else needed?
        # return the winning statement
        if max_score == 0:
            return 'something went wrong - nobody has won'
        else:
            if len(draw_score_pos) == 0:
                return (
                    'Winner of the game was {} with {} points'.format(self.get_players()[max_score_pos].get_user_name(),
                                                                      self.get_players()[max_score_pos].get_points()))
            else:
                return ('Winners of the game are {} with {} points'.format(
                    self.get_players()[draw_score_pos[0]].get_user_name(),
                    self.get_players()[draw_score_pos[1]].get_user_name(),
                    self.get_players()[max_score_pos].get_points()))

    def play_game(self):
        # add a dealer to the game
        self.add_dealer()
        # add a deck and shuffle
        self.deck.shuffle_deck()
        number_of_players = len(self.get_players())
        dealer = self.get_players()[number_of_players - 1]
        # for each player, including the dealer
        for p in self.get_players():
            p.add_cards_to_hand(self.deck.get_next_cards(2))
        # check for a winner
        result = self.check_if_dealt_hand_wins()
        if result == 1:
            return result  # return 1
        # check for hands going bust
        bust_hands = 0
        for i, p in enumerate(self.get_players()):
            print("It is now {}'s go".format(p.get_user_name()))
            # if everyone else has gone bust, final player (dealer) wins so don't bother with loop
            if bust_hands < number_of_players - 1:
                # check if it is still this players turn
                players_turn = True
                while players_turn:
                    # do the actions within a loop of a single players turn
                    players_turn = players_turn_actions(bust_hands, p, dealer, self.deck)

        # calculate winner
        return self.calculate_winner()
