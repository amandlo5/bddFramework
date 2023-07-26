from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_search_Link = "HP LP3065"
    message_xpath = "//input[@id='button-search']//following-sibling::p"

    def validSearch(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_search_Link).is_displayed()

    def errorMessage(self,msg):
        return self.driver.find_element("xpath",self.message_xpath).text.__eq__(msg)