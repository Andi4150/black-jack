from BlackJackPcg.Game import Game

if __name__ == '__main__':
    game_flag = True
    while game_flag:
        g = Game()
        g.__init__()
        input_count = 0
        n_players = g.number_of_players(input_count, 3)

        for i in range(n_players):
            p_detail = input('Please provide players name')
            g.add_player(p_detail)

        print(p.get_username() for p in g.get_players())
        print(g.get_deck())
        print(g.play_game())

        ng_count = 0
        new_game = g.new_game_decision(ng_count, 3)
        if new_game == 0:
            game_flag = False


