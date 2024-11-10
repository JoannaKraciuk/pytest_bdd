from playwright.sync_api import Page
from Mod_00_Log_in.locators.Login_locators import LoginLocators

class LoginPage():

    def __init__(self, page: Page):
        self.page = page
        self.user_name = self.page.locator(LoginLocators.USER_NAME_INPUT)
        self.password = self.page.locator(LoginLocators.PASSWORD_INPUT)
        self.submit = self.page.locator(LoginLocators.SUBMIT_BUTTON)
        self.error_message = self.page.locator(LoginLocators.ERROR_MESSAGE)

    def open_login_page(self, url):
        self.page.goto(url)

    def input_user_name(self, login):
        self.user_name.fill(login)
        self.user_name.blur()

    def input_password(self, password):
        self.password.fill(password)

    def click_submit_button(self):
        self.submit.click()

    def check_new_url(self, expected_url: str):
        current_url = self.page.url
        return current_url == expected_url

    def get_error_message(self):
        error_message = self.error_message.is_visible()
        return error_message
