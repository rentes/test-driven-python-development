# -*- coding: utf-8 -*-
"""Stock Alert Application"""


class Stock:
    """The Stock class"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None

    def update(self, timestamp, price):
        self.price = price