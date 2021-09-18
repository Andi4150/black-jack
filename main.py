from BlackJackPcg.Game import Game
from BlackJackPcg.Player.Players import Player

if __name__ == '__main__':
    game_flag = True
    while game_flag:
        g = Game()
        g.add_players('user_1')
        g.add_players('user_2')
        g.deck.shuffle_deck()
        for player in g.get_players():
            dealt_cards = g.deck.get_next_cards(2)
            player.add_cards_to_hand(dealt_cards)
        dealt_cards = g.deck.get_next_cards(2)
        g.dealer.add_cards_to_hand(dealt_cards)
        scores = g.players_turn()
        print(scores)
        game_flag = False

