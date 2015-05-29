# -*- coding: utf-8 -*-
"""Price Rule"""


class PriceRule:
    """PriceRule is a rule that triggers when a stock price
    satisfies a condition (usually greater, equal or lesser
    than a given value)"""

    def __init__(self, symbol, condition):
        self.symbol = symbol
        self.condition = condition

    def matches(self, exchange):
        """
        Returns True or False depending on whether the rule is matched or not
        """
        try:
            stock = exchange[self.symbol]
        except KeyError:
            return False
        return self.condition(stock) if stock.price else False

    def depends_on(self):
        """Returns which stocks updates the rule depends on"""
        return {self.symbol}
