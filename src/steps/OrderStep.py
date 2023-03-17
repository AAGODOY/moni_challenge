import allure, json
from typing import List
from src.core.validation.Assertion import Assertion
from pytest_bdd import scenarios, given, when, then

from src.facades.LoginFacades import do_login
from src.pages.HomePage import HomePage as home
from src.pages.LoginPage import LoginPage as login
from src.pages.OrderListPage import OrderListPage as orderList
from src.pages.CreateOrderPage import CreateOrderPage as createOrder

scenarios('../features/Order.feature')

@allure.step("a user logged with credentials <user> y <password>")
@given("a user logged with credentials <user> y <password>")
def log_in_user(user, password):
    login().set_up()
    do_login(user, password)

@allure.step("click on sales menu")
@when("click on sales menu")
def click_on_sales_menu():
    home().click_on_menu_sale_button()

@allure.step("click on orders")
@when("click on orders")
def click_on_orders():
    home().click_on_order_option_button()

@allure.step("click on new order button")
@when("click on new order button")
def click_on_new_order_button():
    orderList().click_on_new_order_button()

@allure.step("add a <customer>")
@when("add a <customer>")
def add_a_customer(customer):
    createOrder().click_modal_customer_button().click_on_customer_input().complete_customer_input('sarasa').\
        complete_customer_input(customer).click_on_save_customer_button()
    Assertion().assertEquals(failedMessage='Error on the alert message when add a customer', 
                             expectedValue='You have successfully modified customers',
                             actualValue=createOrder().get_success_alert_text())
    createOrder().click_on_close_modal_customer()
    
@allure.step("add <products> to the order")
@when("add <products> to the order")
def add_a_customer(products: str):
    createOrder().click_on_add_new_product()
    products_list = products.split(',')
    for product in products_list:
        createOrder().click_choose_product_input(product).click_on_save_product_button()
        Assertion().assertEquals(failedMessage='Error on the alert message when add a product',
                               expectedValue='Success: You have modified your shopping cart!',
                               actualValue=createOrder().get_success_alert_text())
    createOrder().click_on_close_modal_product_button()

@allure.step("add payment address")
@when("add payment address")
def add_payment_address():
    createOrder().click_on_add_payment_address().click_on_payment_address_input().\
        click_on_first_address_in_list().click_on_save_payment_address_button()
    Assertion().assertEquals(failedMessage='Error on the alert message when add a payment address',
                        expectedValue='Success: Payment address has been set!',
                        actualValue=createOrder().get_success_alert_text())
    createOrder().click_on_close_modal_payment_address_button()


@allure.step("select shipping method")
@when("select shipping method")
def select_shipping_method():
    createOrder().click_on_refresh_shipping_method_button().click_on_shipping_method_drop_down().\
        click_on_shipping_method_option()
    Assertion().assertEquals(failedMessage='Error on the alert message when add a payment address',
                        expectedValue='Success: Shipping method has been set!',
                        actualValue=createOrder().get_success_alert_text())
    
@allure.step("select payment method")
@when("select payment method")
def select_payment_method():
    createOrder().click_on_refresh_payment_method_button().click_on_payment_method_drop_down().\
        click_on_payment_method_option()
    Assertion().assertEquals(failedMessage='Error on the alert message when add a payment address',
                        expectedValue='Success: Payment method has been set!',
                        actualValue=createOrder().get_success_alert_text())
    
@allure.step("confirm the creation of the order")
@then("confirm the creation of the order")
def click_on_confirm_order():
    createOrder().click_on_confirm_order_button()

@allure.step("validate the succesffuly order message")
@then("validate the succesffuly order message")
def click_on_confirm_order():
    Assertion().assertEquals(failedMessage='Error on the alert message when add a payment address',
                    expectedValue='Success: You have modified orders!',
                    actualValue=createOrder().get_success_alert_text())
    login().tear_down()