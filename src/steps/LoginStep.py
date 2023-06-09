import allure
from src.core.validation.Assertion import Assertion
from pytest_bdd import scenarios, given, when, then

from src.pages.LoginPage import LoginPage as login
from src.pages.HomePage import HomePage as home

scenarios('../features/Login.feature')

@allure.step("located on login page")
@given("located on login page")
def locate_on_login_page():
    login().set_up()
    login().validate_visibility_of_user_name_field().validate_visibility_of_password_field()

@allure.step("complete <user> field")
@when("complete <user> field")
def complete_user_field(user):
    login().complete_user_name_field(user)

@allure.step("complete <password> field")
@when("complete <password> field")
def complete_password_field(password):
    login().complete_password_field(password)

@allure.step("click on Login button")
@when("click on Login button")
def click_on_login_button():
    login().click_on_Login_button()


@allure.step("user is succesffuly logged with <first_name> and <last_name>")
@then("user is succesffuly logged with <first_name> and <last_name>")
def user_is_successfully_logged(first_name, last_name):
    home().click_on_close_modal_notification_button()
    Assertion().assertEquals(failedMessage='The header profile text is incorrect', 
                             expectedValue=first_name + ' ' + last_name,
                             actualValue=home().get_header_profile_text().strip())
    login().tear_down()

@allure.step("an error alert is displayed")
@then("an error alert is displayed")
def user_is_successfully_logged():
    Assertion().assertEquals(failedMessage="The alert wasn't displayed", 
                             expectedValue='No match for Username and/or Password.',
                             actualValue=login().get_alert_text())
    login().tear_down()

@allure.step("click on Logout button")
@when("click on Logout button")
def click_on_logout_button():
    home().click_on_close_modal_notification_button()
    home().click_on_logout_button()

@allure.step("user is succesfully logout")
@then("user is succesfully logout")
def user_is_successfully_logout():
    login_button_validation = login().is_login_button_visible() != None
    Assertion().assertTrue(failedMessage='Error when logout', value=login_button_validation)