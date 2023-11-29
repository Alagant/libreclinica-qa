#!/bin/bash
# Run Behave tests
echo "Running Behave tests from environment ${BEHAVE_STAGE}"
venv/bin/python3 -m behave

# Copy the generated results to the shared volume
##cp -r /app/allure-results/* /allure-results

# Run the post execution python script which uploads the pdf report to Confluence


venv/bin/python3 -m src.utils.commit_to_pdf "$@"
venv/bin/python3 -m upload_report
