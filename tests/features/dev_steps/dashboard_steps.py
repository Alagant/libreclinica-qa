#!/usr/bin/env python3

# dashboard_steps.py

"""
Description: This script describes the steps that can be used in the 'login.feature'
Author: @edenilsonpineda
Version: 1.0
Python version: 3.12.0
Dependencies: selenium
"""
import allure
from behave import then
from src.webdriver.webapp import webapp
from src.pages.DashboardPage import DashboardPage
from selenium.common.exceptions import InvalidSelectorException as SeleniumException


@then(u'Login is successful and dashboard is shown along with a Welcome message')
def step_impl_login_successful_and_welcome_message_is_shown(context):
    context.dashboard_page = DashboardPage(webapp.get_driver())
    try:
        allure.attach(context.testPage.screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        context.dashboard_page.validate_welcome_message_isShown()
    except SeleniumException:
        raise