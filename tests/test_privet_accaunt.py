
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestPrivetAcc:
    def test_privet_acc_click_true(self, driver):
        driver.find_element(*Locators.PRIVET_ACC).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TITLE_LOGIN_PAGE))
        assert driver.find_element(*Locators.TITLE_LOGIN_PAGE).text == 'Вход'
