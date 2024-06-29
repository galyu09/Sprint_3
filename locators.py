from selenium.webdriver.common.by import By


class Locators:

    ENTER_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # модальный лоадер
    LOADER_MODAL = (By.XPATH, './/img[contains(@class, "Modal_modal__loading__")]')

    # кнопка 'Войти в аккаунт' на главной
    ENTER_BUTTON = (By.XPATH, './/button[contains(@class, "button_button__")]')

    # поле ввода email
    EMAIL = (By.XPATH, './/label[text()="Email"]/following-sibling::input')

    # поле ввода пароля
    PASSWORD = (By.XPATH, './/input[@name="Пароль"]')  # форма для ввода пароля

    # поле ввода имени
    NAME = (By.NAME, 'name')

    # кнопка 'Войти' в форме авторизации
    LOGIN_BUTTON = (By.XPATH, './/button[contains(text(),"Войти")]')

    # Заголовок 'Соберите бургер' на главной странице
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # Кнопка оформить заказ на главной странице
    CHECKOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # кнопка входа в личный кабинет
    PRIVET_ACC = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Заголовок Вход на странице Личный кабинет
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[contains(text(),'Вход')]")

    # Кнопка регистрации на странице register
    LINK_ENTER_REG = (By.XPATH, '//a[contains(@class, "Auth_link")]')

    LINK_ENTER_SET_PAS = (By.XPATH, '//a[contains(@class, "Auth_link__1fOlj")]')

    # Кнопка Зарегестрироваться в форме регистрации
    BUTTON_REG_ENTER = (By.XPATH, '//button[contains(@class, "button_button__")]')

    # Уведомление о вводе неправильного пароля
    PASSWORD_FAIL = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Кнопка востановить пароль на странице /login
    SET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")

    # логотип Stellar Burgers
    BURGER_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo__')]")

    # кнопка выхода из аккаунта из Личного кабинета (на страничке профиля)
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")


    # Вкладка Булки
    BREAD = (By.XPATH, "//span[text()='Булки']/..")
    # Вкладка Соусы
    SAUCES = (By.XPATH, "//span[text()='Соусы']/..")
    # Начинки "
    FILLINGS = (By.XPATH, "//span[text()='Начинки']/..")

    # Форма профиля
    PROFILE_FORM = (By.XPATH, "//div[contains(@class, 'Account_content')]")
    NAME_FIELD = (By.XPATH, '//input[@name="Name"]')
    EMAIL_FIELD = (By.XPATH, '(//input[@name="name"])[1]')

    ERROR_PASSWORD_MESSAGE = (By.XPATH, '//p[contains(@class, "input__error")]')



