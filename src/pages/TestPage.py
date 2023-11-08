from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from src.utils.report import ReportGenerator

class TestPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_title(self, title):
        assert self.get_title() == title

    def generate_pdf_report(self, file_name, data):
        report_generator = ReportGenerator(file_name)
        report_generator.generate_report(data)