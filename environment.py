import json
from behave.configuration import Configuration

config = Configuration()

with open('settings.json', 'r') as config_file:
    config_data = json.load(config_file)

# Get the chosen environment
environment = config_data.get("env", "dev")

# Set environment-specific values
if environment in config_data["environments"]:
    settings = config_data["environments"][environment]
    BASE_URL = settings.get("base_url")
    BROWSER = settings.get("browser")
    DEFAULT_TIMEOUT = settings.get("defaultTimeout")

    print(f'Running Browser {BROWSER} at Host: {BASE_URL}')

else:
    raise ValueError(f"Environment '{environment}' is not a valid property.")