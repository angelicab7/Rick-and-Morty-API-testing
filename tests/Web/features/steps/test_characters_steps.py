from pytest_bdd import given, when, then, scenario
from playwright.sync_api import Page
from tests.Web.pages.home_page import HomePage
from tests.Web.pages.characters_page import CharactersPage

@scenario('../search_character.feature', 'Verify Characters List is displayed')
def test_search_character():
    pass

@given('I am on the Rick and Morty web Page') 
def verify_home(page: Page):
    home_page = HomePage() 
    home_page.verify_home_page(page)

@when('I click on Characters Button') 
def click_characters(page: Page):
    home_page = HomePage() 
    home_page.proceed_to_characters_page(page)

@then('I should see the list of Characters displayed') 
def characters_displayed(page: Page):
    characters_page = CharactersPage() 
    characters_page.verify_characters_page(page)
   