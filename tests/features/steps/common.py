#!/usr/bin/env python3

# common.py

"""
Description: This script describe common steps that can be used in a '*.feature' e.g. Launch Web Browser, Open a web page, etc.
Author: @edenilsonpineda
Version: 1.0
Python version: 3.12.0
Dependencies: selenium
"""
import allure
from behave import given, when, then
from src.webdriver.webapp import webapp
from src.pages.TestPage import TestPage
from environment import BASE_URL
from pathlib import Path
import time

@given(u'Launch the browser')
def step_impl_launch_browser(context):
    try:
        context.webapp = webapp.get_instance()
    except:
        ValueError("Cannot launch web browser")

@when(u'I open the LibreClinica application')
def step_impl_open_libreclinica_app(context):
    try:
        context.webapp.load_website(BASE_URL)
        context.testPage = TestPage(context.webapp.get_driver()) 
    except:
        context.webapp.terminate_driver()
        assert False, "Failed to open LibreClinica's webapp"

@when(u'Open the "{website}" website')
def step_impl_open_given_web_url(context, website):
    try:
        context.webapp.load_website(website)
        context.testPage = TestPage(context.webapp.get_driver()) # pass the driver to the TestPage
    except:
        context.webapp.terminate_driver()
        assert False, "Test failed to open website"

@then(u'The main page is opened and shows the title "{title}"')
def step_impl_then_page_is_shown(context, title):
    try:
        context.testPage.validate_title(title)
    except:
        context.testPage.terminate_driver()
        assert False, "Test is failed in validate main page title"

@then(u'The login page is shown')
def step_impl_then_page_is_shown(context):
    try:
        context.testPage.verify_element_displayed('LibreClinica')
        allure.attach(context.testPage.screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    except:
        context.testPage.terminate_driver()
        assert False, "Test failed in login page"

@then(u'Take screenshot')
def step_impl_take_screenshot(context):
    try:
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = "screenshot-".join(timestamp)
        #png_bytes = context.webapp.screenshot_as_png()
        allure.attach(context.testPage.screenshot_as_png(), name=file_name, attachment_type=allure.attachment_type.PNG)
    except:
        allure.attach(context.testPage.screenshot_as_png(), name="screenshot_on_failure", attachment_type=allure.attachment_type.PNG)
        raise
    finally:
        context.testPage.terminate_driver()