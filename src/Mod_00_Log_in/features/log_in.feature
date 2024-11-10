Feature: Log in
  As a user
  I want to log in to the system
  So that I can access my account

  Scenario: Successful login
    Given I am on the login page
    When I enter <user_name>
    Then I enter <password>
    Then I click the login button
    Then I should see the dashboard


