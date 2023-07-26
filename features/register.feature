Feature: Register Account Functionality

    @register @runonly
    Scenario: Register with mandatory fields
      Given User navigate to register page
      When user enter details into mandatory fields
          |first_name|last_name|telephone |password|
          |Amul      |Mondal   |1234567890|12345   |

      And user click on continue button
      Then Account should be created

    @register @runonly
    Scenario: Register with all fields
      Given User navigate to register page
      When user enter details into all fields
      And user click on continue button
      Then Account should be created

    @register
    Scenario: Register with duplicate email address
      Given User navigate to register page
      When user enter details into all fields except email field
      And user enter existing account email into email field
      And user click on continue button
      Then Proper warning message informing about duplicate account should be displayed

    @register
    Scenario: Register without providing any details
      Given User navigate to register page
      When user dont enter anything into fields
      And user click on continue button
      Then Proper warning message for every mandatory fields should be displayed