@employee   @regression
Feature: Employee
  In order to manage the employee records
  As a user
  I want to add, edit and delete employee records

  @positive @validemployee
  Scenario Outline: AddValidEmployee
    Given user opens browser with OrangeHRM application
    When user enter the username as "<username>"
    And user enter the password as "<password>"
    And user clicks on login
    And user clicks on PIM menu
    And user clicks on Add Employee
    And user fill the employee details form
      | firstName    | middleName    | lastName    | employeeId    |
      | <first_name> | <middle_name> | <last_name> | <employee_id> |
    And user clicks on save employee
    Then user should get the profile name as "<first_name> <last_name>"
    And user should get the firstname field as "<first_name>"
    Examples:
      | username | password | first_name | middle_name | last_name | employee_id |
      | Admin    | admin123 | saul       | w           | goodman   | 4554        |
      | Admin    | admin123 | john       | w           | wick      | 4555        |

