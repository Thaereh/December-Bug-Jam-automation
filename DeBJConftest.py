# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BASE_URL, DEFAULT_IMPLICIT_WAIT


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the RecommenDead app."""
    return BASE_URL


@pytest.fixture(scope="session")
def driver():
    """Session-scoped WebDriver (Chrome)."""
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # uncomment for headless mode

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(DEFAULT_IMPLICIT_WAIT)

    yield driver

    driver.quit()
