import re
from playwright.sync_api import Page, expect

class CharactersPage:

    def verify_characters_page(self,page: Page): 
        expect(page.get_by_text("Characters")).to_be_visible()