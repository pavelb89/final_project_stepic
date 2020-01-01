from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_product_information()
        product_info = self.get_product_info()
        self.should_be_basket_button()
        # self.should_not_be_success_message()
        self.go_to_the_basket()
        self.solve_quiz_and_get_code()
        self.check_content_of_basket(*product_info)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message should disappear, but it didn't happen!"

    def check_content_of_basket(self, product_name, product_price):
        # find all messages
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"

        # check product name
        # CSS-selector: #messages div:first-child div.alertinner
        names_equal = False
        for item_strong in msg_lst:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"

        # check total cost of basket
        item_basket_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL)
        assert item_basket_cost.text == product_price, \
            "Prices in basket and in product page isn't equal"

    def get_product_info(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        return product_name, product_price

    def go_to_the_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Button to add product in the basket is not present"

    def should_be_product_information(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT), \
            "Name of product is not present"
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT), \
            "Price of product is not present"
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_OF_PRODUCT), \
            "Description of product is not present"
