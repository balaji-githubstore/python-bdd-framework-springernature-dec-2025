@login @regression
Feature: Login
  In order to manage the employee records
  As a user
  I want to get access to dashboard

  Background:
    Given user opens browser with OrangeHRM application

  @smoke  @positive  @valid
  Scenario: ValidLogin
    When user enter the username as "Admin"
    And user enter the password as "admin123"
    And user clicks on login
    Then user should get access to dashboard with header as "Quick Launch77"


  @negative
  Scenario Outline: InvalidLogin
    When user enter the username as "<username>"
    And user enter the password as "<password>"
    And user clicks on login
    Then user should not get access with error as "<expected_error>"
    Examples:
      | username | password | expected_error      |
      | saul     | saul123  | Invalid credentials |
      | john     | john123  | Invalid credentials |

