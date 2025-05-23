import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage

from utils import attach


DEFAULT_BROWSER_VERSION = "128.0" # или "latest"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', help="Choose browser version for testing",
        default='120.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser.config.base_url = 'https://nordclan.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


    options = Options()
    options.add_argument('--headless')

    '''
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')
    selenoid_url = os.getenv('SELENOID_URL')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub",
        options=options
    )
    '''
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if driver == webdriver.Remote:
        attach.add_video(browser, selenoid_url)
    # attach.add_video(browser, selenoid_url) # раскомментировать при запуске на selenoid

    driver.quit()


@pytest.fixture
def main_page():
    return MainPage()

@pytest.fixture
def vacancies_page():
    return VacanciesPage()