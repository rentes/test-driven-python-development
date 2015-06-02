# -*- coding: utf-8 -*-
"""Stock Alert Test"""

import unittest
from stock_alerter.stock import Stock


class StockTest(unittest.TestCase):
    """The Stock Test suite"""
    def test_price_of_a_new_stock_class_should_be_None(self):
        """Tests that a price of a new Stock should be None"""
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)
