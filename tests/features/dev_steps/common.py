#!/usr/bin/env python3

# common.py

"""
Description: This script describe common steps that can be used in a '*.feature' e.g. Launch Web Browser, Open a web page, etc.
Author: @edenilsonpineda
Version: 1.0
Python version: 3.12.0
Dependencies: selenium
"""
import glob
import json
import os
import allure
from behave import given, when, then
from src.webdriver.webapp import webapp
from src.pages.TestPage import TestPage
from environment import BASE_URL, CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USERNAME, CONFLUENCE_URL, CONFLUENCE_PAGEID, CONFLUENCE_SPACE_ID
from pathlib import Path
import time
from src.utils.confluence_helper import ConfluenceHelper

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
        context.webapp.terminate_driver()
        assert False, "Test is failed in validate main page title"

@then(u'The login page is shown')
def step_impl_then_page_is_shown(context):
    try:
        assert True, context.testPage.verify_element_displayed('LibreClinica')
        allure.attach(context.testPage.screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    except:
        context.webapp.terminate_driver()
        assert False, "Test failed in login page"

@then(u'Take screenshot')
def step_impl_take_screenshot(context):
    try:
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = "screenshot-".join(timestamp)
        #png_bytes = context.webapp.screenshot_as_png()
        allure.attach(context.testPage.screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    except:
        allure.attach(context.testPage.screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        raise
    finally:
        context.webapp.terminate_driver()


@then(u'Close the browser')
def step_impl_close_browser(context):
    context.webapp.terminate_driver()

@then("Generate a PDF report")
def step_impl_generate_pdf_report(context):
    try:
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = "report-".__add__(timestamp).__add__(".pdf")
        file_path = "reports/".__add__(file_name)
        
        report_data = max(glob.glob(os.path.join('allure-results', '*.json')), key=os.path.getctime) #get the latest json file

        with open(report_data, 'r') as test_results:
            test_data = json.load(test_results)

        context.testPage.generate_pdf_report(file_path, test_data)
        context.latest_report = file_path
    except Exception as ex:
        print(f'An error ocurred while generating the PDF report {str(ex)}')
        raise

@then("Upload the PDF report to Confluence")
def step_impl_upload_pdf_to_confluence(context):
    try:
        latest_report = context.latest_report
        confluence_helper = ConfluenceHelper(confluence_url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_ACCESS_TOKEN)

        confluence_helper.upload_pdf_to_confluence(page_id=CONFLUENCE_PAGEID, pdf_file_path=latest_report, 
                            pdf_file_name=Path(latest_report).name, space=CONFLUENCE_SPACE_ID,
                                                   comment="Uploaded via automated test execution")
    except Exception as ex:
        print(f'An error ocurred while uploading the PDF report to Confluence {str(ex)}')
        raise
