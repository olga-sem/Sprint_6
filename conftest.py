import pytest
from selenium import webdriver
import helpers
from locators.main_page_locators import MainPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(helpers.URL)
    driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()
    yield driver
    driver.quit()