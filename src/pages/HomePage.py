from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    CLOSE_MODAL_NOTIFICATION_BUTTON = 'btn-close'
    HEADER_PROFILE_TEXT = '#header-profile > a > span'

    def click_on_close_modal_notification_button(self):
        element = BasePage().DRIVER.find_element(By.CLASS_NAME, 
                                                 self.CLOSE_MODAL_NOTIFICATION_BUTTON)
        BasePage().click_element(element)

    def get_header_profile_text(self):
        element = BasePage().DRIVER.find_element(By.CSS_SELECTOR, self.HEADER_PROFILE_TEXT)
        return BasePage().get_text(element)