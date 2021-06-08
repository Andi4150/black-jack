from BlackJackPcg.Utils import CardUtils


class Card:

    def __init__(self, suit, number):
        if number not in CardUtils.get_possible_numbers():
            raise RuntimeError("the number passed to the card is not valid")

        if suit not in CardUtils.get_possible_suits():
            raise RuntimeError("the suit passed to the card is not valid")

        self.suit = suit
        self.number = number

    def get_number(self):
        return self.number

    def get_suit(self):
        return self.suit

    def show(self):
        print("The card is: {}{}".format(self.number, self.suit))

    def get_points(self):
        # initiate points
        points = 0
        # check number of card
        n = self.get_number()
        # if face card then points are 10
        if n in ["J", "Q", "K"]:
            points = 10
        # if card is Ace then points are 11
        elif n == 'A':
            points = 11
        # otherwise points are number of card
        else:
            points = int(n)
        return points
