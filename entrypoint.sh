#!/bin/bash

# Run Behave tests
behave

pwd

# Run the post execution python script which uploades the pdf report to Confluence
python3 /app/upload_report.py

# Copy the generated results to the shared volume
cp -r /app/allure-results/* /allure-results

# sleep 2m
sleep 5m
