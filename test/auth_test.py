from page.AuthPage import AuthPage
from page.MainPage import MainPage

def auth_test(browser):
    email = "dmitry.eremin@inbox.ru"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "sky123456")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    assert main_page.get_current_url().endswith("skyeng_user_d/boards")
    assert info[0] == "Dmitry"
    assert info[1] == email
    
    
    