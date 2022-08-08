from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ADDING_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")
    SUCCESS_ADDING_MESSAGE_TOTAL_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_ADDING_MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')

