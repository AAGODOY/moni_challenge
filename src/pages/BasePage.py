from src.core.driver.WebDriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time 

class BasePage():

    def is_visible(self, locator: WebElement):
        try:
            time.sleep(2)
            locator.is_displayed()
        except Exception as e:
            print('Element {} is not visible: '.format(locator))

    def click_element(self, locator: WebElement):
        try:
            locator.click()
            time.sleep(2)
        except Exception as e:
            print('Unable to click element: ', locator)

    def complete_element(self, locator: WebElement, text):
        try:
            locator.send_keys(text)
            time.sleep(2)
        except Exception as e:
            print('Unable to complete element: ', locator)

    def get_text(self, locator: WebElement):
        try:
            time.sleep(2)
            return locator.text
        except Exception as e:
            print('Unable to get text from element: ', locator)

    def scroll_until_element_appears(self, locator):
        WebDriver().get_driver().execute_script("arguments[0].scrollIntoView();", locator)

    def tear_down(self):
        WebDriver().get_driver().quit()
    
    def set_up(self):
        WebDriver().create_driver()