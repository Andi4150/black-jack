from BlackJackPcg.Player import Person


class Player(Person):

    def __init__(self, user_name):
        Person.__init__(self, user_name)

    def pick_a_card_decision(self):
        # initiate variables
        dec = None
        incorrect_input = True
        while incorrect_input:  # check if correct value given
            # collect input from user
            try:
                dec = int(input('Enter 0 if you do not want a new card, or 1 if you want a new card'))
                if dec == 1:
                    incorrect_input = False  # confirm exit of loop
                elif dec == 0:
                    incorrect_input = False  # confirm exit of loop
                else:
                    # currently no limit on number of tries to collect input
                    print("Incorrect input! Do you want a card? Please enter 0 for no, 1 for yes")
            # catch error if input invalid
            except ValueError as e:
                print("Incorrect input! Do you want a card? Please enter 0 for no, 1 for yes")
        return dec
