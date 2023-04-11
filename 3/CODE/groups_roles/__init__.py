import random
from otree.api import *

author = 'MP'

doc = """
Matching and roles:

Constant type and constant matching (CT/CM)
Varying type and constant matching (VT/CM)
Constant type and varying matching (CT/VM)
Varying type and varying matching (VT/VM)

Uncomment the desired mathing protocol
"""

#--------------------------------------------
# MODELS
#--------------------------------------------


############################################################
# 1) Constant Type and Constant Matching (CT/CM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = "Constant Type and Constant Matching (CT/CM)"

# class Subsession(BaseSubsession):
#     pass

# def creating_session(subsession):
#     if subsession.round_number == 1:  # this way we get a fixed role across repetitions
#         subsession.group_randomly()
#         print(subsession.get_group_matrix())
#         for g in subsession.get_groups():
#             for p in g.get_players():
#                 if p.id_in_group % 2 == 0:
#                     p.type = 'BLUE'
#                     p.value = cu(10) # assign the corresponding value
#                 else:
#                     p.type = 'GREEN'
#                     p.value = cu(0)# assign the corresponding value
#     else:
#         subsession.group_like_round(1)
#         for g in subsession.get_groups():
#             for p in g.get_players():
#                 p.type = p.in_round(subsession.round_number-1).type
#                 p.value = p.in_round(subsession.round_number-1).value
# #---------------------------------------------------------------------

# # print some information
#     print(subsession.round_number)
#     print(subsession.get_group_matrix())
#     for p in subsession.get_players():
#         for i in p.in_previous_rounds():
#             print(i.id_in_subsession,i.type)

# # To get values of the other in the group
#     for p in subsession.get_players():
#         for i in p.get_others_in_group():
#             p.id_oth=i.id_in_subsession
#             p.type_oth=i.type
#             p.value_oth=i.value


############################################################
# END OF Constant type and constant matching (partner)
############################################################

############################################################
# 2) Varying Type and Constant Matching (VT/CM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = " Varying Type and Constant Matching (VT/CM)"

# import random
# class Subsession(BaseSubsession):
#     pass

# def creating_session(subsession):
#     if subsession.round_number == 1: # this way we get a fixed role across repetitions
#         subsession.group_randomly()# built-in function
#         print(subsession.get_group_matrix())
#         rdm=random.randint(0, 1)
#         print(rdm)
#         for g in subsession.get_groups():
#             for p in g.get_players():
#                 if rdm==1: #this way we randomize role accordin to id in group
#                     if p.id_in_group % 2 == 0:
#                         p.type = 'BLUE'
#                         p.value = cu(10)# assign the corresponding value
#                     else:
#                         p.type = 'GREEN'
#                         p.value = cu(0)   # assign the corresponding value
#                 else:
#                     if p.id_in_group % 2 == 0:
#                         p.type = 'GREEN'
#                         p.value = cu(0)
#                     else:
#                         p.type = 'BLUE'
#                         p.value = cu(10)
#     else:
#         subsession.group_like_round(1)
#         rdm=random.randint(0, 1)
#         print(rdm)
#         for g in subsession.get_groups():
#             for p in g.get_players():
#                 if rdm==1: #this way we randomize role accordin to id in group
#                     if p.id_in_group % 2 == 0:
#                         p.type = 'BLUE'
#                         p.value = cu(10)
#                     else:
#                         p.type = 'GREEN'
#                         p.value = cu(0)
#                 else:
#                     if p.id_in_group % 2 == 0:
#                         p.type = 'GREEN'
#                         p.value = cu(0)
#                     else:
#                         p.type = 'BLUE'
#                         p.value = cu(10)
#         print(subsession.get_group_matrix())
# #---------------------------------------------------------------------

# # print some information (just a check)
#         print(subsession.round_number)
#         print(subsession.get_group_matrix())
#         for p in subsession.get_players():
#             for i in p.in_previous_rounds():
#                 print(i.id_in_subsession, i.type)

