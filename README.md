# Sprint_3

в директории `tests` лежат тесты по функциональностям:

`test_auth.py` - файл с тестами на авторизацию:
- `test_login_from_main_page_true` - вход по кнопке «Войти в аккаунт» на главной,
- `test_login_from_privet_acc_true` - вход через кнопку «Личный кабинет»,
- `test_login_from_registration_form_true` - вход через кнопку в форме регистрации,
- `test_login_from_revert_form_true` - вход через кнопку в форме восстановления пароля.

`test_private_acc.py` - файл с тестами для личного кабинета:
- `test_private_acc_click_enter_unreg_true` - переход по клику на «Личный кабинет» НЕавторизованным пользователем
- `test_private_acc_click_enter_reg_true` - переход по клику на «Личный кабинет» авторизованным пользователем
- `test_logout_from_lk_true` - выход из личног каюинета

`constructor.py` - файл с тестами на Конструктор:
- `test_enter_from_lk_true` - Переход в конструктор из Личного кабинета
- `test_burger_logo_tap_true` - Тап на логотип
- `test_sauce_scroll_true` - Подскролл к разделу «Соусы»
- `test_bread_scroll_true` - Подскролл к разделу «Булки»
- `test_fillings_scroll_true` - Подскролл к разделу «Начинки»

`test_registration.py` - файл с тестами на регистрацию пользователя:
- `test_new_user_registration_sucsess` - Тест успешной регистрации
- `test_new_user_registration_incorrect_password_faild` - Тест на регистрацию с невалидным паролем

Файл `Conftest`
содержит фикстуру, используемую в тестах


Файл `Constants`
содержит набор входных данных

Файл `Locators`
Содержит  локаторы тестового проекта