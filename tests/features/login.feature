Feature: User Login
    Feature: User Login
    As a data manager user, I want to be able to securely log in to the LibreClinica platform.
    
    Background:
        Given Launch the browser
        When I open the LibreClinica application
        Then The login page is shown
    
    Scenario: Login with valid credentials
        And Provide root user credentials
        And Click on the Login button
        Then Login is successful and dashboard is shown along with a Welcome message
        Then Generate a PDF report
        Then Upload the PDF report to Confluence
        Then Close the browser 
    
