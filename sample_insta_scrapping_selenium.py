from selenium import webdriver
from bs4 import BeautifulSoup
import re

username = "nicky.chanana"
password = "nikita123"

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome('chromedriver.exe')
driver.get(getdriver)

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
try:
    button_login = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]')
except:
    button_login = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')

button_login.click()
link = 'https://www.instagram.com/goglambynitika6/'
driver.get(link)
src = driver.page_source
soup = BeautifulSoup(src, "html.parser")
new_emails = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', src)
print(new_emails)
