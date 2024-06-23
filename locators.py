from selenium.webdriver.common.by import By


class Locators:

    """блок авторизации"""
    # кнопка 'Войти в аккаунт' на главной
    ENTER_BUTTON = (By.XPATH, './/button[contains(@class, "button_button__")]')

    # email
    EMAIL = (By.XPATH, './/label[text()="Email"]/following-sibling::input')

    # пароль
    PASSWORD = (By.XPATH, './/input[@name="Пароль"]')  # форма для ввода пароля

    # кнопка 'Войти' в форме авторизации
    LOGIN_BUTTON = (By.XPATH, './/button[contains(text(),"Войти")]')

    # Заголовок 'Соберите бургер' на главной странице
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # кнопка входа в личный кабинет
    PRIVET_ACC = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Заголовок Вход на странице /login
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[contains(text(),'Вход')]")

    """блок регистрации"""

    # логин
    LOGIN = (By.XPATH, './/input[@name="name"]')
    GET_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Уведомление о вводе неправильного пароля
    PASSWORD_FAIL = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Кнопка входа на страницах register и login


    # Кнопка регистрации на странице register
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')

    # Кнопка востановить пароль на странице /login
    button_password_setting = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Кнопака Войти на странице register
    button_login_reg_form = (By.XPATH, "//a[contains(text(),'Войти')]")

    # Заголовок Вход на странице /login
    #TITLE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")


    # Ссылка для входа в раздел конструктор
    link_constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Ссылка на логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')


# class MainPage:
    # Кнопка войти в аккаунт на главной странице
    button_login = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Заголовок на главной стрице Соберите бургер
    title_main_page = (By.XPATH, "//h1[text() = 'Соберите бургер']")

    # Кнопка оформить заказ на главной странице
    button_checkout = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Активная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Секция соусов
    sauce_element = (By.XPATH, "//span[text() = 'Соусы']")

    # Секция Булки
    bread_element = (By.XPATH, "//span[text() = 'Булки']")

    # Секция Начинки
    filling_element = (By.XPATH, "//span[text() = 'Начинки']")


# class ProfilePage:
    # Кнопка выхода из Личного кабинета
    button_exit = (By.XPATH, "//button[contains(text(),'Выход')]")