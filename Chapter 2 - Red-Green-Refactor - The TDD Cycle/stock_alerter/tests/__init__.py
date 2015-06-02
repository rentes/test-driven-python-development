# -*- coding: utf-8 -*-
"""Initialise the stock alerter tests package"""
import os
import sys

PACKAGE_PARENT = '..'
TESTS_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(TESTS_DIR, PACKAGE_PARENT)))
