Feature: User Login
    As a data manager user I want to login on the website 
    So that I can access LibreClinica platform 
    
    @smoke-test
    Scenario:  Login with valid credentials
        Given Launch the browser
        When I open the LibreClinica application
        Then The login page is shown
    #    Then Take screenshot
    
    #Scenario: Login with valid credentials
    #    Given Launch the browser
    #    When Open the "https://www.google.com" website
    #    Then The main page is opened and shows the title "Google"

    
    #@valid_login
    #Scenario: Login with valid credentials
    #    And Provide the username "root" and password "123456"
    #    And Click on the Signin button
    #    Then Login is successful and dashboard is shown
    #    Then Close the browser
    
