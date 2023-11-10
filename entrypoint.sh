#!/bin/bash
# Run Behave tests
behave

pwd

# Copy the generated results to the shared volume
cp -r /app/allure-results/* /allure-results

# Run the post execution python script which uploades the pdf report to Confluence
python3 /app/upload_report.py

# sleep 2m
#sleep 5m

