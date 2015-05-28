# -*- coding: utf-8 -*-
"""Stock Alert Test"""

import unittest
from ..stock import Stock
from datetime import datetime


class StockTest(unittest.TestCase):
    """The Stock Test suite"""
    def test_price_of_a_new_stock_class_should_be_None(self):
        """Tests that a price of a new Stock should be None"""
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        # Following the Arrange-Act-Assert pattern
        goog = Stock("GOOG")  # Arrange
        goog.update(datetime(2015, 5, 28), price=10)  # Act
        self.assertEqual(10, goog.price)  # Assert

    def test_negative_price_should_throw_ValueError(self):
        """Tests that a price should not be negative
        """
        goog = Stock("GOOG")
        try:
            goog.update(datetime(2015, 5, 28), -1)
        except ValueError:
            return
        self.fail("ValueError was not raised")