# # To get values of the other in the group
#     for p in subsession.get_players():
#         for i in p.get_others_in_group():
#             p.id_oth = i.id_in_subsession
#             p.type_oth = i.type
#             p.value_oth = i.value

############################################################
# END OF  Varying type and constant matching (partner)
############################################################

############################################################
# 3) Constant Type and Varying Matching (CT/VM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = "Constant Type and Varying Matching (CT/VM)"

# class Subsession(BaseSubsession):
#     pass

# def creating_session(subsession):
#     subsession.group_randomly(fixed_id_in_group=True)# built-in function
#     print(subsession.get_group_matrix())
#     for g in subsession.get_groups():
#         for p in g.get_players():
#             if p.id_in_group % 2 == 0:
#                 p.type = 'BLUE'
#                 p.value = cu(10)
#             else:
#                 p.type = 'GREEN'
#                 p.value = cu(0)

# #To assign values in each round, the blue get 10 and the green get 0
#     for p in subsession.get_players():
#         if p.type == 'BLUE':
#             p.value = cu(10)
#         else:
#             p.value = cu(0)
# #---------------------------------------------------------------------

# # print some information (just a check)
#         print(subsession.round_number)
#         print(subsession.get_group_matrix())
#         for p in subsession.get_players():
#             for i in p.in_previous_rounds():
#                 if subsession.round_number==Constants.num_rounds:
#                     print(i.id_in_subsession, i.type)

# # To get values of the other in the group
#     for p in subsession.get_players():
#         for i in p.get_others_in_group():
#             p.id_oth = i.id_in_subsession
#             p.type_oth = i.type
#             p.value_oth = i.value


############################################################
# END Constant type and varying matching
############################################################

############################################################
# 4) Varying Type and Varying Matching (VT/VM)
############################################################

class Constants(BaseConstants):
    name_in_url = 'groups_roles'
    players_per_group = 2
    num_rounds = 10
    matching = "Varying Type and Varying Matching (VT/VM)"

class Subsession(BaseSubsession):
    pass

#--------------------------------------------------------
# Create here the function that takes care of the matching
#--------------------------------------------------------

def creating_session(subsession):
    subsession.group_randomly()  # built-in function
    rdm = random.randint(0, 1)
    print(rdm)
    for g in subsession.get_groups():
        for p in g.get_players():
            if rdm == 1:  # this way we randomize role according to id in group
                if p.id_in_group % 2 == 0:
                    p.type = 'BLUE'
                    p.value = cu(10)
                else:
                    p.type = 'GREEN'
                    p.value = cu(0)
            else:
                if p.id_in_group % 2 == 0:
                    p.type = 'GREEN'
                    p.value = cu(0)
                else:
                    p.type = 'BLUE'
                    p.value = cu(10)
    print(subsession.get_group_matrix())

#---------------------------------------------------------------------

# print some information (just a check)

    print(subsession.round_number)
    print(subsession.get_group_matrix())
    for p in subsession.get_players():
        for i in p.in_previous_rounds():
            print(i.id_in_subsession, i.type)

# To get values of the other in the group
        for p in subsession.get_players():
            for i in p.get_others_in_group():
                p.id_oth = i.id_in_subsession
                p.type_oth = i.type
                p.value_oth = i.value

############################################################
# END Varying type and varying matching
############################################################


class Group(BaseGroup):
    pass

# needed to store values

class Player(BasePlayer):
    type = models.StringField()
    value = models.CurrencyField()
    id_oth = models.IntegerField()
    type_oth = models.StringField()
    value_oth = models.CurrencyField()

#--------------------------------------------
# PAGES
#--------------------------------------------

class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            round = player.round_number,
            player_current_id = player.id_in_subsession,
            player_current_type = player.type,
            player_current_value = player.value,
            player_current_id_oth = player.id_oth,
            player_current_type_oth = player.type_oth,
            player_current_value_oth = player.value_oth      
        )
    

page_sequence = [MyPage]
