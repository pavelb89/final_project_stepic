from .base_page import BasePage
from .locators import LoginPageLocators
import re


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert re.search('login', self.browser.current_url) is not None

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_USERNAME), \
            "Username input box is not present in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), \
            "Password input box is not present in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_RESET_LINK), \
            "Password reset link is not presented in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), \
            "Login submit button is not presented in login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_EMAIL), \
            "E-mail input box is not present in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_PASSWORD), \
            "Password-repeat input box is not present in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_REPEAT_PASSWORD), \
            "Password input box is not presented in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_SUBMIT), \
            "Registration submit button is not presented in registration form"
