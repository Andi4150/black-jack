# need a Class for game functionality

from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Player.Dealer import Dealer


# this was taken out of the class by recommendation of PyCharm
# is this because it is better suited to being a method which is applied within game
# rather than using the game properties tehmselves


def players_turn_actions(bust_hands, player, dealer):
    # Player is told what their 2 cards are and one of the dealer's cards.
    player.show_n_cards(len(player.get_hand()))
    dealer.show_n_cards(1)
    # Player given option to get more cards, if no next player,
    action = player.pick_a_card_decision()
    # if they want another card, add card, show points and cards
    if action == 1:
        player.add_cards_to_hand(1)
        points = player.get_points()
        player.show_n_cards(len(player.get_hand()))
        print(points)
        dealer.show_n_cards(1)
        # check if hand went bust, and otherwise repeat offer of card
        if points > 21:
            print('{} has gone bust and loses'.format(player.get_username))
            bust_hands += 1
            return False
        else:
            return True
    else:
        print('Next players turn')
        return False


class Game:

    def __init__(self):
        self.deck = Deck.init_deck()
        self.players = []

    def get_players(self):
        return self.players

    def get_deck(self):
        return self.deck

    def add_player(self, username):
        self.players.append(Player(username))

    def add_dealer(self):
        self.players.append(Dealer())

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
            print('Winner of game with 21 points is {}'.format(champion.get_username()))
            return 1
        else:
            champions = []
            # loop through indexes stored in winner and select the players who won
            for pl in winners:
                champions.append(self.get_players()[pl].get_username())
            print('Game is a draw between {}'.format(champions))
            return 1

    def calculate_winner(self):
        # initiate the variables
        max_score_pos = 0
        max_score = 0
        # loop through the players
        for i, p in enumerate(self.get_players()):
            # calculate the score
            score = p.get_points()
            print('{} scored {}'.format(p.get_username(), score))
            # check if hand can be considered
            if score > 21:
                print("{}'s hand wet bust".format(p.get_username()))
            # if score ok, check if it is highest
            elif max_score < score:
                max_score = score
                max_score_pos = i
            # otherwise skip this player
            else:
                pass  # is an else needed?
        # return the winning statement
        if max_score == 0:
            return 'something went wrong - nobody has won'
        else:
            return ('Winner of the game was {} with {} points'.format(self.get_players()[max_score_pos].get_username(),
                                                                      self.get_players()[max_score_pos].get_score()))

    def play_game(self):
        # add a dealer to the game
        self.add_dealer()
        # add a deck and shuffle
        self.deck.init()
        self.deck.shuffle()
        number_of_players = len(self.get_players())
        dealer = self.get_players()[number_of_players - 1]
        # for each player, including the dealer
        for p in self.get_players():
            p.add_cards_to_hand(self.deck.get_next_cards(2))
        # check for a winner
        result = self.check_if_dealt_hand_wins()
        if result == 1:
            return result  # return 1
        else:
            # continue with game - is an else needed??
            pass
        # check for hands going bust
        bust_hands = 0
        for i, p in enumerate(self.get_players()):
            # if everyone else has gone bust, final player (dealer) wins so don't bother with loop
            while bust_hands < number_of_players - 1:
                # check if it is still this players turn
                players_turn = True
                while players_turn:
                    # do the actions within a loop of a single players turn
                    players_turn = players_turn_actions(bust_hands, p, dealer)

        # calculate winner
        return self.calculate_winner()
