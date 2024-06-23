from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin:
    def test_login_from_main_page_true(self, login_main):
        driver = login_main
        title_main_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*Locators.TITLE_MAIN_PAGE)).text
        assert title_main_page == 'Соберите бургер'

    def test_login_from_privet_acc_true(self, login_private_acc, driver):
        driver = login_private_acc(driver)
        title_main_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*Locators.TITLE_MAIN_PAGE)).text
        assert title_main_page == 'Соберите бургер'



