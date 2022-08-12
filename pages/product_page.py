from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException  # потом удали
import math
import time


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "'Add to the basket button' is missing!"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_success_messages(self):
        self.should_be_success_messages()
        self.should_be_book_name_in_message()
        self.should_be_book_price_in_message()

    def should_be_success_messages(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_ADDING_MESSAGE), \
            "Success messages are missing!"

    def should_be_book_name_in_message(self):
        book_name_object = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name_object.text

        message_text_object = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDING_MESSAGE_BOOK_NAME)
        message_text = message_text_object.text

        assert book_name == message_text, \
            "Book name is not in success adding in basket message!"

    def should_be_book_price_in_message(self):
        book_price_object = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price_object.text

        message_price_object = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDING_MESSAGE_TOTAL_SUM)
        message_price = message_price_object.text

        assert book_price == message_price,\
            "Total basket sum should be equal to the book price!"

    def solve_quiz_and_get_code(self):  # потом удали
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
