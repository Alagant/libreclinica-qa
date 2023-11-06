from selenium import webdriver
from urllib.parse import urljoin
from environment import BROWSER, HEADLESS, DRIVER_PATH, DEFAULT_TIMEOUT
from selenium.webdriver.common.by import By


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        options = None
        if BROWSER.lower() == 'firefox':
            # default firefox options
            options = webdriver.FirefoxOptions()
            options.accept_insecure_certs = True
            options.set_capability()

            if(HEADLESS): 
                options.add_argument('--headless')
                options.add_argument('no-sandbox')
                options.add_argument('disable-setuid-sandbox')
            
            self.driver = webdriver.Firefox(options=options, service_log_path=None)
            self.driver.delete_all_cookies()
        elif BROWSER.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            # activate headless option
            if(HEADLESS): 
                options.add_argument('--headless')
                options.add_argument('window-size=1200,600')
                options.add_argument('no-sandbox')
                options.add_argument('disable-setuid-sandbox')

            self.driver = webdriver.Chrome(options=options)
            self.driver.delete_all_cookies()
        else:
            self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def get_driver(self):
        self.driver.timeouts.implicit_wait = float(DEFAULT_TIMEOUT)
        return self.driver

    def load_website(self, url):
        self.driver.get(url)

    def validate_body_component_exists(self, component):
        assert component in self.driver.find_element(By.TAG_NAME, 'body').text, \
            "Component {} not found on page".format(component)

    def terminate_driver(self):
        self.driver.quit()

    def screenshot_as_png(self):
        self.driver.get_screenshot_as_png()

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)


webapp = WebApp.get_instance()
