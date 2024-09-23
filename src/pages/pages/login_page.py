from playwright.sync_api import Page
from src.pages.locators.login_page_locators import LoginPageLocators


class LoginPage():

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.user_name_input = self.page.locator(LoginPageLocators.USER_NAME_INPUT)
        self.password_input = self.page.locator(LoginPageLocators.PASSWORD_INPUT)
        self.login_button = self.page.locator(LoginPageLocators.LOGIN_BUTTON)

    def login(self, user_name, password):
        self.user_name_input.fill(user_name)
        self.password_input.fill(password)
        self.login_button.click()