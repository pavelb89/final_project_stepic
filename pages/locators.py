from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_PASSWORD_RESET_LINK = (By.CSS_SELECTOR, "#login_form a")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REG_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")
