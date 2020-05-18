import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
import re

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
link = 'view-source:https://www.linkedin.com/feed/hashtag/covid19/'
browser.get(link)
src = browser.page_source
soup = BeautifulSoup(src, "html.parser")
new_emails = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', src)
print(new_emails)

# abc = 'https://www.google.com/'
# elementID.submit()
# link = 'view-source:https://www.linkedin.com/feed/hashtag/covid19/'
# # browser.get(link)
# response = requests.get(link)
# soup = BeautifulSoup(response.text, 'html.parser')
# # soup = BeautifulSoup(src, "html.parser")
# new_emails = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
# print(new_emails)