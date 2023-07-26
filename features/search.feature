Feature: Search Functionality



  @search
  Scenario: Search for valid product
    Given User navigates to homepage
    When User enter valid product in search box field
    And user click on Search button
    Then valid product should get displayed in Search Results

  @search
  Scenario: Search for invalid product
    Given User navigates to homepage
    When user enters invalid product in search box field
    And user click on search button
    Then proper message should be displayed in Search Results

  @search
  Scenario: Search without entering any product
    Given User navigates to homepage
    When user dont enter anything into search box field
    And user click on search button
    Then proper message should be displayed in Search Results