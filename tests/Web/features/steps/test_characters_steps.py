from pytest_bdd import given, when, then, scenario
from playwright.sync_api import Page
from tests.Web.pages.home_page import HomePage
from tests.Web.pages.characters_page import CharactersPage

@scenario('../search_character.feature', 'Verify Characters List is displayed')
def test_verify_characters():
    pass

@given('I am on the Rick and Morty web Page') 
def verify_home(page: Page):
    home_page = HomePage(page) 
    home_page.verify_home_page()

@when('I click on Characters Button') 
def click_characters(page: Page):
    home_page = HomePage(page) 
    home_page.proceed_to_characters_page()

@then('I should see the list of Characters displayed') 
def characters_displayed(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.verify_characters_page()

@scenario('../search_character.feature', 'Search and filter Character')
def test_search_character():
    pass

@given('I am on Characters Page') 
def verify_characters(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.verify_characters_page()

@when('I click in order dropdown and select A - Z option') 
def click_order_dropdown(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.click_order_dropdown()

@then('I should see the characters displayed in the order chosen') 
def characters_sorted(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.verify_characters_sorted()

@when('I click in species dropdown and select Animals option') 
def click_species_dropdown(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.click_order_dropdown()

@then('I Should see only Animal characters displayed') 
def humans_displayed(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.verify_characters_sorted()
    
@when('I click on search button and type "pickle"') 
def click_search_button(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.search_for_character()

@then('I should see Character displayed') 
def character_displayed(page: Page):
    characters_page = CharactersPage(page) 
    characters_page.verify_character_displayed()