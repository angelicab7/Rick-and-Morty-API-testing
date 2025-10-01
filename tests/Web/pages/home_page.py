import re
from playwright.sync_api import Page, expect

class HomePage:
    def verify_home_page(self,page: Page):
        expect(page.get_by_text("Fun Facts")).to_be_visible()
        
    def proceed_to_characters_page(self,page: Page):
        page.get_by_role("button",name="Characters").click()