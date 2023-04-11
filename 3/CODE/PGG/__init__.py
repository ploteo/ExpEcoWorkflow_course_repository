from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'PGG'
    players_per_group = 3
    num_rounds = 4
    endowment = cu(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_choices = models.CurrencyField()  # for VC is withdrawals, for CP is contributions
    individual_share = models.CurrencyField()
    total_earnings = models.CurrencyField()


class Player(BasePlayer):
    choice = models.CurrencyField(min=0, max=Constants.endowment)  #ì
    payoff_final = models.CurrencyField()
    # to store final payoff


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:  # this way we get a fixed role across repetitions
        subsession.group_randomly()
    else:
        subsession.group_like_round(1)


def set_payoffs(group: Group):
    players = group.get_players()
    choices = [p.choice for p in players]
    group.total_choices = sum(choices)
    group.total_earnings = group.total_choices * Constants.multiplier
    group.individual_share = group.total_earnings / Constants.players_per_group
    for p in players:
        p.payoff = Constants.endowment - p.choice + group.individual_share

    # compute final payoff (as sum of all payoffs)
    if group.round_number == Constants.num_rounds:
        for p in players:
            hist = p.in_all_rounds()
            p.payoff_final = sum([g.payoff for g in hist])
            # print(p.payoff_final)

# PAGES
class Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'common_proj': Constants.endowment * Constants.players_per_group,
        }

class Contribute(Page):
    form_model = 'player'
    form_fields = ['choice']
    # the player will fill out the field choice and it will be saved in player model (see models)
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'round_number': player.round_number,
            'endowment': Constants.endowment,
        }


class ResultsWaitPage(WaitPage):
    # If you have a WaitPage in your sequence of pages, then oTree waits until all players in the group have arrived at that point in the sequence, and then all players are allowed to proceed.
    after_all_players_arrive = 'set_payoffs'
    # see method 'set_payoffs' in class Group in models.py
    # payoffs are computed here


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # retrieve historical values
        hist = player.in_previous_rounds()
        # for the dynamic history graph
        history_contrib = [g.group.total_choices for g in hist]
        history_contrib = safe_json(history_contrib)
        # history data
        data_hist = [
            [g.choice for g in hist],
            [g.group.individual_share for g in hist],
            [g.payoff for g in hist]
        ]
        print(data_hist)
        # organize them
        table_hist = []
        for j in range(0, (player.round_number-1)):  # start from 
            t = []
            t.append(j+1)#round
            for i in data_hist:
                t.append(i[j])
            table_hist.append(t)
        print(table_hist)
        amount_kept = Constants.endowment - player.choice
        return {
            'history_contrib': history_contrib,
            'round_number': player.round_number,
            'kept': amount_kept,
            # old values
            'table_hist': table_hist
        }


class FinalResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        return {'payoff_final': player.payoff_final}  #


page_sequence = [Instructions, Contribute, ResultsWaitPage, Results, FinalResults]
