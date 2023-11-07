#!/bin/bash

# Run Behave tests
behave

# Copy the generated results to the shared volume
cp -r /app/allure-results/* /allure-results