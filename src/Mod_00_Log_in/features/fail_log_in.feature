Feature: Fail Login
  As a user
  I want to see an error message when I enter incorrect login credentials
  So that I know the login attempt was unsuccessful

  Scenario Outline: Fail login
    Given I am on the login page
    When I enter <user_name>
    Then I enter <password>
    And I click the login button
    Then I should see the error message

    Examples:
      | user_name       | password    |
      | locked_out_user | secret_sauce|
