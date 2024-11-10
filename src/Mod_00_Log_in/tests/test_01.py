from pytest_bdd import scenario, given, when, then, parsers
from urllib.parse import urljoin

from Mod_00_Log_in.pages.login_page import LoginPage
from Mod_00_Log_in.conftest import valid_username, valid_password, url


DASHBOARD_URL = "inventory.html"
# PAGE_URL = urljoin(url(), DASHBOARD_URL)


# Dekorator nie powinien być nad krokiem, ale nad funkcją testową
@scenario(
    "C:/Users/valcr/PycharmProjects/Saucedemo_e2e/src/Mod_00_Log_in/features/log_in.feature",
    "Successful login")


def test_successful_login(browser_context):
    pass


@given("I am on the login page")
def get_login_page(login_page: LoginPage, url):
    login_page.open_login_page(url)


@when(parsers.parse('I enter {user_name}'))
def input_username(login_page: LoginPage, valid_username):
    login_page.input_user_name(valid_username)


@then(parsers.parse('I enter {password}'))
def input_password(login_page: LoginPage, valid_password):
    login_page.input_password(valid_password)


@then("I click the login button")
def click_submit(login_page: LoginPage):
    login_page.click_submit_button()


@then("I should see the dashboard")
def check_page_url(login_page: LoginPage, url):
    page_url = urljoin(url, DASHBOARD_URL)
    assert login_page.check_new_url(page_url), f"Expected URL: {page_url}, but got: {login_page.page.url}"
