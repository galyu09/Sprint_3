import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants


@pytest.fixture
def driver():
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.maximize_window()
    browser = webdriver.Firefox()
    browser.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_main(driver):
    driver.get(Constants.URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture(name='login_private_acc')
def login_private_acc(driver):
    driver.get(Constants.URL)
    driver.find_element(*Locators.PRIVET_ACC).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.EMAIL))
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    return driver