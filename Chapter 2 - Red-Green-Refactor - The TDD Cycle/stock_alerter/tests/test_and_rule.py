# -*- coding: utf-8 -*-
"""AndRule Test"""

import unittest
from ..stock import Stock
from datetime import datetime
from ..rule import PriceRule, AndRule


class AndRuleTest(unittest.TestCase):
    """The AndRule Test suite"""
    @classmethod
    def setUpClass(cls):
        """This method is called before every test method below is executed"""
        goog = Stock("GOOG")
        goog.update(datetime(2015, 5, 28), 8)
        goog.update(datetime(2015, 5, 29), 10)
        goog.update(datetime(2015, 5, 30), 12)
        msft = Stock("MSFT")
        msft.update(datetime(2015, 5, 28), 10)
        msft.update(datetime(2015, 5, 29), 10)
        msft.update(datetime(2015, 5, 30), 12)
        redhat = Stock("RHT")
        redhat.update(datetime(2015, 5, 28), 7)
        cls.exchange = {"GOOG": goog, "MSFT": msft, "RHT": redhat}

    def test_an_AndRule_matches_if_all_component_rules_are_true(self):
        """Tests if an AndRule matches if all component rules are True"""
        rule = AndRule(PriceRule("GOOG", lambda stock: stock.price > 8),
                       PriceRule("MSFT", lambda stock: stock.price > 10))
        self.assertTrue(rule.matches(self.exchange))
