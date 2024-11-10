Feature: Fail Login
  As a user
  I want to see an error message when I enter incorrect login credentials
  So that I know the login attempt was unsuccessful

  Scenario: Fail login
    Given I am on the login page
    When I enter "locked_out_user" in user_name input
    Then I enter "secret_sauce" in password input
    And I click the login button
    Then I should see the error message
