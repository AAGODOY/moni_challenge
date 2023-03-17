from src.core.driver.WebDriver import WebDriver
from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class OrderListPage(BasePage):
    NEW_ORDER_BUTTON = '//a[@aria-label="Add New"]'

    def click_on_new_order_button(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.NEW_ORDER_BUTTON)
        BasePage().click_element(element)