import json
import os
from src.utils.utils import Utils
from behave.configuration import Configuration

config = Configuration(stage=os.environ.get('BEHAVE_STAGE', 'dev'))
print(f"Config stage is {config.stage}, config is {config}, with defaults {config.defaults}")
print(f"We are in the branch {os.environ.get('branch')}")

with open('settings.json', 'r') as config_file:
    config_data = json.load(config_file)

# Get the chosen environment
environment = config.stage or config_data.get("env", "dev")

# Set environment-specific values
if environment in config_data["environments"]:
    settings = config_data["environments"][environment]
    
    
    _utils = Utils()
    _utils.generate_env_props(settings,'./allure-results/','environment.properties', environment)
    credentials = _utils.get_credentials(settings)

    # Set the constants from settings.json based on chosen env
    BASE_URL = settings.get("base_url")
    BROWSER = settings.get("browser")
    DEFAULT_TIMEOUT = settings.get("defaultTimeout")
    HEADLESS = settings.get("headless")
    ROOT_USERNAME = os.environ.get('LC_ROOT_USERNAME', credentials.get("root_username"))
    ROOT_PASSWORD = os.environ.get('LC_ROOT_PASSWORD', credentials.get("root_password"))
    DRIVER_PATH = settings.get("driver_default_path")
    CONFLUENCE_USERNAME = os.environ.get('CONFLUENCE_USERNAME')
    print(f"CONFLUENCE_USERNAME {CONFLUENCE_USERNAME}, {ROOT_USERNAME}, {ROOT_PASSWORD}")
    CONFLUENCE_PAGE_ID = settings["confluence_config"].get("parentPageId")
    CONFLUENCE_URL = settings["confluence_config"].get("url")
    CONFLUENCE_SPACE_ID = os.environ.get('CONFLUENCE_SPACE_ID')
    CONFLUENCE_ACCESS_TOKEN = os.environ.get('CONFLUENCE_ACCESS_TOKEN')
    print(f"cosaid {CONFLUENCE_SPACE_ID}, {CONFLUENCE_ACCESS_TOKEN}, {CONFLUENCE_URL}, {CONFLUENCE_PAGE_ID}")

    print(f'Running Browser {str(BROWSER).upper()} | Host: {str(BASE_URL)} | environment: {str(environment).upper()}')
    

else:
    raise ValueError(f"Environment '{environment}' is not a valid property.")