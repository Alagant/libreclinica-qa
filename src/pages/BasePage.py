#!/usr/bin/env python3

# BasePage.py

"""
Description: It contains common action methods and utilities for pages interactions
             every other Page type-class should inherit from this BasePage class.
Author: @edenilsonpineda
Version: 1.0
Python version: 3.12.0
Dependencies: selenium
"""


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_c
from selenium.common.exceptions import InvalidSelectorException as SeleniumException
from environment import DEFAULT_TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, float(DEFAULT_TIMEOUT)).until(expected_c.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except SeleniumException:
            print("Can't click on element")
    
    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, float(DEFAULT_TIMEOUT)).until(expected_c.visibility_of_element_located(by_locator)).send_keys(text)
        except SeleniumException:
            print("Can't interact with element of type: (input)")

    def get_title(self):
        return self.driver.title
    
    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, float(DEFAULT_TIMEOUT)).until(expected_c.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except SeleniumException:
            return False
    
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_c.visibility_of_element_located(by_locator))
        return element.text
    
    def screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()
    
    def wait_for_element_and_clickit(self, by_locator):
        element = WebDriverWait(self.driver, float(DEFAULT_TIMEOUT)).until(expected_c.element_to_be_clickable(by_locator))
        element.click()
        WebDriverWait(self.driver, float(15000))
    
    def wait_for_element_and_send_keys(self, by_locator, text): 
        element = WebDriverWait(self.driver, float(DEFAULT_TIMEOUT)).until(expected_c.element_to_be_clickable(by_locator))
        element.send_keys(text)
    
