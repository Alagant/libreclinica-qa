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
from src.pages.LoginPage import LoginPage
from environment import ROOT_USERNAME, ROOT_PASSWORD

@then(u'Provide root user credentials')
def step_impl_enter_root_user_credentials(context):
    context.loginpage = LoginPage(webapp.get_driver())
    try:
        context.loginpage.enter_login_credentials(ROOT_USERNAME, ROOT_PASSWORD)
    except: 
        assert False, "Failed to login"

@then(u'Click on the Login button')
def step_impl_click_login_button(context):
    context.loginpage.click_login_button()


