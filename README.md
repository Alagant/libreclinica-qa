# LibreClinica-QA

## Overview

This project demonstrates the integration of Python, Behave, and Selenium for behavior-driven testing of LibreClinica's web application. The combination of Behave (a BDD framework) and Selenium (a web testing tool) allows to write and automate tests in a more human-readable, behavior-focused manner. [ToDo: Change the overview]

## Dependencies

Below is a table showing the project's dependencies:

| Dependency        | Version   | Description                                     |
|-------------------|-----------|-------------------------------------------------|
| Python            | >=3.8     | Python programming language                     |
| Behave            | >=1.2.6   | Behavior-driven testing framework for Python    |
| Selenium          | >=4.14.0  | Web testing tool for automating browser actions |
| Allure Reports    | >= 2.24.1 | A flexible lightweight multi-language test report tool designed to create fancy and clear testing reports. |


## BEFORE RUNNING
Before running the application:

- Rename the `settings.example.json` file to `settings.json`.
- Configure your environment specific properties.
- Define the `environment` (**dev**, **qa** or **prod** are valid values) that you need to test against it in the 'stage' property inside `behave.ini`. 

## Installation

1. **Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/).

2. **Behave**: Install Behave using pip:

   ```bash
   pip install behave
   ```

3. **Selenium**: Install Selenium using pip:

   ```bash
   pip install selenium
   ```

4. **WebDriver**: Depending on your choice of web browser, download and install the appropriate WebDriver. For example, for Chrome, you'll need [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/). Ensure the WebDriver executable is in your system's PATH.

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

3. Write your feature files in the `features` directory using Behave's Gherkin syntax.

4. Implement your step definitions in the `tests/features/steps` directory using Python.

5. Run your tests using Behave:

   ```bash
   behave
   ```

   Behave will execute the scenarios defined in your feature files and report the results.

## Configuration

- You can configure browser-specific settings, credentials, etc. in the test environment in the `settings.json` file.

## Contributing

Contributions to this project are welcome. Please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and ensure tests pass.

4. Create a pull request to the main repository.

## License

#TBD

---