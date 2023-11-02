#!/usr/bin/env python3

# login_steps.py

"""
Description: This script describes the steps that can be used in the 'login.feature'
Author: @edenilsonpineda
Version: 1.0
Python version: 3.12.0
Dependencies: selenium
"""

from behave import given, when, then
from src.webdriver.webapp import webapp
from src.pages.TestPage import TestPage