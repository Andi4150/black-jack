from BlackJackPcg.Game import Game

if __name__ == '__main__':
    game_flag = True
    while game_flag:
        g = Game(['user_1'])
        g.__init__()
        g.get_players()
        g.get_dealer()
        g.get_deck()