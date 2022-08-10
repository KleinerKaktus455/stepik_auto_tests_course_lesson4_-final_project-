from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty!"

    def should_be_message_about_emptiness(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTINESS), \
            "Message about basket emptyness is not present!"
