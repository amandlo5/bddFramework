from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_xpath = "//i[@class='fa fa-user']//following-sibling::span[1]"
    login_link = "Login"
    search_box_name = "search"
    search_button_xpath = "//div[@id='search']//span/button"

    def clickMyAccount(self):
        self.driver.find_element("xpath",self.my_account_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link).click()
        return LoginPage(self.driver)

    def searchBox(self,value):
        self.driver.find_element("name",self.search_box_name).send_keys(value)

    def clickSearch(self):
        self.driver.find_element("xpath",self.search_button_xpath).click()
        return SearchPage(self.driver)