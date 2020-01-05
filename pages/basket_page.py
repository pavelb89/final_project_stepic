from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "The basket is not empty"

    def should_be_empty_basket_message(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert 'en' in language.lower(), 'This test should run with option language == "en"'
        message = self.browser.find_element(*BasketPageLocators.SIGN_OF_EMPTY_BASKET).text
        assert 'Your basket is empty' in message, f'{message} is different from "Your basket is empty"'
