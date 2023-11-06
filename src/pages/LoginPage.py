from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN_FORM_TITLE = (By.XPATH, "//*[@id='login']/form/h1")
    LOGIN_FORM_USERNAME_INPUT_TEXT = (By.ID, "username")
    LOGIN_FORM_PASSWORD_INPUT_TEXT = (By.ID, "j_password")
    LOGIN_FORM_SUBMIT_BUTTON = (By.XPATH, "//*[@id='login']/form/input")

    """Constructor of LoginPage class"""
    def __init__(self, driver):
        super().__init__(driver)

    def validate_login_form_isLoaded(self):
        self.verify_element_displayed(self.LOGIN_FORM_TITLE)
        assert self.get_element_text(self.LOGIN_FORM_TITLE) == "Login"

    def enter_login_credentials(self, user, password):
        self.wait_for_element_and_send_keys(self.LOGIN_FORM_USERNAME_INPUT_TEXT, user)
        self.wait_for_element_and_send_keys(self.LOGIN_FORM_PASSWORD_INPUT_TEXT, password)

    def click_login_button(self):
        self.wait_for_element_and_clickit(self.LOGIN_FORM_SUBMIT_BUTTON)
