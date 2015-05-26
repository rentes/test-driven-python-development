# -*- coding: utf-8 -*-
"""Stock Alert Test Application"""

import unittest


class StockTest(unittest.TestCase):
    """Tests that a price of a new Stock should be None"""
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock("GOOG")
        self.assertIsNone(stock.price)

if __name__ == "__main__":
    unittest.main()
