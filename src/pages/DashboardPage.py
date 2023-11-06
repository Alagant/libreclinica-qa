from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    WELCOME_MESSAGE_ALERT = (By.XPATH, "//*[@id='sidebar_Alerts_open']/td/div/div")

    """Constructor of LoginPage class"""
    def __init__(self, driver):
        super().__init__(driver)

    def validate_welcome_message_isShown(self):
        assert True, str(self.get_element_text(self.WELCOME_MESSAGE_ALERT)).__contains__('Welcome to LibreClinica')
