import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Constants.URL)
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.LOADER_MODAL))
    yield driver
    driver.quit()



