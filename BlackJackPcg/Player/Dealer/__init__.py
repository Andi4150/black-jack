from BlackJackPcg.Player import Person


class Dealer(Person):

    def __init__(self):
        Person.__init__(self, user_name='Dealer')

    def pick_a_card_decision(self):
        if self.get_points() < 17:
            return True
        else:
            return False
