import allure
from pytest_bdd import given, when, then, scenario
from playwright.sync_api import Page
from tests.Web.pages.home_page import HomePage
from tests.Web.pages.characters_page import CharactersPage

@scenario('../search_character.feature', 'Verify Characters List is displayed')
def test_verify_characters():
    pass

@given('I am on the Rick and Morty web Page') 
def verify_home(page: Page):
    with allure.step('I am on the Rick and Morty web Page'):
        home_page = HomePage(page) 
        home_page.verify_home_page()

@when('I click on Characters Button') 
def click_characters(page: Page):
    with allure.step('I click on Characters Button'):
        home_page = HomePage(page) 
        home_page.proceed_to_characters_page()

@then('I should see the list of Characters displayed') 
def characters_displayed(page: Page):
    with allure.step('I should see the list of Characters displayed'):
        characters_page = CharactersPage(page) 
        characters_page.verify_characters_page()

@scenario('../search_character.feature', 'Search and filter Character')
def test_search_character():
    pass

@given('I am on Characters Page') 
def verify_characters(page: Page):
    with allure.step('I am on Characters Page'):
        characters_page = CharactersPage(page) 
        characters_page.verify_characters_page()

@when('I click in order dropdown and select A - Z option') 
def click_order_dropdown(page: Page):
    with allure.step('I click in order dropdown and select A - Z option'):
        characters_page = CharactersPage(page) 
        characters_page.click_order_dropdown()

@then('I should see the characters displayed in the order chosen') 
def characters_sorted(page: Page):
    with allure.step('I should see the characters displayed in the order chosen'):
        characters_page = CharactersPage(page) 
        characters_page.verify_characters_sorted()

@when('I click in species dropdown and select Animals option') 
def click_species_dropdown(page: Page):
    with allure.step('I click in species dropdown and select Animals option'):
        characters_page = CharactersPage(page) 
        characters_page.click_order_dropdown()

@then('I Should see only Animal characters displayed') 
def humans_displayed(page: Page):
    with allure.step('I Should see only Animal characters displayed'):
        characters_page = CharactersPage(page) 
        characters_page.verify_characters_sorted()

@when('I click on search button and type "pickle"')
def click_search_button(page: Page):
    with allure.step('I click on search button and type "pickle"'):
        characters_page = CharactersPage(page) 
        characters_page.search_for_character()

@then('I should see Character displayed') 
def character_displayed(page: Page):
    with allure.step('I should see Character displayed'):
        characters_page = CharactersPage(page) 
        characters_page.verify_character_displayed()