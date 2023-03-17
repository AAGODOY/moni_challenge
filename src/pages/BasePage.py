from src.core.driver.WebDriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
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
            time.sleep(1)
        except Exception as e:
            print('Unable to click element: ', locator)

    def complete_element(self, locator: WebElement, text):
        try:
            locator.clear()
            locator.send_keys(text)
            time.sleep(2)
        except Exception as e:
            print('Unable to complete element: ', locator)

    def get_text(self, locator: WebElement):
        try:
            time.sleep(0.01)
            return locator.text
        except Exception as e:
            print('Unable to get text from element: ', locator)


    def scroll_down_until_element_appears(self, locator):
        WebDriver().get_driver().execute_script("arguments[0].scrollIntoView();", locator)
        time.sleep(0.5)

    def scroll_up_to_the_site(self):
        WebDriver().get_driver().find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_UP)

    def keys_enter(self):
        ActionChains(WebDriver().get_driver()).send_keys(Keys.ENTER).perform()

    def keys_tab(self):
        ActionChains(WebDriver().get_driver()).send_keys(Keys.TAB * 2).perform()

    def tear_down(self):
        WebDriver().get_driver().quit()
    
    def set_up(self):
        WebDriver().create_driver()