# LibreClinica-QA

## Overview

This project demonstrates the integration of Python, Behave, and Selenium for behavior-driven testing of LibreClinica's web application. The combination of Behave (a BDD framework) and Selenium (a web testing tool) allows you to write and automate tests in a more human-readable, behavior-focused manner.

## Dependencies

Below is a table showing the project's dependencies:

| Dependency        | Version   | Description                                     |
|-------------------|-----------|-------------------------------------------------|
| Python            | >=3.8     | Python programming language                     |
| Behave            | >=1.2.6   | Behavior-driven testing framework for Python    |
| Selenium          | >=4.14.0  | Web testing tool for automating browser actions |
| Allure Reports Server    | >= 2.24.1 | A flexible lightweight multi-language test report tool designed to create fancy and clear testing reports. |

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

4. Implement your step definitions in the `features/steps` directory using Python.

5. Run your tests using Behave:

   ```bash
   behave
   ```

   Behave will execute the scenarios defined in your feature files and report the results.

## Configuration

- You can configure browser-specific settings and URLs in the test environment in the `environment.py` file.

## Contributing

Contributions to this project are welcome. Please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and ensure tests pass.

4. Create a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

This README provides an overview of the project, its dependencies, installation instructions, and usage guidelines. You can customize it to suit your project's specific needs.