from playwright.sync_api import Page

from Mod_00_Log_in.locators.Login_locators import LoginLocators
from conftest import page

import configparser

def get_dict_section(config_file: str, section: str) -> dict:
    config = configparser.ConfigParser()
    config.read(config_file)
    if section not in config:
        raise KeyError(f"Section '{section}' not found in the configuration file.")

    return dict(config[section])

data_path = "data_00_s1_log_in.ini"
url_path = "url.ini"

USER_DATA = get_dict_section(data_path, "login_data")
BASIC_URL = get_dict_section(url_path, "url")

def get_value(dictionary: dict, key: str, default=None):
    return dictionary.get(key, default)


class LoginPage():

    def __init__(self, page: Page):
        self.page = page
        self.user_name = self.page.locator(LoginLocators.USER_NAME_INPUT)
        self.password = self.page.locator(LoginLocators.PASSWORD_INPUT)
        self.submit = self.page.locator(LoginLocators.SUBMIT_BUTTON)

    def open_page(self, url):
        self.page.goto(url)

    def input_user_name(self, login):
        self.user_name.fill(login)

    def input_password(self, password):
        self.password.fill(password)

    def click_submit_button(self):
        self.submit.click()