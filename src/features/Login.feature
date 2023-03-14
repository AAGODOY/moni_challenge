Feature: Login

    Scenario Outline: Validate correct login
        Given located on login page
        When complete <user> field
        And complete <password> field
        And click on Login button
        Then user is succesffuly logged with <first_name> and <last_name>

    Examples:
        | user | password | first_name | last_name |
        | demo |   demo   |    demo    |   demo    |