from src.core.driver.WebDriver import WebDriver
from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USER_NAME_FIELD = 'input-username'
    PASSWORD_FILED = 'input-password'
    LOGIN_BUTTON = '.text-end > button'
    ERROR_ALERT = '#alert > div'

    def validate_visibility_of_user_name_field(self):
        element = WebDriver().get_driver().find_element(By.ID, self.USER_NAME_FIELD)
        BasePage().is_visible(element)
        return self

    def validate_visibility_of_password_field(self):
        element = WebDriver().get_driver().find_element(By.ID, self.PASSWORD_FILED)
        BasePage().is_visible(element)
        return self

    def complete_user_name_field(self, user_name):
        element = WebDriver().get_driver().find_element(By.ID, self.USER_NAME_FIELD)
        BasePage().complete_element(element, user_name)
        return self

    def complete_password_field(self, password):
        element = WebDriver().get_driver().find_element(By.ID, self.PASSWORD_FILED)
        BasePage().complete_element(element, password)
        return self

    def click_on_Login_button(self):
        element = WebDriver().get_driver().find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON)
        BasePage().click_element(element)
        return self
    
    def get_alert_text(self):
        element = WebDriver().get_driver().find_element(By.CSS_SELECTOR, self.ERROR_ALERT)
        return BasePage().get_text(element)
    
    def is_login_button_visible(self):
        return WebDriver().get_driver().find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON)