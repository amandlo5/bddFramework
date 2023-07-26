from datetime import datetime

from behave import *
from selenium import webdriver
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from features.pages.AccountPage import AccountPage
from selenium.webdriver.common.by import By
from utilities import commonmethods

@given('User navigate to login page')
def navigateLogin(context):
    context.home = HomePage(context.driver)
    context.home.clickMyAccount()
    context.login = context.home.clickLogin()


@when('user enter valid email address is "{email}" and valid password is "{pwd}" into the fields')
def validCredentials(context,email,pwd):

    context.login.enterEmail(email)
    context.login.enterPassword(pwd)


@when(u'user click on Login button')
def clickLogin(context):
    context.account = context.login.clickOnLogin()


@then(u'user should get logged in')
def loggedIn(context):
    assert context.account.getTitle()



@when(u'user enter invalid email and valid password into the fields')
def invalidEmail(context):
    context.invalid_email = commonmethods.generateEmailRandom()
    context.login.enterEmail(context.invalid_email)
    context.login.enterPassword("Amol@0143")


@then(u'user should get a proper warning message')
def warningMessage(context):
    context.exp_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login.warningMsg(context.exp_message)



@when(u'user enter valid email and invalid password into the fields')
def invalidPassword(context):
    context.login.enterEmail("amolmandloi@gmail.com")
    context.login.enterPassword("Amol@014353")


@when(u'user enter invalid email and invalid password into the fields')
def invalidCredentials(context):
    context.invalid_email = commonmethods.generateEmailRandom()
    context.login.enterEmail(context.invalid_email)
    context.login.enterPassword("Amol@014353")



@when(u'user dont enter anything into email and password fields')
def dontEnter(context):
    context.login.enterEmail("")
    context.login.enterPassword("")



