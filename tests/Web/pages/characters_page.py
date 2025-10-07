from playwright.sync_api import Page, expect 

class CharactersPage:
    def __init__(self, page: Page):
        self.page = page
        self.characters_button = page.get_by_text("Characters")
        self.character_container = page.locator("#characters-container > .column")
        self.search_field = page.locator("#searchIn")
        self.search_button = page.locator("#searchButton")
        self.character_card = page.get_by_text("Pickle Rick")
        self.order_dropdown = page.locator("#filter-input-order")
        self.species_dropdown = page.locator("#filter-input-species")
        self.characters_sorted = page.get_by_text("Abadango Cluster Princess")
        self.category_displayed = page.locator(".card-container > .card-back font-color > .card-description div:has-text('Species: Animal')")

    def verify_characters_page(self): 
        expect(self.characters_button).to_be_visible()
        expect(self.character_container).not_to_have_count(0) 

    def click_order_dropdown(self):
        self.order_dropdown.select_option("Order A-Z")

    def verify_characters_sorted(self):
        expect(self.character_container).not_to_have_count(0)
        expect(self.characters_sorted).to_be_visible()
    
    def click_species_dropdown(self):
        self.species_dropdown.select_option("Animal")

    def verify_species_displayed(self):
        expect(self.character_container).not_to_have_count(0)
        expect(self.category_displayed).to_be_visible()

    def search_for_character(self):
        self.search_field.fill("pickle")
        self.search_button.wait_for()
        self.search_button.click()

    def verify_character_displayed(self):
        self.character_card.wait_for()
        expect(self.character_card).to_be_visible()