from urllib.parse import urljoin

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from pytest_bdd.parsers import parse

import conftest
from Mod_00_Log_in.pages.login_page import LoginPage
from Utils.stepdata_00_s_login import config_data
from conftest import browser_context

BASIC_URL = conftest.BASIC_URL
DASHBOARD_URL = "/inventory.html"
PAGE_URL = urljoin(BASIC_URL, DASHBOARD_URL)

scenario("log_in.feature")

@given ("I am on the login page")
def get_login_page(login_page: LoginPage, config_data, page):
    login_page.open_page(config_data['url'])
    return page

@when (parsers.pars('I enter "<user_name>"'))
def input_username(login_page: LoginPage, config_data):
    login_page.input_user_name(config_data['username'])





