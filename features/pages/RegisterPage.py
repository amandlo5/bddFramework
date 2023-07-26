from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_xpath = "//i[@class='fa fa-user']//following-sibling::span[1]"
    register_link = "Register"
    fname_name = "firstname"
    lname_name = "lastname"
    email_name = "email"
    telephone_name = "telephone"
    password_name = "password"
    confirm_name = "confirm"
    radio_left_xpath = "//input[@name='newsletter'][@value='1']"
    radio_right_xpath = "//input[@name='newsletter'][@value='2']"
    privacy_xpath = "//input[@type='checkbox']"
    duplicate_xpath = "//div[@id='account-register']//div[1]"
    warning_privacy_xpath = "//div[@id='account-register']//div[1]"
    expected_fname = "//input[@id='input-firstname']//following-sibling::div"
    expected_lname = "//input[@id='input-lastname']//following-sibling::div"
    expected_email = "//input[@id='input-email']//following-sibling::div"
    expected_telephone = "//input[@id='input-telephone']//following-sibling::div"
    expected_password = "//input[@id='input-password']//following-sibling::div"
    continue_xpath = "//input[@value='Continue']"
    account_created_xpath = "//div[@id='content']/h1"

    def clickMyAccount(self):
        self.driver.find_element("xpath", self.my_account_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.register_link).click()

    def setFname(self,fname):
        self.driver.find_element("name",self.fname_name).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element("name",self.lname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element("name",self.email_name).send_keys(email)

    def setTelephone(self,tel):
        self.driver.find_element("name",self.telephone_name).send_keys(tel)

    def setPassword(self,password):
        self.driver.find_element("name",self.password_name).send_keys(password)

    def confirmPassword(self,cnf):
        self.driver.find_element("name",self.confirm_name).send_keys(cnf)

    def selectRadio(self,select):
        if select == '1':
            self.driver.find_element("xpath",self.radio_left_xpath).click()
        elif select ==2:
            self.driver.find_element("xpath",self.radio_right_xpath).click()

    def clickPrivacy(self):
        self.driver.find_element("xpath",self.privacy_xpath).click()

    def duplicateMessage(self,exp):
        return self.driver.find_element("xpath",self.duplicate_xpath).text.__contains__(exp)

    def warningPrivacy(self,exp1):
        return self.driver.find_element("xpath",self.warning_privacy_xpath).text.__contains__(exp1)

    def errorFname(self,errorFname):
        return self.driver.find_element("xpath",self.expected_fname).text.__eq__(errorFname)

    def errorLname(self,errorLname):
        return self.driver.find_element("xpath",self.expected_lname).text.__eq__(errorLname)

    def errorEmail(self,errorEmail):
        return self.driver.find_element("xpath",self.expected_email).text.__eq__(errorEmail)

    def errorTelephone(self,errorTelephone):
        return self.driver.find_element("xpath",self.expected_telephone).text.__eq__(errorTelephone)

    def errorPassword(self,errorPassword):
        return self.driver.find_element("xpath",self.expected_password).text.__eq__(errorPassword)

    def clickContinue(self):
        self.driver.find_element("xpath",self.continue_xpath).click()

    def accountCreated(self,exp2):
        return self.driver.find_element("xpath",self.account_created_xpath).text.__eq__(exp2)