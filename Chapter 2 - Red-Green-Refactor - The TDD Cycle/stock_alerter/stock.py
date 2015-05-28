# -*- coding: utf-8 -*-
"""Stock Alert Application"""


class Stock:
    """The Stock class"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None

    def update(self, timestamp, price):
        """Updates the Stock with a timestamp and a price"""
        if price < 0:
            raise ValueError("price should not be negative")
        self.price = price
