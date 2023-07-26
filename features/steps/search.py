from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage
from utilities.loggerConfig import LogGen

logger = LogGen.logGen()
@given(u'User navigates to homepage')
def navigateHomepage(context):
    logger.info("TC started***************")
    assert context.driver.title.__eq__("Your Store")


@when(u'User enter valid product in search box field')
def enterSearchBox(context):
    context.home = HomePage(context.driver)
    context.home.searchBox("HP")


@when(u'user click on Search button')
def clickSearch(context):
    context.home = HomePage(context.driver)
    context.search = context.home.clickSearch()


@then(u'valid product should get displayed in Search Results')
def validProduct(context):
    assert context.search.validSearch()


@when(u'user enters invalid product in search box field')
def invalidProduct(context):
    context.home = HomePage(context.driver)
    context.home.searchBox("Honda")
    logger.error("Info")


@then(u'proper message should be displayed in Search Results')
def messageProper(context):
    assert context.search.errorMessage("There is no product that matches the search criteria.abc")



@when(u'user dont enter anything into search box field')
def emptySearch(context):
    context.home = HomePage(context.driver)
    context.home.searchBox("")
    logger.info("TC ended***************")