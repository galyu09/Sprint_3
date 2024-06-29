from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators


class TestPrivetAcc:

    # переход по клику на «Личный кабинет» НЕавторизованным пользователем
    def test_private_acc_click_enter_unreg_true(self, driver):

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        title_main_page = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.TITLE_LOGIN_PAGE)).text
        assert title_main_page == 'Вход'

    # переход по клику на «Личный кабинет» авторизованным пользователем
    def test_private_acc_click_enter_reg_true(self, driver):

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        # ждем пока пропадет лоадер
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.LOADER_MODAL))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        # current_url = driver.current_url
        # assert current_url == f"{Constants.URL}account/profile"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_FORM))
        name = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.NAME_FIELD)).get_attribute('value')
        email = WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.EMAIL_FIELD)).get_attribute('value')
        assert name == Constants.NAME
        assert email == Constants.EMAIL

    # Выход из личного кабинета
    def test_logout_from_lk_true(self, driver):
        # авторизация
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        # переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.LOADER_MODAL))
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.LOADER_MODAL))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON)).click()
        expected = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert expected.is_displayed()