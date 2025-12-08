Feature: Login
  In order to manage the employee records
  As a user
  I want to get access to dashboard


  Scenario: ValidLogin
    Given user opens browser with OrangeHRM application
    When user enter the username as "Admin"
    And user enter the password as "admin123"
    And user clicks on login
    Then user should get access to dashboard with header as "Quick Launch"

