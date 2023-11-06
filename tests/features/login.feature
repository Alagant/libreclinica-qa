Feature: User Login
    As a data manager user I want to login on the website 
    So that I can access LibreClinica platform 
    
    Background:
        Given Launch the browser
        When I open the LibreClinica application
        Then The login page is shown
    
    Scenario: Login with valid credentials
        And Provide root user credentials
        And Click on the Login button
        Then Login is successful and dashboard is shown along with a Welcome message
    
