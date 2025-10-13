Feature: Visual Stability of Character Search and Filter

  Scenario: Home Page Components
    Given I am on the Rick and Morty web Page
    Then The banner and fun facts section should be visually stable

  Scenario: Visual Check after applying a filter
    Given I am on the Characters Page
    Then The search button and filters should be visually stable
    When I select "Animal" from the species dropdown
    Then the character card list should be visually stable with the filter applied