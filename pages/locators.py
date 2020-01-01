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


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main>h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    DESCRIPTION_OF_PRODUCT = (By.CSS_SELECTOR, "#product_description")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    MSG_PRODUCT_ADD_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
