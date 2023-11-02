from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    LOGIN_FORM_TITLE = (By.XPATH, "//*[@id='login']/form/h1")
    
    def __init__(self, driver):
        super().__init__(driver)

    def validate_login_form_isLoaded(self):
        self.verify_element_displayed(self.LOGIN_FORM_TITLE)
        assert self.get_element_text(self.LOGIN_FORM_TITLE) == "Login"