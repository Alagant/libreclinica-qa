import json
import os
from src.utils.utils import Utils
from behave.configuration import Configuration

config = Configuration()

with open('settings.json', 'r') as config_file:
    config_data = json.load(config_file)

# Get the chosen environment
environment = config.stage or config_data.get("env", "dev")

# Set environment-specific values
if environment in config_data["environments"]:
    settings = config_data["environments"][environment]
    
    
    _utils = Utils()
    _utils.generate_env_props(settings,'./allure-results/','environment.properties', environment)

    # Set the constants from settings.json based on chosen env
    BASE_URL = settings.get("base_url")
    BROWSER = settings.get("browser")
    DEFAULT_TIMEOUT = settings.get("defaultTimeout")
    HEADLESS = settings.get("headless")
    ROOT_USERNAME = os.environ.get('LC_ROOT_USERNAME')
    ROOT_PASSWORD = os.environ.get('LC_ROOT_PASSWORD')
    DRIVER_PATH = settings.get("driver_default_path")
    CONFLUENCE_USERNAME =  os.environ.get('CONFLUENCE_USERNAME')
    CONFLUENCE_PAGEID = settings["confluence_config"].get("parentPageId")
    CONFLUENCE_URL = settings["confluence_config"].get("url")
    CONFLUENCE_SPACE_ID = os.environ.get('CONFLUENCE_SPACE_ID')
    CONFLUENCE_ACCESS_TOKEN = os.environ.get('CONFLUENCE_ACCESS_TOKEN')

    print(f'Running Browser {str(BROWSER).upper()} | Host: {str(BASE_URL)} | environment: {str(environment).upper()}')
    

else:
    raise ValueError(f"Environment '{environment}' is not a valid property.")