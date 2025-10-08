import os
import allure
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results, take a screenshot on failure, and attach it to Allure.
    """
    # 1. Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # 2. Check if the test failed during the 'call' stage
    if report.when == "call" and report.failed:
        # Check if the 'page' fixture is available for the failing test
        if "page" in item.fixturenames:
            try:
                # Retrieve the live page fixture from the scope
                page: Page = item.funcargs["page"]
                
                # --- Screenshot Logic ---
                # Create a clean filename
                test_name: str = report.nodeid.replace("::", "_").replace("/", "-")
                filename: str = f"FAIL_{test_name}.png"
                screenshot_dir: str = "allure-screenshots" # A temporary directory for screenshots
                screenshot_path: Path = Path(screenshot_dir) / filename

                # Ensure the screenshot directory exists
                os.makedirs(screenshot_dir, exist_ok=True)
                
                # Take the screenshot!
                page.screenshot(path=screenshot_path)
                print(f"\n[FAILURE] Screenshot saved to: {screenshot_path}")

                # --- Allure Attachment Logic ---
                # 3. Attach the saved screenshot file to the Allure report
                allure.attach.file(
                    str(screenshot_path),
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG,
                )
                
            except Exception as e:
                # Handle cases where page might not be fully initialized or closed
                print(f"\n[ERROR] Could not take or attach screenshot: {e}")


"""
    Fixture to create a browser instance and a session-level scope.
"""
@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       yield browser
       browser.close()

"""
    Fixture to create a new page within the browser instance.
"""
@pytest.fixture(scope="session")
def page(browser):
   page = browser.new_page()
   yield page
   page.close()
   
"""
    Fixture to navigate to the webpage before each test.
"""
@pytest.fixture(scope="session", autouse=True)
def before_each(page: Page):
    print("before the test runs")
    
    # Use the 'page' instance, not the 'Page' class
    page.goto("https://angelicab7.github.io/BOG001-data-lovers/index.html")
    
    # Assert on the 'page' instance with the correct URL and title
    expect(page.get_by_text("Fun Facts")).to_be_visible()

# This hook is provided by pytest-bdd
# It runs immediately after a scenario is executed.
def pytest_bdd_after_scenario(request, feature, scenario):
    """
    Sets the Allure test title dynamically using the Gherkin Scenario name.
    """
    # 1. Check if the scenario title exists and is valid
    if scenario and scenario.name:
        
        # 2. Get the scenario name (which is the title defined in the .feature file)
        scenario_title = scenario.name
        
        # 3. Use allure.dynamic.title() to override the default pytest function name
        #    This applies the title to the current test result item.
        allure.dynamic.title(scenario_title)
        allure.dynamic.description(f"Feature: {feature.name}")
