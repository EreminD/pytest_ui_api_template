import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage

def auth_test(browser):
    email = "dmitry.eremin@inbox.ru"
    password = "sky123456"
    username = "Dmitry"
    
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на skyeng_user_d/boards"):
        assert current_url.endswith("skyeng_user_d/boards")
    
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть "+email):
            assert info[1] == email
    
    
    