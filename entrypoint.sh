#!/bin/bash
# Run Behave tests
behave

pwd

# Copy the generated results to the shared volume
cp -r /app/allure-results/* /allure-results

# Run the post execution python script which uploades the pdf report to Confluence
echo "listing /app"
ls /app
python3 /app/upload_report.py
python3 /app/commit_to_pdf.py

# sleep 2m
#sleep 5m

