from BlackJackPcg.Deck import Deck
# from BlackJackPcg.Card import Card
# from BlackJackPcg.Utils import CardUtils
from BlackJackPcg.Player import Player, Dealer

if __name__ == '__main__':
    d = Deck()
    d.init_deck()
    # d.print_deck()
    print()
    d.shuffle_deck()
    # d.print_deck()
    print()
    print(len(d.deck))
    p = Player(user_name='Andi')
    print(p.get_user_name())
    p.add_cards_to_hand(d.get_next_cards(2))
    p.show_n_cards(2)
    print('bot is Dealer')
    bot = Dealer()
    print(bot.get_user_name())
    bot.add_cards_to_hand(d.get_next_cards(1))
    bot.show_n_cards(1)
