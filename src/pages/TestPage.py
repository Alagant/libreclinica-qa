from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class TestPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_title(self, title):
        assert self.get_title() == title