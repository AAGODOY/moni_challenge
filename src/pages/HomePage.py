from src.core.driver.WebDriver import WebDriver
from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    CLOSE_MODAL_NOTIFICATION_BUTTON = 'btn-close'
    HEADER_PROFILE_TEXT = '#header-profile > a > span'
    LOGOUT_BUTTON = 'header-logout'
    MENU_SALE_BUTTON = 'menu-sale'
    ORDER_OPTION_BUTTON = '//li[@id="menu-sale"]/ul/li/a[text()="Orders"]'

    def click_on_close_modal_notification_button(self):
        element = WebDriver().get_driver().find_element(By.CLASS_NAME, 
                                                 self.CLOSE_MODAL_NOTIFICATION_BUTTON)
        BasePage().click_element(element)

    def get_header_profile_text(self):
        element = WebDriver().get_driver().find_element(By.CSS_SELECTOR, self.HEADER_PROFILE_TEXT)
        return BasePage().get_text(element)

    def click_on_logout_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.LOGOUT_BUTTON)
        BasePage().click_element(element)

    def click_on_menu_sale_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.MENU_SALE_BUTTON)
        BasePage().click_element(element)
    
    def click_on_order_option_button(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.ORDER_OPTION_BUTTON)
        BasePage().click_element(element)