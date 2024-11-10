import pytest
from playwright.sync_api import sync_playwright
from Utils.stepdata_00_s_login import config_data
from Mod_00_Log_in.pages.login_page import LoginPage

BASIC_URL: str = None

@pytest.fixture(scope="session")
def browser_config():
    return config_data['browser']

@pytest.fixture(scope="session")
def browser_context(browser_config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=browser_config['headless'], slow_mo=1000)
        context = browser.new_context(viewport=browser_config['viewport'])
        yield context
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture()
def url():
    url = config_data['url']
    return url

def dashboard_url():
    site_url = config_data['dashboard_url']
    return site_url

@pytest.fixture()
def valid_username():
    return config_data['username']

@pytest.fixture()
def valid_password():
    return config_data['password']

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def error_message():
    return config_data['error_message']