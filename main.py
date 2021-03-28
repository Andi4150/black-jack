from BlackJackPcg.Deck import Deck
from BlackJackPcg.Card import Card
from BlackJackPcg.Utils import CardUtils

class Player:
    pass


if __name__ == '__main__':
    d = Deck()
    d.init_deck()
    d.print_deck()
    print()
    d.shuffle_deck()
    d.print_deck()
    print()
    print(len(d.deck))
    # c = Card(CardUtils.get_possible_suits()[0], CardUtils.get_possible_colors()[0], CardUtils.get_possible_numbers()[0])
    # c.show()
