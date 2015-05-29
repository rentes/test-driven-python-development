# -*- coding: utf-8 -*-
"""Price Rule Test"""

import unittest
from ..stock import Stock
from ..rule import PriceRule
from datetime import datetime
from builtins import classmethod


class PriceRuleTest(unittest.TestCase):
    """The PriceRule Test suite"""
    @classmethod
    def setUpClass(cls):
        """This method is called before every test method below is executed"""
        goog = Stock("GOOG")
        goog.update(datetime(2015, 5, 28), 11)
        cls.exchange = {"GOOG": goog}

    def test_a_PriceRule_matches_when_it_meets_the_condition(self):
        """Tests if a PriceRule matches when it meets the condition"""
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_condition_is_not_met(self):
        """Tests if a PriceRule is False if the condition is not met"""
        rule = PriceRule("GOOG", lambda stock: stock.price < 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange(self):
        """Tests if a PriceRule is False if the stock is not in the exchange"""
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet(self):
        """
        Tests if a PriceRule is False if the stock hasn't got an update yet
        """
        self.exchange["AAPL"] = Stock("AAPL")
        rule = PriceRule("AAPL", lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_only_depends_on_its_stock(self):
        """Tests if a PriceRule only depends on its stock"""
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        self.assertEqual({"MSFT"}, rule.depends_on())
