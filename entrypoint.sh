#!/bin/bash
# Run Behave tests
echo "Running Behave tests"
behave

pwd

# Copy the generated results to the shared volume
cp -r /app/allure-results/* /allure-results

# Run the post execution python script which uploades the pdf report to Confluence
echo "listing /app"
ls /app
pwd
cd /app
echo "pwding"
pwd
python -m src.utils.commit_to_pdf $(Build.SourceVersion) $(Build.BuildId) $(Build.BuildNumber) $(Build.SourceVersionMessage)
python -m upload_report

# sleep 2m
# sleep 5m

