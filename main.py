from BlackJackPcg.Game import Game
from BlackJackPcg.Player.Players import Player

if __name__ == '__main__':
    game_flag = True
    g = Game()
    g.add_players('user_1')
    g.add_players('user_2')
    while game_flag:
        g.start_game()
        g.players_turn()
        g.calculate_winner()
        for player in g.get_players():
            print(player.get_user_name(), ' : ', player.get_winner_streak())
        game_flag = g.newGameDecision()

