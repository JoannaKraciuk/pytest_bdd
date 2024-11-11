from pytest_bdd import scenario, given, when, then, parsers
from urllib.parse import urljoin

from Mod_00_Log_in.pages.login_page import LoginPage
from Mod_00_Log_in.conftest import url, error_message_1

@scenario("C:/Users/valcr/PycharmProjects/Saucedemo_e2e/src/Mod_00_Log_in/features/multi_invalid_user_log_in.feature",
    "Multi invalid user log in")


def test_failed_login(browser_context):
    pass


@given("I am on the login page")
def get_login_page(login_page: LoginPage, url):
    login_page.open_login_page(url)


@when(parsers.parse('I enter {user_name} in user_name input'))
def input_username(login_page: LoginPage, user_name):
    login_page.input_user_name(user_name)


@then(parsers.parse('I enter {password} in password input'))
def input_password(login_page: LoginPage, password):
    login_page.input_password(password)


@then("I click the login button")
def click_submit(login_page: LoginPage):
    login_page.click_submit_button()


@then("I should see the error message")
def check_page_url(login_page: LoginPage, error_message_1):
    current_message = login_page.error_message
    assert current_message.inner_text() == error_message_1
