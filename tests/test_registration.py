from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import Locators

faker = Faker()


class TestRegistration:

    # Тест успешной регистрации
    def test_new_user_registration_sucsess(self, driver):
        # переход к форме регистрации
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LINK_ENTER_REG)).click()

        # заполнение формы регистрации
        new_name = faker.name()
        new_email = faker.email()

        driver.find_element(*Locators.NAME).send_keys(new_name)  # имя в форме регистрации (вводим валидное)
        driver.find_element(*Locators.EMAIL).send_keys(new_email)  # емайл в форме регистрации
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)  # валидный пароль в форме регистрации

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.BUTTON_REG_ENTER)).click()  # кнопка зарегестрироваться
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(new_email)  # емайл в форме регистрации
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)  # пароль в форме регистрации
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.LOADER_MODAL))
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_FORM))
        expected_name = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)).get_attribute('value')
        expected_email = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)).get_attribute('value')
        assert expected_name == new_name and expected_email == new_email

    # Тест на регистрацию с невалидным паролем
    def test_new_user_registration_incorrect_password_faild(self, driver):
        # переход к форме регистрации
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.PRIVET_ACC)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.LINK_ENTER_REG)).click()

        # заполнение формы регистрации
        new_name = faker.name()
        new_email = faker.email()

        driver.find_element(*Locators.NAME).send_keys(new_name)  # имя в форме регистрации (вводим валидное)
        driver.find_element(*Locators.EMAIL).send_keys(new_email)  # емайл в форме регистрации
        driver.find_element(*Locators.PASSWORD).send_keys(
            Constants.INCORRECT_PASSWORD)  # НЕвалидный пароль в форме регистрации

        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.BUTTON_REG_ENTER)).click()  # кнопка зарегестрироваться

        error_message = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ERROR_PASSWORD_MESSAGE)).text
        assert error_message == Constants.INCORRECT_PASSWORD_MESSAGE
