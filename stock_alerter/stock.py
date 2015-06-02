# -*- coding: utf-8 -*-
"""Stock Alert Application"""


class Stock:
    """The Stock class"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        """Updates the Stock with a timestamp and a price"""
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history.append(price)

    @property
    def price(self):
        """This method mimics the price attribute as existed before"""
        return self.price_history[-1] if self.price_history else None

    def is_increasing_trend(self):
        """Infers if a Stock has an increasing trend"""
        return self.price_history[-3] < \
            self.price_history[-2] < self.price_history[-1]
