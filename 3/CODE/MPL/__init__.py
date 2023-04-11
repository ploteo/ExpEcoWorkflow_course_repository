import random
from otree.api import *

author = 'MP'
doc = """
MPL risk elicitation à la Holt&Laury
"""

class Constants(BaseConstants):
    name_in_url = 'MPL'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    A_h = 2.00
    A_l = 1.60
    B_h = 3.85
    B_l = 0.10

class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_2 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_3 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_4 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_5 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_6 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_7 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_8 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_9 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    HL_10 = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal
    )
    # This is needed for the instructions
    HL = models.CharField(
        choices=['A', 'B'], widget=widgets.RadioSelectHorizontal, blank =True
    )

    # These variables are collected in the final questionnaire
    sex = models.StringField(widget=widgets.RadioSelectHorizontal(), choices=['Male', 'Female', 'Other'])
    age = models.IntegerField(choices=range(18, 60, 1))
    comment = models.TextField(label="Your comment here:")
    like = models.IntegerField(choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    # Define here the methods associated to Players
    # this method is needed to compute payoffs

    # Variables needed for payoff
    row = models.IntegerField()
    drawn = models.IntegerField()
    choice = models.CharField()

# FUNCTIONS
def set_payoff_HL(player: Player):
    # *******************************************
    # select random row and random outcome
    # *******************************************
    player.row = random.randint(1, 10)
    # select one row randomly for payment (from module random)
    player.drawn = random.randint(1, 10)
    # select the number x that defines the outcome of the lottery (if x<=p, outcome is left A_h or B_h, otherwise A_l or A_h)
    # *******************************************
    # select choices in correspondence to random row
    # *******************************************
    choices = [player.HL_1,player.HL_2,player.HL_3,player.HL_4,player.HL_5,player.HL_6,player.HL_7,player.HL_8,player.HL_9,player.HL_10]
    # create a list with all choices of the player (see self)
    player.choice = choices[player.row - 1]
    # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
    # *******************************************
    # Compute here the payoffs
    # *******************************************
    if player.drawn <= player.row:
        # if the random number is smaller equal than the random row
        if player.choice == "A":  
            # if the choice was A
            player.payoff = float(Constants.A_h)
            # because HL_row is the same as p in the MPL
        else:
            # if the choice was B
            player.payoff = float(Constants.B_h)
    else:
        # if the random number is larger than the random row
        if player.choice == "A":  # A
            # if the choice was A
            player.payoff=float(Constants.A_l)
            # because HL_row is the same as p in the MPL
        else:
            player.payoff=float(Constants.B_l)
    # write the payoff to player.payoff
    print(player.payoff)
# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['HL']  # the demo MPL


class PageHL(Page):
    pass
    # which forms are needed from class player
    form_model = 'player'
    form_fields = [
        'HL_1',
        'HL_2',
        'HL_3',
        'HL_4',
        'HL_5',
        'HL_6',
        'HL_7',
        'HL_8',
        'HL_9',
        'HL_10',
    ]  # all 10 options
    # values that are to be displayed (dictionary)
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from constants and store them in a dictionary
        return {'A_h': Constants.A_h, 'A_l': Constants.A_l, 'B_h': Constants.B_h, 'B_l': Constants.B_l}

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # built-in method
        set_payoff_HL(player)  # see in models in Player class


class PageHL_2(Page):
    form_model = 'player'
    form_fields = [
        'HL_1',
        'HL_2',
        'HL_3',
        'HL_4',
        'HL_5',
        'HL_6',
        'HL_7',
        'HL_8',
        'HL_9',
        'HL_10'
    ]  # all 10 options

    @staticmethod
    def vars_for_template(player: Player):
        Lotteries = []
        for i in range(1, 11):
            Lotteries.append(
                [
                    i,
                    str(i) + "/10 of €" + str(Constants.A_h),
                    str(10 - i) + "/10 of €" + str(Constants.A_l),
                    "",
                    str(i) + "/10 of €" + str(Constants.B_h),
                    str(10 - i) + "/10 of €" + str(Constants.B_l),
                ]
            )
        return {'Lott': Lotteries}

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # built-in method
        set_payoff_HL(player)  # see in models in Player class


class OutcomeHL(Page):
    # values needed to inform subjects about the actual outcome
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'row': player.row,  # randomly chosen row
            'value': player.drawn,  # randomly chosen value to define outcome
            'choice': player.choice,  # actual choice
            'p_A_1': player.row,
            'p_A_2': 10 - player.row,
            'p_B_1': player.row,
            'p_B_2': 10 - player.row
        }



# the coreography of pages
page_sequence = [Instructions, PageHL, OutcomeHL]
