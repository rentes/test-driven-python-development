# -*- coding: utf-8 -*-
"""Stock Trend Test"""

import unittest
from ..stock import Stock
from datetime import datetime


class StockTrendTest(unittest.TestCase):
    """The Stock Trend Test suite"""
    def setUp(self):
        """This method is called before every test method below is executed"""
        self.goog = Stock("GOOG")

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        """Checks if a stock has an increasing trend"""
        timestamps = [datetime(2015, 5, 28), datetime(2015, 5, 29),
                      datetime(2015, 5, 30)]
        prices = [8, 10, 12]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        self.assertTrue(self.goog.is_increasing_trend())
