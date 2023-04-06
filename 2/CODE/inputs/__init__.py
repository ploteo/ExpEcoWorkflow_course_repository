import random

from otree.api import *


author = 'Matteo P.'
doc = """
A review of input formats
"""


class Constants(BaseConstants):
    name_in_url = 'inputs'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    display_value = models.IntegerField()
    # a simple radio button with two options (ordinal)
    input_radio = models.CharField(choices=['Odd', 'Even'], widget=widgets.RadioSelect)
    input_button = models.CharField()
    input_checker = models.CharField(
        choices=[["Even", 'Yes'], ["Odd", 'No']],
        widget=widgets.RadioSelectHorizontal,
        label="Is the number even?",
    )
    input_dropdown = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    input_radiosequence = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelectHorizontal
    )
    input_value = models.IntegerField(min=1, max=9)
    input_text = models.CharField()
    tab_1 = models.BooleanField(blank=True)
    tab_2 = models.BooleanField(blank=True)
    tab_3 = models.BooleanField(blank=True)
    tab_4 = models.BooleanField(blank=True)
    tab_5 = models.BooleanField(blank=True)
    tab_6 = models.BooleanField(blank=True)
    tab_7 = models.BooleanField(blank=True)
    tab_8 = models.BooleanField(blank=True)
    tab_9 = models.BooleanField(blank=True)

    input_slider = models.IntegerField(min=1, max=9)

    slider_1 = models.IntegerField()
    slider_2 = models.IntegerField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    display_value = random.randint(1, 9)  # this value will be diplayed
    print(display_value)
    for p in Subsession.get_players(subsession):
        p.display_value = display_value


# PAGES
class Radio(Page):
    form_model = 'player'
    form_fields = ['input_radio']


class Button(Page):
    form_model = 'player'
    form_fields = ['input_button']


class Checker(Page):
    form_model = 'player'
    form_fields = ['input_checker']


class Dropdown(Page):
    form_model = 'player'
    form_fields = ['input_dropdown']


class RadioSequence(Page):
    form_model = 'player'
    form_fields = ['input_radiosequence']


class Text(Page):
    form_model = 'player'
    form_fields = ['input_text']


class Value(Page):
    form_model = 'player'
    form_fields = ['input_value']


class Tabular(Page):
    form_model = 'player'
    form_fields = ['tab_1', 'tab_2', 'tab_3', 'tab_4', 'tab_5', 'tab_6', 'tab_7', 'tab_8', 'tab_9']


class Slider(Page):
    form_model = 'player'
    form_fields = ['input_slider']


class Slider_2(Page):
    form_model = 'player'
    form_fields = ['input_slider']

class Slider_3(Page):
    form_model = 'player'
    form_fields = ['slider_1', 'slider_2']



class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        pass


class Results(Page):
    pass


page_sequence = [
    Radio,
    Button,
    Checker,
    Dropdown,
    RadioSequence,
    Text,
    Value,
    Tabular,
    Slider,
    Slider_2,
    Slider_3
]
