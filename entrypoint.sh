#!/bin/bash
# Run Behave tests
echo "Running Behave tests"
behave

pwd

# Copy the generated results to the shared volume
##cp -r /app/allure-results/* /allure-results

# Run the post execution python script which uploades the pdf report to Confluence

echo "pwding"
pwd
#. venv/bin/activate
venv/bin/python3 -m src.utils.commit_to_pdf "$@"
venv/bin/python3 -m upload_report

# sleep 2m
# sleep 5m

