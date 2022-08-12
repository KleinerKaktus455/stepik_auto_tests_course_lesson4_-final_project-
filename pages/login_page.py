from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Current url is false. No 'login' in  url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is missing"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT)
        confirm_registration_button = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        confirm_registration_button.click()
