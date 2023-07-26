import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.pages.RegisterPage import RegisterPage
from utilities import commonmethods


@given(u'User navigate to register page')
def navigateRegister(context):
    context.register = RegisterPage(context.driver)
    context.register.clickMyAccount()
    context.register.clickRegister()
    time.sleep(3)


@when(u'user enter details into mandatory fields')
def mandatoryFields(context):
    for row in context.table:
        context.driver.execute_script("window.scrollBy(0,1200)")
        time.sleep(3)
        context.register.setFname(row["first_name"])
        context.register.setLname(row["last_name"])
        context.email = commonmethods.generateEmailRandom()
        context.register.setEmail(context.email)
        time.sleep(3)
        context.register.setTelephone(row["telephone"])
        context.register.setPassword(row["password"])
        context.register.confirmPassword(row["password"])
        context.register.clickPrivacy()
        time.sleep(3)


@when(u'user click on continue button')
def clickContinue(context):
    context.register.clickContinue()


@then(u'Account should be created')
def accountCreated(context):
    expected_text = "Your Account Has Been Created!"
    assert context.register.accountCreated(expected_text)


@when(u'user enter details into all fields')
def allFields(context):
    context.driver.execute_script("window.scrollBy(0,1000)")
    context.register.setFname("Amol")
    context.register.setLname("Robot")
    email = commonmethods.generateEmailRandom()
    context.register.setEmail(email)
    time.sleep(3)
    context.register.setTelephone("1234567890")
    context.register.setPassword("12345")
    context.register.confirmPassword("12345")
    context.register.selectRadio("1")
    time.sleep(3)
    context.register.clickPrivacy()
    time.sleep(3)


@when(u'user enter details into all fields except email field')
def exceptEmail(context):
    context.driver.execute_script("window.scrollBy(0,1000)")
    context.register.setFname("Amol")
    context.register.setLname("Robot")
    time.sleep(3)
    context.register.setTelephone("1234567890")
    context.register.setPassword("12345")
    context.register.confirmPassword("12345")
    context.register.selectRadio("1")
    time.sleep(3)
    context.register.clickPrivacy()


@when(u'user enter existing account email into email field')
def emailIntoEmail(context):
    context.register.setEmail("amolmandloi@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def duplicateMessage(context):
    expected_warning = "Warning: E-Mail Address is already registered"
    assert context.register.duplicateMessage(expected_warning)


@when(u'user dont enter anything into fields')
def dontEnter(context):
    context.driver.execute_script("window.scrollBy(0,1000)")
    context.register.setFname("")
    context.register.setLname("")
    context.register.setEmail("")
    time.sleep(3)
    context.register.setTelephone("")
    context.register.setPassword("")
    context.register.confirmPassword("")


@then(u'Proper warning message for every mandatory fields should be displayed')
def everyMandatory(context):
    expected_privacy = "Warning: You must agree to the Privacy Policy!"
    expected_fname = "First Name must be between 1 and 32 characters!"
    expected_lname = "Last Name must be between 1 and 32 characters!"
    expected_email = "E-Mail Address does not appear to be valid!"
    expected_telephone = "Telephone must be between 3 and 32 characters!"
    expected_password = "Password must be between 4 and 20 characters!"
    assert context.register.warningPrivacy(expected_privacy)
    assert context.register.errorFname(expected_fname)
    assert context.register.errorLname(expected_lname)
    assert context.register.errorEmail(expected_email)
    assert context.register.errorTelephone(expected_telephone)
    assert context.register.errorPassword(expected_password)

