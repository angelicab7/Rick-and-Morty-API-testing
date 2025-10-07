Feature: Filter Rick and Morty characters

Scenario: Verify Characters List is displayed
   Given I am on the Rick and Morty web Page
    When I click on Characters Button
    Then I should see the list of Characters displayed

Scenario: Search and filter Character
   Given I am on Characters Page
    When I click in order dropdown and select A - Z option
    Then I should see the characters displayed in the order chosen
    When I click in species dropdown and select Animals option
    Then I Should see only Animal characters displayed
    When I click on search button and type "pickle"
    Then I should see Character displayed