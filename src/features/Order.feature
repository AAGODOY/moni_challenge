Feature: Order

    Examples:
        | user | password  |
        | demo |   demo    |

    Background: As a user logged on opencart application
        Given a user logged with credentials <user> y <password>

    Scenario Outline: Create new order
        When click on sales menu
        And click on orders
        And click on new order button
        And add a <customer>
        And add <products> to the order
        And add payment address
        And select shipping method
        And select payment method
        Then confirm the creation of the order
        And validate the succesffuly order message

    Examples:
        |   customer     |     products      |
        | !Goran Krezic! | HTC Touch HD,iMac |