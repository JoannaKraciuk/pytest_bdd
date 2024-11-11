Feature: Fail Login
  As a user
  I want to see an error message when I enter incorrect login credentials
  So that I know the login attempt was unsuccessful

  Scenario Outline: Multi invalid user log in
    Given I am on the login page
    When I enter <user_name> in user_name input
    Then I enter <password> in password input
    And I click the login button
    Then I should see the error message

    Examples:
    |user_name |password      |
    |user_1    |password 123  |
    |user_2    |password001   |
    |user_3    |wrong_password|


