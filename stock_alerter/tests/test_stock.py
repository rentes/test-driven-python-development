# -*- coding: utf-8 -*-
"""Stock Alert Test"""

from stock_alerter.stock import Stock
from datetime import datetime
import unittest


class StockTest(unittest.TestCase):
    """The Stock Test suite"""
    def setUp(self):
        """This method is called before every test method below is executed"""
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        """Tests that a price of a new Stock should be None"""
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        # Following the Arrange-Act-Assert pattern
        # Arrange is in the setUp method above
        self.goog.update(datetime(2015, 5, 28), price=10)  # Act
        self.assertEqual(10, self.goog.price)  # Assert

    def test_negative_price_should_throw_ValueError(self):
        """Tests that a price should not be negative
        """
        self.assertRaises(ValueError, self.goog.update,
                          datetime(2015, 5, 28), -1)

    def test_stock_price_should_give_the_latest_price(self):
        """After multiple updates, a Stock gives us the latest price"""
        self.goog.update(datetime(2015, 5, 28), price=10)
        self.goog.update(datetime(2015, 5, 28), price=8.4)
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)
