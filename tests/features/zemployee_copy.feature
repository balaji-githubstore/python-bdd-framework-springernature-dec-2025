#@employee   @regression
#Feature: Employee
#  In order to manage the employee records
#  As a user
#  I want to add, edit and delete employee records
#
#  @positive @validemployee
#  Scenario: AddValidEmployee
#    Given user opens browser with OrangeHRM application
#    When user enter the username as "Admin"
#    And user enter the password as "admin123"
#    And user clicks on login
#    And user clicks on PIM menu
#    And user clicks on Add Employee
#    And user fill the employee details form
#      | firstName | middleName | lastName | employeeId |
#      | john      | w          | wick     | 2004       |
#    And user clicks on save employee
#    Then user should get the profile name as "john wick"
#    And user should get the firstname field as "john"
#
#    @validemployee
#  Scenario: AddValidEmployee2
#    Given user opens browser with OrangeHRM application
#    When user enter the username as "Admin"
#    And user enter the password as "admin123"
#    And user clicks on login
#    And user clicks on PIM menu
#    And user clicks on Add Employee
#    And user fill the employee details form
#      | firstName | middleName | lastName | employeeId |
#      | saul      | w          | goodman  | 2005       |
#    And user clicks on save employee
#    Then user should get the profile name as "saul goodman"
#    And user should get the firstname field as "saul"
