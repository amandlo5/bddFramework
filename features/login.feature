Feature: Login Functionality

    @login @check
    Scenario Outline: Login with valid credentials
      Given User navigate to login page
      When user enter valid email address is "<email>" and valid password is "<password>" into the fields
      And user click on Login button
      Then user should get logged in
      Examples:
        | email                | password  |
        |amolmandloi@gmail.com | Amol@0143 |
        |amolmandloi@gmail.com | Amol1234  |


    @login
    Scenario: Login with invalid email and valid password
      Given User navigate to login page
      When user enter invalid email and valid password into the fields
      And user click on Login button
      Then user should get a proper warning message

    @login
    Scenario: Login with valid email and invalid password
      Given User navigate to login page
      When user enter valid email and invalid password into the fields
      And user click on Login button
      Then user should get a proper warning message

    @login
    Scenario: Login with invalid credentials
      Given User navigate to login page
      When user enter invalid email and invalid password into the fields
      And user click on Login button
      Then user should get a proper warning message

    @login
    Scenario: Login without entering any credentials
      Given User navigate to login page
      When user dont enter anything into email and password fields
      And user click on Login button
      Then user should get a proper warning message

