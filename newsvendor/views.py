from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from decimal import Decimal, ROUND_HALF_UP


class WelcomePage(Page):

    def is_displayed(self):
        return self.round_number == 1

    form_model = models.Player
    form_fields = ['check1low', 'check2low', 'check3low', 'check1high', 'check2high', 'check3high', 'check4', 'check5']

    def vars_for_template(self):

        if (Constants.margin == 'low'):
            marginlow = True

        else:
            marginlow = False

        return {
            'marginlow': marginlow,
            'margin': safe_json(Constants.margin),
            'label1l': 'If your order quantity is 600 and the demand realization is 700, what is your profit?',
            'label2l': 'If your order quantity is 600, what is the probability that your profit will be 936?',
            'label3l': 'If your order quantity is 750, what is the probability that your profit will be 806?',
            'label4': 'What happens if the demand is higher than your order quantity?',
            'label5': 'If your average profit over all the rounds is 1130, what is your monetary reward from Part 2?',
            'label1h': 'If your order quantity is 400 and the demand realization is 500, what is your profit?',
            'label2h': 'If your order quantity is 500, what is the probability that your profit will be 700?',
            'label3h': 'If your order quantity is 800, what is the probability that your profit will be 942?'
        }


class DecideOrderQuantity(Page):

    form_model = models.Player
    form_fields = ['orderquantity']

    def vars_for_template(self):

        return {
            'round': self.player.round_number,
            'margin': safe_json(Constants.margin)
        }

    def before_next_page(self):
        self.group.set_payoffs()
        self.group.end_timer()


class Results(Page):

    def vars_for_template(self):

        if (Constants.margin == 'low'):
            demand = self.session.vars['demand'][self.round_number-1]
            demandindex = (demand-500)/50

        else:
            demand = self.session.vars['demand'][self.round_number - 1]
            demandindex = (demand-300)/100

        if (demandindex < self.player.orderquantity):
            demandtext = "Because demand was lower than your inventory level, you have excess units in your inventory that you could not sell to the customers."
        elif (demandindex > self.player.orderquantity):
            demandtext = "Because demand was higher than your inventory level, you could not satisfy all the customer demand."
        else:
            demandtext = "Your order quantity exactly matched demand."

        return {
            'round': self.player.round_number,
            'margin': safe_json(Constants.margin),
            'orderqindex': safe_json(self.player.orderquantity),
            'demand': demand,
            'demandindex': safe_json(demandindex),
            'player_in_all_rounds': self.player.in_all_rounds(),
            'demandtext': demandtext
        }

    def before_next_page(self):
        self.group.start_timer()


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = models.Player
    form_fields = ['pecu','nonpecu','conflict']

    def vars_for_template(self):

        reward = Decimal(float(self.participant.payoff)/(1000*Constants.num_rounds)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        return {
            'averagepay': self.participant.payoff/Constants.num_rounds,
            'reward': reward
        }


page_sequence = [
    WelcomePage,
    DecideOrderQuantity,
    Results,
    FinalPage
]