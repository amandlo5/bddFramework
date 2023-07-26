from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_name = "email"
    password_name = "password"
    login_xpath = "//input[@type='submit']"
    warning_xpath = "//div[@id='account-login']//div[1]"

    def enterEmail(self,email):
        self.driver.find_element("name",self.email_name).send_keys(email)

    def enterPassword(self,password):
        self.driver.find_element("name",self.password_name).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element("xpath",self.login_xpath).click()
        return AccountPage(self.driver)


    def warningMsg(self,expected_message):
        return self.driver.find_element("xpath",self.warning_xpath).text.__contains__(expected_message)