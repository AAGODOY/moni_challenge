from src.pages.LoginPage import LoginPage as login
from src.pages.HomePage import HomePage as home

def do_login(user, password):
    login().complete_user_name_field(user).complete_password_field(password).click_on_Login_button()
    home().click_on_close_modal_notification_button()