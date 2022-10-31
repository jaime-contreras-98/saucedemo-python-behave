Feature: SauceDemo Login Scenario
  Scenario: Login to SauceDemo using valid credentials
    Given I launch Chrome browser
    When I open SauceDemo Homepage
    And Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then User must successfully login to Basepage

  Scenario Outline: Login to SauceDemo using valid credentials
    Given I launch Chrome browser
    When I open SauceDemo homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to Basepage

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | locked_out_user         | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |