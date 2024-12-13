import pytest
from selenium import webdriver
import urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(urls.URL)
    yield driver
    driver.quit()