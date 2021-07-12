from BlackJackPcg.Player import Person
from BlackJackPcg import ProgramUtils


class Player(Person):

    def __init__(self, user_name):
        Person.__init__(self, user_name)
        self.pu = ProgramUtils()

    def pick_a_card_decision(self):
        # initiate variables
        dec = None
        incorrect_input = True
        count = 0
        while incorrect_input:  # check if correct value given
            if count == self.pu.get_num_of_tries():
                print("You tried the wrong value too many times.")
                return -1
            else:
                # collect input from user
                try:
                    dec = int(input('Enter 0 if you do not want a new card, or 1 if you want a new card'))
                    if dec == 1:
                        incorrect_input = False  # confirm exit of loop
                    elif dec == 0:
                        incorrect_input = False  # confirm exit of loop
                    else:
                        count += 1
                        print("Incorrect input! Do you want a card? Please enter 0 for no, 1 for yes")
                # catch error if input invalid
                except ValueError as e:
                    count += 1
                    print("Incorrect input! Do you want a card? Please enter 0 for no, 1 for yes")
        return dec
