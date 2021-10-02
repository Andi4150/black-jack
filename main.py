from BlackJackPcg.Game import Game
from BlackJackPcg.Player.Players import Player

if __name__ == '__main__':
    game_flag = True
    new_user_input_count = 0
    new_player_decision = 1
    g = Game()
    g.new_player_decision_function()
    # add more commentary if needed
    # check for when things go wrong
    while game_flag:
        g.start_game()
        g.players_turn()
        g.dealer_turn()
        g.calculate_winner()
        for player in g.get_players():
            print(player.get_user_name(), ' : ', player.get_winner_streak())
        game_flag = g.newGameDecision()

