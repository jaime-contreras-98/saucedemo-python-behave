Feature: Multiple Scenarios on SauceDemo

  Background: Common steps
    Given I launch Chrome browser
    When I open SauceDemo Homepage
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login button

  Scenario: Login to SauceDemo using valid credentials
    Then User must successfully login to Basepage

  Scenario: Logout from SauceDemo
    When I click the logout button
    Then I must be on the homepage

  Scenario: Add a product to cart
    When I add to cart a product
    Then Product must appear on my cart
