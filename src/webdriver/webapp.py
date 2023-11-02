from selenium import webdriver
from urllib.parse import urljoin
from environment import BROWSER

class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance
    
    def __init__(self):
        if BROWSER.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif BROWSER.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
    
    def get_driver(self):
        return self.driver
    
    def load_website(self, url):
        self.driver.get(url)
    
    def checkIfComponentExists(self, component):
        assert component in self.driver.find_element_by_tag_name('body').text, \
        "Component {} not found on page".format(component)
    
    def terminate_driver(self):
        self.driver.close()
    
    def screenshot_as_png(self):
        self.driver.get_screenshot_as_png()
    
    def save_screenshot(self, path):
        self.driver.save_screenshot(path)


webapp = WebApp.get_instance()