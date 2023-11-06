#!/bin/bash

# Run Behave tests
behave

# Copy the generated results to the shared volume
cp -r ./allure-results/* /allure-results

chmod +x ./executables/allure-pdf-1.6.0/bin/allure-pdf

timestamp=`date +%Y%m%d%H%M%S`
export $report_filename=`'report_'${timestamp}'.pdf'`
export allurepdf='./executables/allure-pdf-1.6.0/bin/allure-pdf'

$allurepdf /app/allure-results -o /allure-results/$report_filename