# -*- coding: utf-8 -*-
"""Stock Alert Application"""
import bisect
import collections


PriceEvent = collections.namedtuple("PriceEvent", ["timestamp", "price"])


class Stock:
    """The Stock class"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        """Updates the Stock with a timestamp and a price"""
        if price < 0:
            raise ValueError("price should not be negative")
        bisect.insort_left(self.price_history, PriceEvent(timestamp, price))

    @property
    def price(self):
        """This method mimics the price attribute as existed before"""
        return self.price_history[-1].price if self.price_history else None

    def is_increasing_trend(self):
        """Infers if a Stock has an increasing trend"""
        return self.price_history[-3].price < \
            self.price_history[-2].price < self.price_history[-1].price
