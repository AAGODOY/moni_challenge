from src.core.driver.WebDriver import WebDriver
from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time 

class CreateOrderPage(BasePage):
    MODAL_CUSTOMER_BUTTON = '//button[@data-bs-target="#modal-customer"]'
    CUSTOMER_INPUT = 'input-customer'
    SAVE_CUSTOMER_BUTTON = 'button-customer'
    SUCCESS_ALERT = '//div[contains(@class,"alert-success")]'
    CLOSE_MODAL_CUSTOMER = '(//div[@id="modal-customer"]//button[@class="btn-close"])[1]'
    MODAL_PRODUCT_BUTTON = '//button[@data-bs-target="#modal-cart"]'
    PRODUCT_INPUT = 'input-product'
    SAVE_PRODUCT_BUTTON = 'button-product-add'
    CLOSE_MODAL_PRODUCT = '(//div[@id="modal-cart"]//button[@class="btn-close"])[1]'
    MODAL_PAYMENT_ADDRESS_BUTTON = '//button[@data-bs-target="#modal-payment-address"]'
    PAYMENT_ADDRESS_INPUT = 'input-payment-address'
    FIRST_ADDRESS_IN_LIST = '//select[@id="input-payment-address"]/option[2]'
    SAVE_PAYMENT_ADDRESS_BUTTON = 'button-payment-address'
    CLOSE_MODAL_PAUMENT_ADDRESS = '//div[@id="modal-payment-address"]//button[@class="btn-close"]'
    REFRESH_SHIPPING_METHOD_BUTTON = 'button-shipping-method'
    SHIPPING_METHOD_DROP_DOWN = 'input-shipping-method'
    SHIPPING_METHOD_OPTION = '//select[@id="input-shipping-method"]/optgroup/option'
    REFRESH_PAYMENT_METHOD_BUTTON = 'button-payment-method'
    PAYMENT_METHOD_DROP_DOWN = 'input-payment-method'
    PAYMENT_METHOD_OPTION = '//select[@id="input-payment-method"]/option[2]'
    CONFIRM_ORDER_BUTTON = 'button-confirm'

    def click_modal_customer_button(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.MODAL_CUSTOMER_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_on_customer_input(self):
        element = WebDriver().get_driver().find_element(By.ID, self.CUSTOMER_INPUT)
        BasePage().click_element(element)
        return self
    
    def complete_customer_input(self, customer):
        element = WebDriver().get_driver().find_element(By.ID, self.CUSTOMER_INPUT)
        element.clear()
        BasePage().complete_element(element, customer)
        BasePage().keys_enter()
        return self
    
    def click_on_save_customer_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.SAVE_CUSTOMER_BUTTON)
        BasePage().click_element(element)
        return self

    def get_success_alert_text(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.SUCCESS_ALERT)
        return BasePage().get_text(element)
    
    def click_on_close_modal_customer(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.CLOSE_MODAL_CUSTOMER)
        BasePage().click_element(element)
        return self
    
    def click_on_add_new_product(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.MODAL_PRODUCT_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_choose_product_input(self, product):
        time.sleep(2)
        element = WebDriver().get_driver().find_element(By.ID, self.PRODUCT_INPUT)
        BasePage().click_element(element)
        BasePage().complete_element(element, product)
        return self

    def click_on_save_product_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.SAVE_PRODUCT_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_on_close_modal_product_button(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.CLOSE_MODAL_PRODUCT)
        BasePage().click_element(element)
        return self 
    
    def click_on_add_payment_address(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.MODAL_PAYMENT_ADDRESS_BUTTON)
        BasePage().scroll_down_until_element_appears(element)
        BasePage().click_element(element)
        return self 
    
    def click_on_payment_address_input(self):
        element = WebDriver().get_driver().find_element(By.ID, self.PAYMENT_ADDRESS_INPUT)
        BasePage().click_element(element)
        return self 

    def click_on_first_address_in_list(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.FIRST_ADDRESS_IN_LIST)
        BasePage().click_element(element)
        return self 
    
    def click_on_save_payment_address_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.SAVE_PAYMENT_ADDRESS_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_on_close_modal_payment_address_button(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.CLOSE_MODAL_PAUMENT_ADDRESS)
        BasePage().click_element(element)
        return self 
    
    def click_on_refresh_shipping_method_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.REFRESH_SHIPPING_METHOD_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_on_shipping_method_drop_down(self):
        element = WebDriver().get_driver().find_element(By.ID, self.SHIPPING_METHOD_DROP_DOWN)
        BasePage().click_element(element)
        return self
    
    def click_on_shipping_method_option(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.SHIPPING_METHOD_OPTION)
        BasePage().click_element(element)
        return self
    
    def click_on_refresh_payment_method_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.REFRESH_PAYMENT_METHOD_BUTTON)
        BasePage().click_element(element)
        return self
    
    def click_on_payment_method_drop_down(self):
        element = WebDriver().get_driver().find_element(By.ID, self.PAYMENT_METHOD_DROP_DOWN)
        BasePage().click_element(element)
        return self
    
    def click_on_payment_method_option(self):
        element = WebDriver().get_driver().find_element(By.XPATH, self.PAYMENT_METHOD_OPTION)
        BasePage().click_element(element)
        return self
    
    def click_on_confirm_order_button(self):
        element = WebDriver().get_driver().find_element(By.ID, self.CONFIRM_ORDER_BUTTON)
        BasePage().click_element(element)
        return self