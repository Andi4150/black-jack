# need a Class for game functionality

from BlackJackPcg.Deck import Deck
from BlackJackPcg.Player.Players import Player
from BlackJackPcg.Player.Dealer import Dealer


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

    def play_game(self):
        # add a dealer to the game
        self.add_dealer()
        # add a deck and shuffle
        self.deck.init()
        self.deck.shuffle()
        # for each player, including the dealer
        for p in self.get_players():
            p.add_cards_to_hand(self.deck.get_next_cards(2))
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
            champion = self.get_players()[winners[0]]
            print('Winner of game with 21 points is {}'.format(champion.get_username()))
            return 1
        else:
            champions = []
            for pl in winners:
                champions.append(self.get_players()[pl].get_username())
            print('Game is a draw between {}'.format(champions))
            return 1
        # Player is told what their 2 cards are and one of the dealer's cards.
        # Player given option to get more cards, if no next player,
        # if yes then add a card, and get points
        # if points > = 21 then next player, otherwise show cards and ask if want another

        # repeat for all players including dealer

        # calculate winner


