import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'normal'
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(10)

#Simple alert
# driver.find_element(By.XPATH,"//button[contains(text(),'Simple Alert')]").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

#Confitm or cancel alert
'''driver.find_element(By.XPATH,"//button[contains(text(),'Confirmation Alert')]").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
# alert.accept()
alert.dismiss()
time.sleep(2)
text = driver.find_element(By.XPATH,"//div[@class='widget-content']/p[@id='demo']").text
if 'OK!' in text:
    print('Alert accepted')
elif 'Cancel!' in text:
    print('Alert dismissed')
else:
    print('Nothing')'''

#ALert message pass
'''driver.find_element(By.XPATH,"//button[contains(text(),'Prompt Alert')]").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys(Keys.CLEAR)
time.sleep(2)
alert.send_keys('Amol Mandloi')
time.sleep(2)
alert.accept()
text = driver.find_element(By.XPATH,"//div[@class='widget-content']/p[@id='demo']").text
print(text)
time.sleep(5)'''

#authentication pop up
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(3)