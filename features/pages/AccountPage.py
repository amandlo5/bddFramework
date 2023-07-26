from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    title_link = "Qafox.com"

    def getTitle(self):
        return self.driver.find_element(By.LINK_TEXT,self.title_link).is_displayed()

