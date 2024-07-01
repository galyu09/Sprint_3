
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


class TestConstructor:


    # Подскролл к разделу «Соусы»
    def test_sauce_scroll_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        expected = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.SAUCES)).get_attribute('class')
        assert 'tab_tab_type_current' in expected

    # Подскролл к разделу «Булки»
    def test_bread_scroll_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUCES)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BREAD)).click()
        expected = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BREAD)).get_attribute('class')
        assert 'tab_tab_type_current' in expected

    # Подскролл к разделу «Начинки»
    def test_fillings_scroll_true(self, driver):

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLINGS)).click()
        expected = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.FILLINGS)).get_attribute('class')
        assert 'tab_tab_type_current' in expected



