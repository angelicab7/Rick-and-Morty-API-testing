import allure
from pytest_bdd import given, when, then, scenario
from playwright.sync_api import Page
from tests.Web.pages.home_page import HomePage 
from tests.Web.pages.characters_page import CharactersPage
from tests.Web.visual_utils import VisualRegression

@scenario('../features/visual_search.feature', 'Home Page Components')
def test_verify_characters():
    pass

@given('I am on the Rick and Morty web Page') 
def verify_home(page: Page):
    with allure.step('I am on the Rick and Morty web Page'):
        home_page = HomePage(page) 
        home_page.verify_home_page()

@then('The banner and fun facts section should be visually stable') 
def check_banner_visuals(visual_regression: VisualRegression):
    with allure.step('The banner and fun facts section should be visually stable'):
        visual_regression.check_full_page(screenshot_name='homepage_initial_header')
