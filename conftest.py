import pytest
from playwright.sync_api import Page, sync_playwright
from Utils.stepdata_00_s_login import config_data


from Mod_00_Log_in.pages.login_page import LoginPage

BASIC_URL: str = None

def pytest_configure(config):
    global BASIC_URL

@pytest.fixture(scope="session")
def browser_config():
    return config_data['browser']

@pytest.fixture(scope="session")
def browser_context(browser_config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=browser_config['headless'])
        context = browser.new_context(viewport=browser_config['viewport'])
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def url():
    return config_data['url']

@pytest.fixture(scope="session")
def valid_user():
    return config_data['valid_user']


@pytest.fixture
def login_page(page):
    return LoginPage(page)