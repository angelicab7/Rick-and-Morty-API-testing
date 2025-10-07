import re
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.fun_facts_text = page.get_by_text("Fun Facts")
        self.characters_button = page.get_by_role("button",name="Characters")


    def verify_home_page(self):
        expect(self.fun_facts_text).to_be_visible()
        
    def proceed_to_characters_page(self):
        self.characters_button.click()