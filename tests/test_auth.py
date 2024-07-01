from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page_true(self, driver: object) -> object:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        button_checkout = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
        assert button_checkout.is_displayed()

    # вход через кнопку «Личный кабинет»
    def test_login_from_privet_acc_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        checkout_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
        assert checkout_button.is_displayed()

    # вход через кнопку в форме регистрации
    def test_login_from_registration_form_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LINK_ENTER_REG)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REG_ENTER))
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LINK_ENTER_REG)).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        checkout_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
        assert checkout_button.is_displayed()

    # вход через кнопку в форме восстановления пароля.
    def test_login_from_revert_form_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        # WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SET_PASSWORD_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_REG_ENTER))
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SET_PASSWORD_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LINK_ENTER_SET_PAS)).click()
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        checkout_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
        assert checkout_button.is_displayed()


